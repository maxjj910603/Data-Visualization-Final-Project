================================================================
Space Graph – Steam Game Data Visualization
Data Visualization, Spring 2026
Team 2
================================================================

Team Members
------------
  方敬棠
  戴廣琛
  李晉豪

----------------------------------------------------------------
System Overview
----------------------------------------------------------------
Space Graph is a web-based interactive visualization system that
presents Steam game data as a star map. Each star represents a
game, with its radial distance from the center encoding price,
star size encoding popularity (positive review count), and star
color encoding primary genre.

----------------------------------------------------------------
Requirements
----------------------------------------------------------------
No installation required. The system runs entirely in a modern
web browser (Chrome or Firefox recommended).

To serve the files locally, one of the following is needed:

  Option A – VS Code Live Server extension
    Right-click index.html → "Open with Live Server"

  Option B – Python (any version)
    python -m http.server 8080
    Then open http://localhost:8080 in your browser.

  Option C – Node.js
    npx serve .
    Then open the URL shown in the terminal.

Note: Opening index.html directly via file:// will NOT work
because d3.csv() requires an HTTP server.

----------------------------------------------------------------
Data Setup
----------------------------------------------------------------
The dataset is not included in this repository due to file size.

Data Source
  Steam Games Dataset by fronkongames on Kaggle
  https://www.kaggle.com/datasets/fronkongames/steam-games-dataset

  The dataset combines:
  (1) Steam Web API  – game metadata, pricing, reviews, playtime
  (2) SteamSpy API   – Estimated owners field

Option A – Automated download (recommended)

  Requires the Kaggle CLI:
    pip install kaggle

  Set up your Kaggle API key:
    1. Go to https://www.kaggle.com/settings → API → Create New Token
    2. Place the downloaded kaggle.json at:
         Windows : C:\Users\<username>\.kaggle\kaggle.json
         macOS   : ~/.kaggle/kaggle.json
         Linux   : ~/.kaggle/kaggle.json

  Then run:
    python fetch_data.py

  This will download, rename, and clean the data automatically.

Option B – Manual download

  1. Download from:
       https://www.kaggle.com/datasets/fronkongames/steam-games-dataset
  2. Rename the file to steam_game_data.csv and place it in data/:
       data/steam_game_data.csv
  3. Run the cleaning script:
       python clean_data.py

  This produces:
    data/steam_game_data_clean.csv
  (filtered to games with Estimated owners >= 20,000;
   approximately 16,900 games retained out of 106,457)

4. Start a local server (see Requirements above) and open
   index.html in your browser.

----------------------------------------------------------------
Starting Page
----------------------------------------------------------------
  index.html

----------------------------------------------------------------
Libraries Used
----------------------------------------------------------------
  D3.js v7  (loaded via CDN – no local installation needed)
    https://d3js.org/d3.v7.min.js

================================================================