from typing import Literal

NewEscalationPolicyPathDataAttributesRetriggerTimeoutMinutes = Literal[
    -1, 10, 20, 30, 40, 50, 60, 90, 120, 180, 240, 300, 360, 720, 1440
]

NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RETRIGGER_TIMEOUT_MINUTES_VALUES: set[
    NewEscalationPolicyPathDataAttributesRetriggerTimeoutMinutes
] = {
    -1,
    10,
    20,
    30,
    40,
    50,
    60,
    90,
    120,
    180,
    240,
    300,
    360,
    720,
    1440,
}


def check_new_escalation_policy_path_data_attributes_retrigger_timeout_minutes(
    value: int,
) -> NewEscalationPolicyPathDataAttributesRetriggerTimeoutMinutes:
    if value in NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RETRIGGER_TIMEOUT_MINUTES_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RETRIGGER_TIMEOUT_MINUTES_VALUES!r}"
    )
