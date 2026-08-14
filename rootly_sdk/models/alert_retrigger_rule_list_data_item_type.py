from typing import Literal, cast

AlertRetriggerRuleListDataItemType = Literal["alert_retrigger_rules"]

ALERT_RETRIGGER_RULE_LIST_DATA_ITEM_TYPE_VALUES: set[AlertRetriggerRuleListDataItemType] = {
    "alert_retrigger_rules",
}


def check_alert_retrigger_rule_list_data_item_type(value: str | None) -> AlertRetriggerRuleListDataItemType | None:
    if value is None:
        return None
    if value in ALERT_RETRIGGER_RULE_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(AlertRetriggerRuleListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_RETRIGGER_RULE_LIST_DATA_ITEM_TYPE_VALUES!r}")
