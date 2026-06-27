from collections import Counter


def generate_metrics(results):

    counter = Counter(r.result for r in results)

    prevented = sum(r.failure_prevented for r in results)

    print()
    print("Healthcare 100-Proof Suite")
    print("--------------------------")
    print(f"Total Demonstrations : {len(results)}")
    print(f"Prevented Failures   : {prevented}")
    print(f"Executions           : {counter['EXECUTED']}")
    print(f"Blocked              : {counter['BLOCKED']}")
