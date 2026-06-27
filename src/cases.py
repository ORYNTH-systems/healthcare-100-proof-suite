import json
from pathlib import Path

from models import HealthcareCase


def load_case(case_id: str) -> HealthcareCase:
    path = Path("cases") / f"{case_id}.json"

    if not path.exists():
        raise FileNotFoundError(f"Case file not found: {path}")

    data = json.loads(path.read_text())

    states = {
        key: value
        for key, value in data.items()
        if key.endswith("_state")
    }

    return HealthcareCase(
        case_id=data["case_id"],
        category=data["category"],
        title=data["title"],
        clinical_action=data["clinical_action"],
        states=states,
        expected_result=data["expected_result"],
        expected_violation=data["expected_violation"],
    )
