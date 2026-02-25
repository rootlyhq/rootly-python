from typing import Literal, cast

AlertRoutingRuleListDataItemType = Literal["alert_routing_rules"]

ALERT_ROUTING_RULE_LIST_DATA_ITEM_TYPE_VALUES: set[AlertRoutingRuleListDataItemType] = {
    "alert_routing_rules",
}


def check_alert_routing_rule_list_data_item_type(value: str | None) -> AlertRoutingRuleListDataItemType | None:
    if value is None:
        return None
    if value in ALERT_ROUTING_RULE_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(AlertRoutingRuleListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_ROUTING_RULE_LIST_DATA_ITEM_TYPE_VALUES!r}")
