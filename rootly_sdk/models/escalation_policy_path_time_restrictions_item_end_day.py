from typing import Literal, cast

EscalationPolicyPathTimeRestrictionsItemEndDay = Literal[
    "friday", "monday", "saturday", "sunday", "thursday", "tuesday", "wednesday"
]

ESCALATION_POLICY_PATH_TIME_RESTRICTIONS_ITEM_END_DAY_VALUES: set[EscalationPolicyPathTimeRestrictionsItemEndDay] = {
    "friday",
    "monday",
    "saturday",
    "sunday",
    "thursday",
    "tuesday",
    "wednesday",
}


def check_escalation_policy_path_time_restrictions_item_end_day(
    value: str | None,
) -> EscalationPolicyPathTimeRestrictionsItemEndDay | None:
    if value is None:
        return None
    if value in ESCALATION_POLICY_PATH_TIME_RESTRICTIONS_ITEM_END_DAY_VALUES:
        return cast(EscalationPolicyPathTimeRestrictionsItemEndDay, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ESCALATION_POLICY_PATH_TIME_RESTRICTIONS_ITEM_END_DAY_VALUES!r}"
    )
