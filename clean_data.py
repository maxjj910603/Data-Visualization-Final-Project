import pandas as pd
import os

INPUT_FILE = "steam_game_data.csv"
OUTPUT_FILE = "steam_game_data_clean.csv"

# 篩選條件：Estimated owners 下界 >= 20,000
OWNER_THRESHOLD = 20000


def parse_owners_lower(s):
    """解析 'X - Y' 格式的 Estimated owners，取下界數值"""
    try:
        return int(str(s).split(" - ")[0].replace(",", "").strip())
    except Exception:
        return 0


def main():
    input_path = os.path.join("data", INPUT_FILE)
    output_path = os.path.join("data", OUTPUT_FILE)

    if not os.path.exists(input_path):
        print(f"[ERROR] 找不到輸入檔案：{input_path}")
        print("請確認 steam_game_data.csv 已放在 data/ 資料夾內")
        return

    print(f"讀取 {input_path} ...")
    df = pd.read_csv(input_path)
    print(f"原始資料：{len(df):,} 筆，{len(df.columns)} 個欄位")

    # 計算 owners 下界，用於篩選（不寫入輸出）
    owners_lower = df["Estimated owners"].apply(parse_owners_lower)
    df_clean = df[owners_lower >= OWNER_THRESHOLD].copy()

    print(f"篩選後資料：{len(df_clean):,} 筆（Estimated owners 下界 >= {OWNER_THRESHOLD:,}）")

    df_clean.to_csv(output_path, index=False)
    print(f"已輸出至：{output_path}")


if __name__ == "__main__":
    main()