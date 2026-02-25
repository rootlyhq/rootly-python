from typing import Literal, cast

AlertsSourceAlertSourceUrgencyRulesAttributesItemConditionableType = Literal["AlertField"]

ALERTS_SOURCE_ALERT_SOURCE_URGENCY_RULES_ATTRIBUTES_ITEM_CONDITIONABLE_TYPE_VALUES: set[
    AlertsSourceAlertSourceUrgencyRulesAttributesItemConditionableType
] = {
    "AlertField",
}


def check_alerts_source_alert_source_urgency_rules_attributes_item_conditionable_type(
    value: str | None,
) -> AlertsSourceAlertSourceUrgencyRulesAttributesItemConditionableType | None:
    if value is None:
        return None
    if value in ALERTS_SOURCE_ALERT_SOURCE_URGENCY_RULES_ATTRIBUTES_ITEM_CONDITIONABLE_TYPE_VALUES:
        return cast(AlertsSourceAlertSourceUrgencyRulesAttributesItemConditionableType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERTS_SOURCE_ALERT_SOURCE_URGENCY_RULES_ATTRIBUTES_ITEM_CONDITIONABLE_TYPE_VALUES!r}"
    )
