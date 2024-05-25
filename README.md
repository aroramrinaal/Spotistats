# Spotistats

Spotistats is a data analysis and visualization project based on personal Spotify streaming history. Spotify is one of the most famous and popular music streaming platforms. This project aims to explore and analyze the user's Spotify usage to gain useful insights into their listening habits.

In this project, we will explore various aspects of Spotify usage data, including:
- The list of songs played
- The list of artists of the songs
- The duration of usage and more

The dataset used here showcases the personal usage of Spotify, downloaded from Spotify's Privacy Setting section, which allows anyone to download their personal usage data.

<img width="809" alt="Screenshot 2024-05-22 at 10 26 29" src="https://github.com/aroramrinaal/Spotistats/assets/90490253/75eef9ea-a147-49f7-b0f4-b74ca50ef0d2">

For this Exploratory Data Analysis (EDA) project, we will utilize several tools and libraries:
- **Jupyter Notebook**: An open-source web application that allows you to create and share documents that contain live code, equations, visualizations, and narrative text.
- **Python**: A powerful programming language known for its readability and vast library support.
- **Libraries**:
  - `numpy`: A library for numerical computations.
  - `pandas`: A powerful data manipulation and analysis library.
  - `matplotlib`: A plotting library for creating static, animated, and interactive visualizations.
  - `seaborn`: A statistical data visualization library based on matplotlib.
  - `wordcloud`: A library for generating word clouds from text.

## Contents of the .zip File

When you download your Spotify extended streaming history, you will receive a .zip file. After extracting the .zip file, the folder structure will look like this:

<img width="783" alt="Screenshot 2024-05-17 at 06 59 13" src="https://github.com/aroramrinaal/Spotistats/assets/90490253/a85d5e44-e9ff-4893-a535-c52058233632">

## Top 10 Favorite Artists

In this project, we analyze and visualize the top 10 favorite artists based on listening time (hours) and the number of times songs were played (count).

### Visualization of Top 10 Favorite Artists by Listening Time (Hours)

