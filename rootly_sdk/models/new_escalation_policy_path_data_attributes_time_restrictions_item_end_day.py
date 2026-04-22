from typing import Literal, cast

NewEscalationPolicyPathDataAttributesTimeRestrictionsItemEndDay = Literal[
    "friday", "monday", "saturday", "sunday", "thursday", "tuesday", "wednesday"
]

NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_TIME_RESTRICTIONS_ITEM_END_DAY_VALUES: set[
    NewEscalationPolicyPathDataAttributesTimeRestrictionsItemEndDay
] = {
    "friday",
    "monday",
    "saturday",
    "sunday",
    "thursday",
    "tuesday",
    "wednesday",
}


def check_new_escalation_policy_path_data_attributes_time_restrictions_item_end_day(
    value: str | None,
) -> NewEscalationPolicyPathDataAttributesTimeRestrictionsItemEndDay | None:
    if value is None:
        return None
    if value in NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_TIME_RESTRICTIONS_ITEM_END_DAY_VALUES:
        return cast(NewEscalationPolicyPathDataAttributesTimeRestrictionsItemEndDay, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_TIME_RESTRICTIONS_ITEM_END_DAY_VALUES!r}"
    )
