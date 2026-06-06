import csv
import os

INPUT_FILE = "steam_game_data.csv"
OUTPUT_FILE = "steam_game_data_clean.csv"

# Keep games whose Estimated owners lower bound is at least 20,000.
OWNER_THRESHOLD = 20000


def parse_owners_lower(value):
    """Parse the lower bound from values like '20,000 - 50,000'."""
    try:
        lower_bound = str(value).split(" - ")[0].replace(",", "").strip()
        return int(lower_bound)
    except (TypeError, ValueError):
        return 0


def main():
    input_path = os.path.join("data", INPUT_FILE)
    output_path = os.path.join("data", OUTPUT_FILE)

    if not os.path.exists(input_path):
        print(f"[ERROR] Missing input file: {input_path}")
        print("Place steam_game_data.csv in the data/ folder and run again.")
        return

    print(f"Reading {input_path} ...")

    with open(input_path, "r", encoding="utf-8", newline="") as source:
        reader = csv.reader(source)
        raw_fieldnames = next(reader, None)

        if not raw_fieldnames or "Estimated owners" not in raw_fieldnames:
            print("[ERROR] Invalid CSV header: missing 'Estimated owners'.")
            return

        fieldnames = []
        for field in raw_fieldnames:
            if field == "DiscountDLC count":
                fieldnames.extend(["Discount", "DLC count"])
            else:
                fieldnames.append(field)

        total_rows = 0
        clean_rows = []

        for values in reader:
            total_rows += 1
            values = values[:len(fieldnames)] + [""] * max(0, len(fieldnames) - len(values))
            normalized_row = dict(zip(fieldnames, values))

            if parse_owners_lower(normalized_row["Estimated owners"]) >= OWNER_THRESHOLD:
                clean_rows.append(normalized_row)

    print(f"Original data: {total_rows:,} rows, {len(fieldnames)} columns")
    print(
        f"Filtered data: {len(clean_rows):,} rows "
        f"(Estimated owners lower bound >= {OWNER_THRESHOLD:,})"
    )

    with open(output_path, "w", encoding="utf-8", newline="") as target:
        writer = csv.DictWriter(target, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(clean_rows)

    print(f"Output written to: {output_path}")


if __name__ == "__main__":
    main()
