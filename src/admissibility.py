from models import HealthcareCase, EvaluationResult


VALID_STATES = {
    "authorized",
    "pending",
    "valid",
    "continuous",
    "preserved",
    "available",
    "satisfied",
    "reconstructable"
}


def evaluate(case: HealthcareCase) -> EvaluationResult:

    violations = []

    for state, value in case.states.items():
        if value not in VALID_STATES:
            violations.append(state)

    result = "BLOCKED" if violations else "EXECUTED"

    return EvaluationResult(
        case_id=case.case_id,
        category=case.category,
        title=case.title,
        result=result,
        failure_prevented=(result == case.expected_result),
        violations=violations,
    )
