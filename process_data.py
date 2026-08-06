import pandas as pd
import glob

files = glob.glob("data/daily_sales_data_*.csv")

all_dfs = []

for file in files:
    df = pd.read_csv(file)
    df = df[df["product"].str.lower() == "pink morsel"]
    df["price"] = df["price"].replace(r"[\$,]", "", regex=True).astype(float)
    df["Sales"] = df["price"] * df["quantity"]
    df = df.rename(columns={"date": "Date", "region": "Region"})
    df = df[["Sales", "Date", "Region"]]
    all_dfs.append(df)

final_df = pd.concat(all_dfs, ignore_index=True)
final_df.to_csv("output.csv", index=False)

print("Done! output.csv created with", len(final_df), "rows.")
print(final_df.head())