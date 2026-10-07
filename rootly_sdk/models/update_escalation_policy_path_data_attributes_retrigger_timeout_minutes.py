from typing import Literal

UpdateEscalationPolicyPathDataAttributesRetriggerTimeoutMinutes = Literal[
    -1, 10, 20, 30, 40, 50, 60, 90, 120, 180, 240, 300, 360, 720, 1440
]

UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RETRIGGER_TIMEOUT_MINUTES_VALUES: set[
    UpdateEscalationPolicyPathDataAttributesRetriggerTimeoutMinutes
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


def check_update_escalation_policy_path_data_attributes_retrigger_timeout_minutes(
    value: int,
) -> UpdateEscalationPolicyPathDataAttributesRetriggerTimeoutMinutes:
    if value in UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RETRIGGER_TIMEOUT_MINUTES_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RETRIGGER_TIMEOUT_MINUTES_VALUES!r}"
    )