```python
# Group by artist name and calculate the sum of listening time and counts
top_artists_df = spotify_stream_df.groupby("master_metadata_album_artist_name")[["Listening Time (Hours)", "Count"]].sum()

# Sort artists by Listening Time (Hours) and select the top 10
top_10_artists_hours = top_artists_df.sort_values(by="Listening Time (Hours)", ascending=False).head(10)

# Visualization of top 10 unique artists by listening time (hours)
plt.figure(figsize=(12, 8))
sns.barplot(x=top_10_artists_hours.index, y=top_10_artists_hours["Listening Time (Hours)"], palette='viridis')
plt.xlabel('Artists')
plt.ylabel('No. of Hours Songs Played')
plt.title('My Top 10 Favourite Artist (based on Hours)')
plt.xticks(rotation=45, ha='right')
plt.show()
```
![output](https://github.com/aroramrinaal/Spotistats/assets/90490253/751484f1-8ebb-45ed-8012-ec0822b972c5)

### Visualization of Top 10 Favorite Artists by Listening Count

```python
# Top 10 artists by Count
top_10_artists_count = top_artists_df.sort_values(by="Count", ascending=False).head(10)

# Visualization of top 10 unique artists by play count
plt.figure(figsize=(10, 5))
sns.barplot(x=top_10_artists_count.index, y=top_10_artists_count["Count"], palette='magma')
plt.xlabel('Artists')
plt.ylabel('No. of Times Songs Played')
plt.title('My Top 10 Favourite Artist (based on Counts)')
plt.xticks(rotation=45, ha='right')
plt.show()
```
![output](https://github.com/aroramrinaal/Spotistats/assets/90490253/8bfbbe18-4703-4935-bdf6-423fb0885464)

## Percentage of Unique Tracks

In this project, we analyze the percentage of unique tracks in the listening history and visualize it using a pie chart.

### Visualization of Unique Tracks Percentage

```python
# Calculate the number of unique tracks
unique_tracks = spotify_stream_df["master_metadata_track_name"].nunique()

# Calculating the total number of track entries
total_tracks = spotify_stream_df["master_metadata_track_name"].count()

# Calculate the percentage of unique tracks
unique_tracks_percentage = (unique_tracks / total_tracks) * 100

# Prepare data for the pie chart
unique_tracks_list = np.array([unique_tracks, total_tracks - unique_tracks])
unique_tracks_list_labels = ["Unique Tracks", "Non Unique Tracks"]

# Create a pie chart
fig, ax = plt.subplots(figsize=(12, 6))
ax.pie(unique_tracks_list, labels=unique_tracks_list_labels, autopct='%1.1f%%', explode=[0.05, 0.05], startangle=180, shadow=True)
plt.title("Unique Tracks Percentage")
plt.show()

# Print the calculated percentages for reference
print(f"Number of unique tracks: {unique_tracks}")
print(f"Total number of track entries: {total_tracks}")
print(f"Percentage of unique tracks: {unique_tracks_percentage:.2f}%")
```
![5114962f-031d-46b3-ade1-5080e609aed5](https://github.com/aroramrinaal/Spotistats/assets/90490253/2deeeea6-59e9-4b49-ad16-2e695d8449e0)

## Day Wise Percentage of Spotify Streaming

In this project, we analyze the distribution of Spotify streaming activity across different days of the week and visualize it using a pie chart.

### Visualization of Day Wise Percentage of Spotify Streaming

```python
fig, ax = plt.subplots(figsize=(12, 6))
ax.pie(spotify_stream_df["day-name"].value_counts(), labels=spotify_stream_df["day-name"].value_counts().index, autopct='%1.1f%%', startangle=180, shadow=True)
ax.set(title="Day wise % of Spotify Streaming")
plt.show()
```
![3515fe61-a713-4a95-b79b-f0543643be2f](https://github.com/aroramrinaal/Spotistats/assets/90490253/b99d87a3-9594-47a1-9a9b-89de13db8667)

## Average Usage Over a Day

In this project, we analyze the distribution of Spotify streaming activity over the hours of a day and visualize it using a histogram with a kernel density estimate (KDE).

### Visualization of Average Distribution of Streaming Over Day Hours

```python
# Average Usage over a day
fig, ax = plt.subplots(figsize=(12,8))
ax.set(title="Average Distribution of Streaming Over Day Hours", xlabel="Hours (in 24 hour format)", ylabel="Songs Played")
sns.histplot(spotify_stream_df["hours"], bins=24, kde=True, color="darkgreen")
plt.show()
```
![97a4b2fb-5254-4559-be90-25d065ba7e54](https://github.com/aroramrinaal/Spotistats/assets/90490253/7c31fe2b-5de7-4abe-aadf-b6f7979f973e)

## Top 100 Favorite Artists

In this project, we generate a word cloud to visualize the top 100 favorite artists based on the number of times their songs were played.

### Visualization of Top 100 Favorite Artists

```python
# Sort artists by Count
top_artists_df = top_artists_df.sort_values(by='Count', ascending=False)

# Select the top 100 artists
top_100_artists = top_artists_df.head(100)

# Generate the word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(top_100_artists['Count'])

# Display the word cloud
plt.figure(figsize=(14, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Top 100 Favorite Artists')
plt.show()
```
![edcf03df-1f5b-43e8-83ea-2ae145d74023](https://github.com/aroramrinaal/Spotistats/assets/90490253/05853e3b-79f4-4041-9cb0-96d52b1b877c)

## Active Usage in a Day Over a Week

In this project, we analyze the active usage of Spotify over different hours of the day throughout the week and visualize it using a heatmap.

### Visualization of Active Usage in a Day Over a Week

```python
# Extract day of the week and hour from 'Play-Time'
spotify_stream_df['day_of_week'] = spotify_stream_df['Play-Time'].dt.day_name()
spotify_stream_df['hour'] = spotify_stream_df['Play-Time'].dt.hour

# Aggregate data by day of the week and hour
usage_by_day_hour = spotify_stream_df.groupby(['day_of_week', 'hour']).size().unstack(fill_value=0)

# Reorder the days of the week
days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
usage_by_day_hour = usage_by_day_hour.reindex(days_order)

# Create a heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(usage_by_day_hour, cmap='Blues', annot=True, fmt='d', cbar_kws={'label': 'Number of Songs Played'})
plt.title('Spotify Usage (Active Usage in a Day Over a Week)')
plt.xlabel('Hour of Day')
plt.ylabel('Day of Week')
plt.show()
```
![203d4346-7dbf-4134-a961-30272869c7ed](https://github.com/aroramrinaal/Spotistats/assets/90490253/f873f1ae-d860-4c85-98eb-fe8c7cc1139d)

## Number of Songs Played Each Day

In this project, we analyze the number of songs played each day and visualize it using a scatter plot.

### Visualization of Number of Songs Played Each Day

```python
# Aggregate data by date
songs_per_day = spotify_stream_df.groupby(spotify_stream_df['Play-Time'].dt.date)['Count'].sum().reset_index()
songs_per_day.columns = ['Date', 'Number of Songs Played']

# Identify the day with maximum songs played
max_songs_day = songs_per_day[songs_per_day['Number of Songs Played'] == songs_per_day['Number of Songs Played'].max()]

print(f"The day with the maximum number of songs played is: {max_songs_day['Date'].values[0]} with {max_songs_day['Number of Songs Played'].values[0]} songs.")

# Plot a scatter plot to show all the dates
plt.figure(figsize=(12, 7))
sns.scatterplot(data=songs_per_day, x='Date', y='Number of Songs Played', hue='Number of Songs Played', palette='viridis', legend=None)
plt.title('Number of Songs Played Each Day')
plt.xlabel('Date')
plt.ylabel('Number of Songs Played')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
```
![f57e95e6-b85a-425e-944e-91c325683d58](https://github.com/aroramrinaal/Spotistats/assets/90490253/13c57a4b-06e8-4576-95b6-c98bea1f0dc9)
