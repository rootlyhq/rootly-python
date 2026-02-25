from typing import Literal, cast

UpdateEscalationPolicyDataAttributesBusinessHoursType0DaysType0Item = Literal["F", "M", "R", "S", "T", "U", "W"]

UPDATE_ESCALATION_POLICY_DATA_ATTRIBUTES_BUSINESS_HOURS_TYPE_0_DAYS_TYPE_0_ITEM_VALUES: set[
    UpdateEscalationPolicyDataAttributesBusinessHoursType0DaysType0Item
] = {
    "F",
    "M",
    "R",
    "S",
    "T",
    "U",
    "W",
}


def check_update_escalation_policy_data_attributes_business_hours_type_0_days_type_0_item(
    value: str | None,
) -> UpdateEscalationPolicyDataAttributesBusinessHoursType0DaysType0Item | None:
    if value is None:
        return None
    if value in UPDATE_ESCALATION_POLICY_DATA_ATTRIBUTES_BUSINESS_HOURS_TYPE_0_DAYS_TYPE_0_ITEM_VALUES:
        return cast(UpdateEscalationPolicyDataAttributesBusinessHoursType0DaysType0Item, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ESCALATION_POLICY_DATA_ATTRIBUTES_BUSINESS_HOURS_TYPE_0_DAYS_TYPE_0_ITEM_VALUES!r}"
    )
