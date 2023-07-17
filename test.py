from evaluation import evaluate
from language_models import process_query

test_set = [
    (
        "Does the Hiscox policy include waiver of subrogation?",
        "Yes, the policy includes waiver of subrogation",
    ),
    (
        "Does the Hiscox policy include blanket additional insured?",
        "Yes, but only applies to for any person or organization for whom you are performing operations or leasing premises",
    ),
    (
        "Does the Hiscox policy cover for primary and non-contributory?",
        "No, Primary and non-contributory is coverage not included in this Hiscox policy",
    ),
    (
        "Does the Hiscox policy cover the products-completed operations?",
        "Yes, products completed operations is included for certain coverages. It is not included for Medical Payments coverage.",
    ),
    (
        "What are the key coverages of the policy?",
        "(1) Bodily injury and property damage liability (2) personal and advertising injury liability (3) medical payments",
    ),
    (
        "What are the key exclusions for the medical payments coverage?",
        "(1) Any insured except voluntary workers (2) Hired person (3) Injury on normally occupied premises (4) if workers compensation could apply (5) for athletic activities (6) for productscompleted operations (7) for any exclusion covered under Coverage A",
    ),
]

if __name__ == "__main__":
    queries = [test[0] for test in test_set]
    predictions = [process_query(query) for query in queries]
    formatted_test_set = [{"question": test[0], "answer": test[1]} for test in test_set]
    formatted_predictions = [{"text": prediction} for prediction in predictions]
    print(evaluate(formatted_test_set, formatted_predictions))
