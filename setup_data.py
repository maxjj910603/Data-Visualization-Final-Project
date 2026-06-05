"""
Space Graph – Data Setup Script
--------------------------------
Checks for the raw dataset and runs the cleaning pipeline.

Usage:
    python setup_data.py
"""

import os
import sys
import subprocess

RAW_FILE   = os.path.join("data", "steam_game_data.csv")
CLEAN_FILE = os.path.join("data", "steam_game_data_clean.csv")
CLEAN_SCRIPT = "clean_data.py"


def check_raw_data():
    if not os.path.exists(RAW_FILE):
        print("=" * 60)
        print("  Raw dataset not found.")
        print("=" * 60)
        print()
        print("  Please obtain the file:")
        print("    steam_game_data.csv")
        print()
        print("  Source: Steam Web API + SteamSpy estimates")
        print()
        print("  Place it in the data/ folder:")
        print(f"    {RAW_FILE}")
        print()
        print("  Then run this script again.")
        print("=" * 60)
        sys.exit(1)
    print(f"[OK] Raw data found: {RAW_FILE}")


def run_cleaning():
    if not os.path.exists(CLEAN_SCRIPT):
        print(f"[ERROR] Cleaning script not found: {CLEAN_SCRIPT}")
        sys.exit(1)

    if os.path.exists(CLEAN_FILE):
        print(f"[SKIP] Clean data already exists: {CLEAN_FILE}")
        print("       Delete it and re-run to regenerate.")
        return

    print(f"[RUN] Running {CLEAN_SCRIPT} ...")
    result = subprocess.run([sys.executable, CLEAN_SCRIPT], capture_output=True, text=True)

    if result.returncode != 0:
        print("[ERROR] Cleaning script failed:")
        print(result.stderr)
        sys.exit(1)

    print(result.stdout.strip())
    print(f"[OK] Clean data ready: {CLEAN_FILE}")


def main():
    print()
    print("  Space Graph – Data Setup")
    print()

    os.makedirs("data", exist_ok=True)
    check_raw_data()
    run_cleaning()

    print()
    print("  Setup complete.")
    print("  Start a local server and open index.html to launch Space Graph.")
    print()
    print("  Example:")
    print("    python -m http.server 8080")
    print("    → http://localhost:8080")
    print()


if __name__ == "__main__":
    main()