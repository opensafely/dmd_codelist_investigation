# For each codelist in the codelists directory, replace any obsolete VMP codes and
# create a new codelist in local_codelists.
#
# VMP codes come from running the following in BigQuery:
#
#   SELECT id, vpiddt, vpidprev, nm FROM ebmdatalab.dmd.vmp WHERE vpidprev IS NOT NULL
#
# and saving the results to vmps.csv.

import csv
import glob

with open("vmps.csv") as f:
    old_to_new = {r["vpidprev"]: r["id"] for r in csv.DictReader(f)}


for path in glob.glob("codelists/*.csv"):
    with open(path) as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    has_old_codes = False

    for r in rows:
        for header in ["vpid", "dmd_id", "id", "code"]:
            if header in r:
                break
        else:
            assert False, r.keys()

        if r[header] in old_to_new:
            has_old_codes = True
            r[header] = old_to_new[r[header]]

    if not has_old_codes:
        continue

    new_path = "local_" + path.replace(".csv", "_new.csv")

    with open(new_path, "w") as f:
        writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(rows)
