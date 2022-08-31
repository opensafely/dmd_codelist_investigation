import re
import json
import pandas as pd
from ripgrepy import Ripgrepy

DEFAULTS = {"project_id": "ebmdatalab", "dialect": "standard"}

SQL = """
SELECT
    id,
    nm,
    vpiddt,
    vpidprev,
    bnf_code
  FROM
    `ebmdatalab.dmd.vmp_full`
  WHERE
    vpidprev IS NOT NULL
"""

df_changed_vmps = pd.read_gbq(SQL, **DEFAULTS)
changed_vmp_files = {}
for id, old_vpid in df_changed_vmps[["id", "vpidprev"]].values:
    rg = (
        Ripgrepy(f"[^0-9]{old_vpid}[^0-9]", "codelists")
        .glob("*.csv")
        .json()
        .run()
        .as_dict
    )
    if rg:
        changed_vmp_files[(id, old_vpid)] = {
            "matches": len(rg),
            "files": list(set([m["data"]["path"]["text"] for m in rg])),
        }

with open("match_report.json", "w") as f:
    json.dump({f"{k[0]}->{k[1]}": v for k, v in changed_vmp_files.items()}, f)

for ids, changes in changed_vmp_files.items():
    id, old_vpid = ids
    for file in changes["files"]:
        new_file = "local_"+file.replace(".csv", "_new.csv")
        with open(file, "r") as of, open(new_file, "w") as nf:
            nf.write(
                re.sub(rf"(?<![0-9]){old_vpid}(?![0-9])", f"{id}", of.read())
            )
