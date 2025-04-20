"""
Module for handling top artists endpoints in the Spotistats API
"""
from flask import jsonify
import pandas as pd
from datetime import datetime

def register_routes(app, user_data):
    """Register top artists routes with the Flask app"""
    
    @app.route('/top_artists/<session_id>', methods=['GET'])
    def top_artists(session_id):
        """Get top artists by listening time and play count"""
        
        # Check if session exists
        if session_id not in user_data:
            return jsonify({'error': 'Session not found'}), 404
            
        # Get the data for this session
        df = user_data[session_id]
        
        # Ensure required columns exist
        required_columns = ['master_metadata_album_artist_name', 'ms_played']
        missing_columns = [col for col in required_columns if col not in df.columns]
        
        if missing_columns:
            return jsonify({
                'error': f'Missing required columns: {missing_columns}',
                'available_columns': list(df.columns)
            }), 400
        
        # Process the data similar to the notebook
        # 1. Convert timestamps to datetime if needed
        if 'ts' in df.columns:
            df['Play-Time'] = pd.to_datetime(df['ts'])
        
        # 2. Add a Count column for counting plays
        df['Count'] = 1
        
        # 3. Convert ms_played to hours
        def ms_to_hours(ms):
            return (ms / 1000) / 3600  # ms to seconds to hours
        
        df['Listening Time (Hours)'] = df['ms_played'].apply(ms_to_hours).round(3)
        
        # 4. Group by artist and calculate totals
        artist_column = 'master_metadata_album_artist_name'
        top_artists_df = df.groupby(artist_column).agg({
            'Listening Time (Hours)': 'sum',
            'Count': 'sum'
        }).reset_index()
        
        # 5. Get top 10 by listening time
        top_by_hours = top_artists_df.sort_values(
            by='Listening Time (Hours)', 
            ascending=False
        ).head(10).to_dict(orient='records')
        
        # 6. Get top 10 by play count
        top_by_count = top_artists_df.sort_values(
            by='Count', 
            ascending=False
        ).head(10).to_dict(orient='records')
        
        return jsonify({
            'top_artists_by_time': top_by_hours,
            'top_artists_by_count': top_by_count,
            'total_unique_artists': df[artist_column].nunique(),
            'total_listening_hours': df['Listening Time (Hours)'].sum().round(2)
        })
    
    @app.route('/artist_stats/<session_id>/<artist_name>', methods=['GET'])
    def artist_stats(session_id, artist_name):
        """Get detailed stats for a specific artist"""
        
        # Check if session exists
        if session_id not in user_data:
            return jsonify({'error': 'Session not found'}), 404
            
        # Get the data for this session
        df = user_data[session_id]
        
        # Filter for the artist
        artist_column = 'master_metadata_album_artist_name'
        if artist_column not in df.columns:
            return jsonify({'error': f'Column {artist_column} not found in data'}), 400
        
        artist_data = df[df[artist_column] == artist_name]
        
        if len(artist_data) == 0:
            return jsonify({'error': f'No data found for artist: {artist_name}'}), 404
        
        # Process ms_played if it exists
        if 'ms_played' in artist_data.columns:
            total_ms = artist_data['ms_played'].sum()
            hours = total_ms / (1000 * 60 * 60)  # Convert ms to hours
        else:
            hours = 0
        
        # Get unique tracks
        track_column = 'master_metadata_track_name'
        unique_tracks = []
        if track_column in artist_data.columns:
            unique_tracks = artist_data[track_column].unique().tolist()
        
        # Return stats
        return jsonify({
            'artist_name': artist_name,
            'play_count': len(artist_data),
            'listening_time_hours': round(hours, 2),
            'unique_tracks': len(unique_tracks),
            'track_list': unique_tracks[:50]  # Limit to 50 tracks to avoid huge responses
        })
