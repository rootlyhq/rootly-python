from typing import Literal, cast

EscalationPolicyListDataItemType = Literal["escalation_policies"]

ESCALATION_POLICY_LIST_DATA_ITEM_TYPE_VALUES: set[EscalationPolicyListDataItemType] = {
    "escalation_policies",
}


def check_escalation_policy_list_data_item_type(value: str | None) -> EscalationPolicyListDataItemType | None:
    if value is None:
        return None
    if value in ESCALATION_POLICY_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(EscalationPolicyListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ESCALATION_POLICY_LIST_DATA_ITEM_TYPE_VALUES!r}")
