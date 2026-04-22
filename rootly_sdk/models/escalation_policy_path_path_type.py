from typing import Literal, cast

EscalationPolicyPathPathType = Literal["deferral", "escalation"]

ESCALATION_POLICY_PATH_PATH_TYPE_VALUES: set[EscalationPolicyPathPathType] = {
    "deferral",
    "escalation",
}


def check_escalation_policy_path_path_type(value: str | None) -> EscalationPolicyPathPathType | None:
    if value is None:
        return None
    if value in ESCALATION_POLICY_PATH_PATH_TYPE_VALUES:
        return cast(EscalationPolicyPathPathType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ESCALATION_POLICY_PATH_PATH_TYPE_VALUES!r}")
