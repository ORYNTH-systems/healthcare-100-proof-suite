import argparse

from admissibility import evaluate
from cases import load_case
from metrics import generate_metrics


def run_case(case_id):
    case = load_case(case_id)
    result = evaluate(case)

    print()
    print(f"Case ID   : {result.case_id}")
    print(f"Category  : {result.category}")
    print(f"Title     : {result.title}")
    print(f"Result    : {result.result}")
    print(f"Prevented : {result.failure_prevented}")
    print(f"Violations: {', '.join(result.violations) if result.violations else 'None'}")

    return result


def main():
    parser = argparse.ArgumentParser(
        description="Healthcare 100-Proof Suite Runtime"
    )

    parser.add_argument("--case", help="Run a single healthcare proof case")
    parser.add_argument("--all", action="store_true", help="Run all healthcare proof cases")

    args = parser.parse_args()

    if args.case:
        run_case(args.case)

    elif args.all:
        results = []
        for i in range(1, 21):
            case_id = f"HC-{i:03d}"
            results.append(run_case(case_id))

        generate_metrics(results)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
