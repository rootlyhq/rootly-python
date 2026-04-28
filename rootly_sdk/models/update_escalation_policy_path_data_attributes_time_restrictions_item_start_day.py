from typing import Literal, cast

UpdateEscalationPolicyPathDataAttributesTimeRestrictionsItemStartDay = Literal[
    "friday", "monday", "saturday", "sunday", "thursday", "tuesday", "wednesday"
]

UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_TIME_RESTRICTIONS_ITEM_START_DAY_VALUES: set[
    UpdateEscalationPolicyPathDataAttributesTimeRestrictionsItemStartDay
] = {
    "friday",
    "monday",
    "saturday",
    "sunday",
    "thursday",
    "tuesday",
    "wednesday",
}


def check_update_escalation_policy_path_data_attributes_time_restrictions_item_start_day(
    value: str | None,
) -> UpdateEscalationPolicyPathDataAttributesTimeRestrictionsItemStartDay | None:
    if value is None:
        return None
    if value in UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_TIME_RESTRICTIONS_ITEM_START_DAY_VALUES:
        return cast(UpdateEscalationPolicyPathDataAttributesTimeRestrictionsItemStartDay, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_TIME_RESTRICTIONS_ITEM_START_DAY_VALUES!r}"
    )
