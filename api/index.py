from flask import Flask, request, jsonify, make_response
import pandas as pd
import json
import os
import tempfile
import uuid
from io import StringIO

import sys
from pathlib import Path

# Add the current directory to the path so we can import top_artists
sys.path.append(str(Path(__file__).parent))
import top_artists

app = Flask(__name__)

# Storage for user data (in-memory for demo purposes)
# In production, you'd use a database
user_data = {}

@app.route('/')
def home():
    return 'welcome to spotistats backend'

@app.route('/test')
def test():
    return 'health check'

@app.route('/upload', methods=['POST'])
def upload_files():
    """Upload and process multiple Spotify JSON files"""
    
    # Check if files were uploaded
    if 'files[]' not in request.files:
        return jsonify({'error': 'No files provided'}), 400
    
    files = request.files.getlist('files[]')
    
    if not files or files[0].filename == '':
        return jsonify({'error': 'No files selected'}), 400
        
    # Process files
    dataframes = []
    
    for file in files:
        # Ensure it's a JSON file
        if not file.filename.endswith('.json'):
            continue
            
        # Read JSON file
        try:
            df = pd.read_json(file)
            dataframes.append(df)
        except Exception as e:
            return jsonify({'error': f'Error processing file {file.filename}: {str(e)}'}), 400
    
    if not dataframes:
        return jsonify({'error': 'No valid JSON files were processed'}), 400
    
    # Combine DataFrames
    combined_df = pd.concat(dataframes, ignore_index=True)
    
    # Create a unique ID for this user's data
    session_id = str(uuid.uuid4())
    
    # Store the DataFrame in memory (would store in DB in production)
    user_data[session_id] = combined_df
    
    # Return basic stats about the data
    return jsonify({
        'session_id': session_id,
        'total_records': len(combined_df),
        'unique_artists': combined_df['master_metadata_album_artist_name'].nunique() if 'master_metadata_album_artist_name' in combined_df.columns else 0,
        'unique_tracks': combined_df['master_metadata_track_name'].nunique() if 'master_metadata_track_name' in combined_df.columns else 0
    })

@app.route('/basic_stats/<session_id>', methods=['GET'])
def basic_stats(session_id):
    """Get basic statistics about the user's data"""
    
    # Check if session exists
    if session_id not in user_data:
        return jsonify({'error': 'Session not found'}), 404
        
    df = user_data[session_id]
    
    # Simple stats (similar to the first analysis parts of the notebook)
    stats = {
        'total_records': len(df),
        'data_columns': list(df.columns)
    }
    
    # Add artist stats if the column exists
    if 'master_metadata_album_artist_name' in df.columns:
        stats['unique_artists'] = df['master_metadata_album_artist_name'].nunique()
        
    # Add track stats if the column exists
    if 'master_metadata_track_name' in df.columns:
        stats['unique_tracks'] = df['master_metadata_track_name'].nunique()
    
    return jsonify(stats)

# Register our top_artists routes
top_artists.register_routes(app, user_data)