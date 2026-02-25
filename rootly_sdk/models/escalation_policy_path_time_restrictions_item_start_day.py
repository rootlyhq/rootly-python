from typing import Literal, cast

EscalationPolicyPathTimeRestrictionsItemStartDay = Literal[
    "friday", "monday", "saturday", "sunday", "thursday", "tuesday", "wednesday"
]

ESCALATION_POLICY_PATH_TIME_RESTRICTIONS_ITEM_START_DAY_VALUES: set[
    EscalationPolicyPathTimeRestrictionsItemStartDay
] = {
    "friday",
    "monday",
    "saturday",
    "sunday",
    "thursday",
    "tuesday",
    "wednesday",
}


def check_escalation_policy_path_time_restrictions_item_start_day(
    value: str | None,
) -> EscalationPolicyPathTimeRestrictionsItemStartDay | None:
    if value is None:
        return None
    if value in ESCALATION_POLICY_PATH_TIME_RESTRICTIONS_ITEM_START_DAY_VALUES:
        return cast(EscalationPolicyPathTimeRestrictionsItemStartDay, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ESCALATION_POLICY_PATH_TIME_RESTRICTIONS_ITEM_START_DAY_VALUES!r}"
    )
