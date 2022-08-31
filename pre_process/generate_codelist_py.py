import json

with open("match_report.json", "r") as f:
    match_report = json.load(f)

codelists = [v["files"] for v in match_report.values()]
codelists = [a for b in codelists for a in b]
codelists = list(set(codelists))


def codelist_name(path):
    return path.replace('codelists/', '')\
        .replace('.csv', '')\
        .replace('-', '_')


def new_codelist_path(path):
    return path.replace('.csv', '_new.csv')


def codelist_from_csv(path):
    with open(path, 'r') as cf:
        line = cf.readline()
    idcol = [c for c in line.split(',') if 'id' in c and c != 'vpid'][0]
    return f"""codelist_from_csv(
        '{path}',
        system='snomed',
        column='{idcol}'
        )"""


with open("analysis/codelists.py", "w") as f:
    f.write("from cohortextractor import codelist_from_csv\n")
    f.write("dict_codelists = {\n")
    for c in codelists:
        f.write(f"'{codelist_name(c)}': {codelist_from_csv(c)},\n")
        n = new_codelist_path(c)
        f.write(f"'{codelist_name(n)}': {codelist_from_csv(n)},\n")
    f.write("}\n")
