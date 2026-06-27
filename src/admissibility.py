from models import HealthcareCase, EvaluationResult


def evaluate(case: HealthcareCase) -> EvaluationResult:

    violations = []

    if case.states.get("patient_identity_state") != "continuous":
        violations.append("patient_identity_state")

    if case.states.get("consent_state") != "valid":
        violations.append("consent_state")

    if case.states.get("temporal_state") != "valid":
        violations.append("temporal_state")

    if case.states.get("dependency_state") != "satisfied":
        violations.append("dependency_state")

    if case.states.get("resource_state") != "available":
        violations.append("resource_state")

    if case.states.get("policy_state") != "valid":
        violations.append("policy_state")

    if case.states.get("verification_state") != "reconstructable":
        violations.append("verification_state")

    if case.states.get("integrity_state") != "preserved":
        violations.append("integrity_state")

    authority = case.states.get("authority_state")

    if authority not in (None, "valid", "authorized"):
        violations.append("authority_state")

    result = "BLOCKED" if violations else "EXECUTED"

    return EvaluationResult(
        case_id=case.case_id,
        category=case.category,
        title=case.title,
        result=result,
        failure_prevented=(result == case.expected_result),
        violations=violations,
    )
