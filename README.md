# 🌌 Space Graph
### Steam Game Data Visualization
**Data Visualization – Spring 2026 | Team 2**

> An interactive star map where every star is a Steam game.

---

## Team Members
| Name |
|------|
| 方敬棠 |
| 戴廣琛 |
| 李晉豪 |

---

## Overview

Space Graph visualizes the Steam game dataset as an interactive star map. Each star represents a single game, with its position, size, and color encoding different data dimensions:

| Visual Element | Data Dimension |
|----------------|---------------|
| Radial distance from center | Price |
| Star size | Popularity (positive review count) |
| Star color | Primary genre |
| Star angle | User-selectable attribute |

---

## Features

- **Radial Scale Switching** – Toggle between Linear, Square Root, and Logarithmic scales for radial distance
- **Angle Attribute Selector** – Map angular position to any numeric attribute (Release Date, Metacritic Score, Playtime, etc.)
- **Dynamic Guide Line** – Hover over the chart to see a guide line indicating the value at that angle
- **Hover Tooltip** – Hover over any star to see detailed game metadata
- **Click to Pan** – Click any star to pan the view to center it
- **Scroll to Zoom** – Zoom in/out with the mouse wheel
- **Genre & Size Legend** – Sidebar legend for color and size encoding
- **Filters** – Filter by Genre, Price, Release Year, Peak CCU, Metacritic Score, Positive/Negative Reviews, and Recommendations

---

## Getting Started

### Requirements
- A modern web browser (Chrome or Firefox recommended)
- Python 3 (for data preprocessing only)
- A local HTTP server (see options below)

### Data Setup

The dataset is not included due to file size. Follow these steps:

**1. Obtain the raw data file:**
```
steam_game_data.csv
```
Source: Steam Web API + SteamSpy estimates

**2. Place it in the `data/` folder:**
```
data/steam_game_data.csv
```

**3. Run the cleaning script:**
```bash
python clean_data.py
```
This generates `data/steam_game_data_clean.csv` (games with Estimated owners ≥ 20,000 — about 16,900 games).

### Running the Visualization

> `index.html` cannot be opened directly via `file://` — a local HTTP server is required.

**Option A – VS Code Live Server**
Right-click `index.html` → *Open with Live Server*

**Option B – Python**
```bash
python -m http.server 8080
# Open http://localhost:8080
```

**Option C – Node.js**
```bash
npx serve .
```

---

## Tech Stack

- **[D3.js v7](https://d3js.org/)** – All visualizations (loaded via CDN)
- HTML / CSS / Vanilla JavaScript

---

## Data Source

**Steam Games Dataset** by fronkongames on Kaggle
🔗 https://www.kaggle.com/datasets/fronkongames/steam-games-dataset

The dataset combines:
- **Steam Web API** — game metadata, pricing, reviews, playtime
- **SteamSpy API** — Estimated owners field

### Automated Download (recommended)

```bash
pip install kaggle
# Place your kaggle.json at ~/.kaggle/kaggle.json
# (get it from https://www.kaggle.com/settings → API → Create New Token)

python fetch_data.py
```

### Manual Download

1. Download from the Kaggle link above
2. Rename to `steam_game_data.csv` and place in `data/`
3. Run `python clean_data.py`