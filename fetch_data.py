"""
Space Graph – Dataset Download Script
--------------------------------------
Downloads the Steam Games Dataset from Kaggle and prepares it
for use with Space Graph.

Dataset: https://www.kaggle.com/datasets/fronkongames/steam-games-dataset

Requirements
------------
1. Install the Kaggle CLI:
     pip install kaggle

2. Set up your Kaggle API key:
   a. Go to https://www.kaggle.com/settings → "API" → "Create New Token"
   b. A file named kaggle.json will be downloaded.
   c. Place it at:
        Windows : C:\\Users\\<username>\\.kaggle\\kaggle.json
        macOS   : ~/.kaggle/kaggle.json
        Linux   : ~/.kaggle/kaggle.json

Usage
-----
    python fetch_data.py

What this script does
---------------------
1. Downloads the dataset from Kaggle
2. Renames the file to steam_game_data.csv
3. Runs clean_data.py to generate steam_game_data_clean.csv
"""

import os
import sys
import subprocess
import shutil

DATASET     = "fronkongames/steam-games-dataset"
DATA_DIR    = "data"
RAW_NAME    = "games.csv"                            # filename inside the Kaggle zip
TARGET_NAME = "steam_game_data.csv"                  # filename expected by the project
RAW_PATH    = os.path.join(DATA_DIR, RAW_NAME)
TARGET_PATH = os.path.join(DATA_DIR, TARGET_NAME)
CLEAN_SCRIPT = "clean_data.py"


def check_kaggle_cli():
    """Return True if the kaggle command is available."""
    try:
        r = subprocess.run(["kaggle", "--version"],
                           capture_output=True, text=True)
        return r.returncode == 0
    except FileNotFoundError:
        return False


def check_kaggle_key():
    """Return True if kaggle.json exists in the expected location."""
    home = os.path.expanduser("~")
    key_path = os.path.join(home, ".kaggle", "kaggle.json")
    return os.path.isfile(key_path)


def download_dataset():
    """Download and unzip the Kaggle dataset into DATA_DIR."""
    print(f"[DOWNLOAD] {DATASET}")
    os.makedirs(DATA_DIR, exist_ok=True)

    result = subprocess.run(
        ["kaggle", "datasets", "download",
         "-d", DATASET,
         "--path", DATA_DIR,
         "--unzip"],
        text=True
    )

    if result.returncode != 0:
        print("[ERROR] Kaggle download failed.")
        sys.exit(1)

    print("[OK] Download complete.")


def rename_file():
    """Rename games.csv → steam_game_data.csv if needed."""
    if os.path.isfile(TARGET_PATH):
        print(f"[SKIP] {TARGET_NAME} already exists.")
        return

    if os.path.isfile(RAW_PATH):
        shutil.move(RAW_PATH, TARGET_PATH)
        print(f"[OK] Renamed {RAW_NAME} → {TARGET_NAME}")
    else:
        # Try to find any CSV in data/ in case the filename changed
        csvs = [f for f in os.listdir(DATA_DIR) if f.endswith(".csv")]
        if len(csvs) == 1:
            shutil.move(os.path.join(DATA_DIR, csvs[0]), TARGET_PATH)
            print(f"[OK] Renamed {csvs[0]} → {TARGET_NAME}")
        else:
            print("[ERROR] Could not locate the downloaded CSV.")
            print(f"        Files in {DATA_DIR}/: {csvs}")
            sys.exit(1)


def run_cleaning():
    """Run clean_data.py to produce steam_game_data_clean.csv."""
    if not os.path.isfile(CLEAN_SCRIPT):
        print(f"[ERROR] {CLEAN_SCRIPT} not found.")
        sys.exit(1)

    clean_path = os.path.join(DATA_DIR, "steam_game_data_clean.csv")
    if os.path.isfile(clean_path):
        print(f"[SKIP] steam_game_data_clean.csv already exists.")
        return

    print(f"[RUN] {CLEAN_SCRIPT}")
    result = subprocess.run([sys.executable, CLEAN_SCRIPT], text=True)
    if result.returncode != 0:
        print("[ERROR] Cleaning script failed.")
        sys.exit(1)
    print("[OK] Clean data ready.")


def print_setup_guide():
    print()
    print("  Kaggle CLI is not set up. Follow these steps:")
    print()
    print("  1. Install the Kaggle CLI:")
    print("       pip install kaggle")
    print()
    print("  2. Get your API key:")
    print("       https://www.kaggle.com/settings → API → Create New Token")
    print()
    print("  3. Place kaggle.json at:")
    print("       Windows : C:\\Users\\<username>\\.kaggle\\kaggle.json")
    print("       macOS   : ~/.kaggle/kaggle.json")
    print("       Linux   : ~/.kaggle/kaggle.json")
    print()
    print("  4. Re-run this script.")
    print()
    print("  Alternatively, download manually from:")
    print("  https://www.kaggle.com/datasets/fronkongames/steam-games-dataset")
    print("  and place the CSV as:  data/steam_game_data.csv")
    print("  Then run:  python clean_data.py")
    print()


def main():
    print()
    print("  Space Graph – Dataset Download")
    print()

    if not check_kaggle_cli():
        print("[ERROR] Kaggle CLI not found.")
        print_setup_guide()
        sys.exit(1)

    if not check_kaggle_key():
        print("[ERROR] kaggle.json not found.")
        print_setup_guide()
        sys.exit(1)

    if os.path.isfile(TARGET_PATH):
        print(f"[SKIP] {TARGET_NAME} already exists. Skipping download.")
    else:
        download_dataset()
        rename_file()

    run_cleaning()

    print()
    print("  Done! Start a local server and open index.html.")
    print()
    print("    python -m http.server 8080")
    print("    → http://localhost:8080")
    print()


if __name__ == "__main__":
    main()