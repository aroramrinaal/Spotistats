# How to Run the Spotistats Project

## Prerequisites

- Python 3.9.6 (Current system version)
- Jupyter Notebook environment
- Required Python packages:
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - wordcloud

## Setup Steps

1. **Clone the repository or navigate to the project directory**
   ```bash
   cd /Users/mrinaalarora/Spotistats
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   ```

3. **Install required packages**
   ```bash
   pip3 install pandas numpy matplotlib seaborn wordcloud jupyter
   ```

## Running the Project

1. **Start Jupyter Notebook**
   ```bash
   python3 -m jupyter notebook
   ```

2. **Open the notebook**
   - In the Jupyter interface that opens in your browser, click on `spotistats.ipynb`

3. **Data Requirements**
   - The notebook expects Spotify streaming history data in the `/data` directory
   - If you need to process new data:
     - Place your Spotify Extended Streaming History JSON files in a directory
     - Update the `directory` variable in the second code cell to point to your data location
     - Run the second cell to process and combine the JSON files
     - The combined data will be saved as `spotify_data.json`

4. **Running the Notebook**
   - You can run the entire notebook by selecting "Kernel" > "Restart & Run All"
   - Or run individual cells by selecting them and pressing Shift+Enter

## Notes

- The notebook analyzes Spotify listening history data, creating visualizations of your most-played artists, tracks, and listening patterns
- If you encounter issues with the wordcloud package, you may need to install additional dependencies:
  ```bash
  pip3 install pillow
  ```
- Python 3.9.6 is confirmed to be compatible with this project
- Your system has both `python` (aliased to python3) and `python3` commands available
- Similarly, both `pip` and `pip3` commands should work, but it's recommended to use `pip3` to ensure you're using the Python 3 version
