from pathlib import Path

import pandas as pd
import requests

response = requests.get("https://disease.sh/v3/covid-19/countries", timeout=15)
response.raise_for_status()
data = response.json()

table = pd.json_normalize(data, sep="_")
table = table[["country", "continent", "cases", "deaths", "recovered", "tests", "population", "active"]]
table = table.dropna(subset=["cases", "continent"])

out = Path(__file__).parent / "DATA" / "raw.csv"
out.parent.mkdir(exist_ok=True)
table.to_csv(out, index=False)
print(f"Saved {len(table)} rows to {out}")