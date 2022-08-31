import pandas as pd

for year in range(2019, 2023):
    df = pd.read_csv(f"output/input_{year}-01-01.csv.gz")
    df[[c for c in df.columns if c != "patient_id"]].sum().reset_index().rename(
        columns={"index": "codelist", 0: "count"}
    ).to_csv(f'output/counts_{year}.csv', index=None)
