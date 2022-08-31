from cohortextractor import StudyDefinition, patients
from codelists import dict_codelists

med_vars = {
    k: patients.with_these_medications(
        v,
        between=["index_date", "index_date + 1 year"],
        returning="number_of_matches_in_period",
    )
    for k, v in dict_codelists.items()
}

study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "1900-01-01", "latest": "today"},
        "rate": "uniform",
        "incidence": 0.5,
        "int": {"distribution": "normal", "mean": 2, "stddev": 1},
    },
    index_date="2019-01-01",
    population=patients.all(),
    **med_vars
)
