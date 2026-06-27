from dataclasses import dataclass
from typing import Dict, List


@dataclass
class HealthcareCase:
    case_id: str
    category: str
    title: str
    clinical_action: str
    states: Dict[str, str]
    expected_result: str
    expected_violation: str


@dataclass
class EvaluationResult:
    case_id: str
    category: str
    title: str
    result: str
    failure_prevented: bool
    violations: List[str]
