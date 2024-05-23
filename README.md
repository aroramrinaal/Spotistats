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
