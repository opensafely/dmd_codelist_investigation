# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     notebook_metadata_filter: all,-language_info
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.3.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import csv
import glob
import os
import pandas as pd
import pyodbc

# +
dsn = os.environ['FULL_DATABASE_URL']
conn = pyodbc.connect(dsn)

sql = """
SELECT count(*)
FROM medicationissue mi
JOIN medicationdictionary md ON mi.multilexdrug_id = md.multilexdrug_id
WHERE mi.consultationdate >= '2019-01-01'
  AND md.dmd_id in ({})
"""

# +
counts = {"old": {}, "new": {}}

for path in glob.glob("../local_codelists/*.csv"):
    name = path.split("/")[-1][:-8]
    print(name)

    with open(f"../codelists/{name}.csv") as f:
        rows = list(csv.DictReader(f))

    for header in ["vpid", "dmd_id", "id", "code"]:
        if header in rows[0]:
            break
    else:
        assert False, rows[0].keys()
        
    old_codes = [r[header] for r in rows]

        
    with open(path) as f:
        rows = list(csv.DictReader(f))

    new_codes = [r[header] for r in rows]
    
    counts["old"][name] = list(conn.execute(sql.format(", ".join(old_codes))))[0][0]
    counts["new"][name] = list(conn.execute(sql.format(", ".join(new_codes))))[0][0]
# -

df = pd.DataFrame(counts)
df["delta"] = df["new"] - df["old"]
df["delta %"] = 100 * df["delta"] / df["old"]

df

print(df.to_markdown(floatfmt=".0f"))
