import pandas as pd
from sqlalchemy import create_engine
import sqlite3
import os

# === File Paths ===
BASE_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(BASE_DIR, "../data/us_house_Sales_data.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "../output")
DB_FILE = os.path.join(OUTPUT_DIR, "ushouse.db")
CSV_FILE = os.path.join(OUTPUT_DIR, "house_sales.csv")

# === Load and clean raw data ===
def load_data(path):
    print("Reading CSV...")
    df = pd.read_csv(path)

    df["Price"] = df["Price"].astype(str).str.replace(r"[$,]", "", regex=True).str.strip().astype(int)
    df["Bedrooms"] = df["Bedrooms"].str.extract(r"(\d+)").astype(int)
    df["Bathrooms"] = df["Bathrooms"].str.extract(r"(\d+)").astype(int)
    df["Area (Sqft)"] = df["Area (Sqft)"].str.replace("sqft", "", regex=False).str.strip().astype(int)
    df["Lot Size"] = df["Lot Size"].str.replace("sqft", "", regex=False).str.strip().astype(int)

    return df

# === Generate city-level stats ===
def generate_stats(df):
    city_avg = df.groupby(["City", "Property Type"])["Price"].mean().round().astype(int).reset_index()

    for_sale_df = df[df["Status"].str.strip().str.lower() == "for sale"]
    forsale_avg = for_sale_df.groupby(["City", "Property Type"])["Price"].mean().round().astype(int).reset_index()

    return city_avg, forsale_avg

# === Save data to SQLite DB ===
def save_to_db(df, city_avg, forsale_avg, db_path):
    print("Saving to SQLite database...")
    engine = create_engine(f"sqlite:///{db_path}")
    df.to_sql("house_sales", engine, if_exists="replace", index=False)
    city_avg.to_sql("city_avg_price", engine, if_exists="replace", index=False)
    forsale_avg.to_sql("forsale_avg_price", engine, if_exists="replace", index=False)
    engine.dispose()

# === Export cleaned data as CSV ===
def export_csv(df, path):
    df.to_csv(path, index=False)
    print(f"Exported cleaned data to {path}")

# === Test To Read DB ===
def check_db_tables(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Available tables in the database:")
    for name, in tables:
        print(f"- {name}")

    cursor.execute("SELECT * FROM forsale_avg_price LIMIT 5")
    columns = [col[0] for col in cursor.description]
    rows = cursor.fetchall()
    preview_df = pd.DataFrame(rows, columns=columns)
    print("\nPreview of 'forsale_avg_price':")
    print(preview_df)

    conn.close()

# === Main ETL ===
if __name__ == "__main__":
    try:
        df = load_data(DATA_FILE)
        city_avg, forsale_avg = generate_stats(df)
        save_to_db(df, city_avg, forsale_avg, DB_FILE)
        export_csv(df, CSV_FILE)
        check_db_tables(DB_FILE)
        print("ETL process finished.")
    except Exception as e:
        print(f"Error: {e}")