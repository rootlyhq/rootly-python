from typing import Literal, cast

NewEscalationPolicyDataAttributesBusinessHoursType0DaysType0Item = Literal["F", "M", "R", "S", "T", "U", "W"]

NEW_ESCALATION_POLICY_DATA_ATTRIBUTES_BUSINESS_HOURS_TYPE_0_DAYS_TYPE_0_ITEM_VALUES: set[
    NewEscalationPolicyDataAttributesBusinessHoursType0DaysType0Item
] = {
    "F",
    "M",
    "R",
    "S",
    "T",
    "U",
    "W",
}


def check_new_escalation_policy_data_attributes_business_hours_type_0_days_type_0_item(
    value: str | None,
) -> NewEscalationPolicyDataAttributesBusinessHoursType0DaysType0Item | None:
    if value is None:
        return None
    if value in NEW_ESCALATION_POLICY_DATA_ATTRIBUTES_BUSINESS_HOURS_TYPE_0_DAYS_TYPE_0_ITEM_VALUES:
        return cast(NewEscalationPolicyDataAttributesBusinessHoursType0DaysType0Item, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ESCALATION_POLICY_DATA_ATTRIBUTES_BUSINESS_HOURS_TYPE_0_DAYS_TYPE_0_ITEM_VALUES!r}"
    )
