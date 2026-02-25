from typing import Literal, cast

EscalationPolicyBusinessHoursType0DaysType0Item = Literal["F", "M", "R", "S", "T", "U", "W"]

ESCALATION_POLICY_BUSINESS_HOURS_TYPE_0_DAYS_TYPE_0_ITEM_VALUES: set[
    EscalationPolicyBusinessHoursType0DaysType0Item
] = {
    "F",
    "M",
    "R",
    "S",
    "T",
    "U",
    "W",
}


def check_escalation_policy_business_hours_type_0_days_type_0_item(
    value: str | None,
) -> EscalationPolicyBusinessHoursType0DaysType0Item | None:
    if value is None:
        return None
    if value in ESCALATION_POLICY_BUSINESS_HOURS_TYPE_0_DAYS_TYPE_0_ITEM_VALUES:
        return cast(EscalationPolicyBusinessHoursType0DaysType0Item, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ESCALATION_POLICY_BUSINESS_HOURS_TYPE_0_DAYS_TYPE_0_ITEM_VALUES!r}"
    )
