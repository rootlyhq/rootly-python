from typing import Literal, cast

UpdateEscalationPolicyPathDataAttributesTimeRestrictionsItemEndDay = Literal[
    "friday", "monday", "saturday", "sunday", "thursday", "tuesday", "wednesday"
]

UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_TIME_RESTRICTIONS_ITEM_END_DAY_VALUES: set[
    UpdateEscalationPolicyPathDataAttributesTimeRestrictionsItemEndDay
] = {
    "friday",
    "monday",
    "saturday",
    "sunday",
    "thursday",
    "tuesday",
    "wednesday",
}


def check_update_escalation_policy_path_data_attributes_time_restrictions_item_end_day(
    value: str | None,
) -> UpdateEscalationPolicyPathDataAttributesTimeRestrictionsItemEndDay | None:
    if value is None:
        return None
    if value in UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_TIME_RESTRICTIONS_ITEM_END_DAY_VALUES:
        return cast(UpdateEscalationPolicyPathDataAttributesTimeRestrictionsItemEndDay, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_TIME_RESTRICTIONS_ITEM_END_DAY_VALUES!r}"
    )
