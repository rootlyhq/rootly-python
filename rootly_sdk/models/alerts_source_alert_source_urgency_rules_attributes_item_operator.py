from typing import Literal, cast

AlertsSourceAlertSourceUrgencyRulesAttributesItemOperator = Literal["contains", "does_not_contain", "is", "is_not"]

ALERTS_SOURCE_ALERT_SOURCE_URGENCY_RULES_ATTRIBUTES_ITEM_OPERATOR_VALUES: set[
    AlertsSourceAlertSourceUrgencyRulesAttributesItemOperator
] = {
    "contains",
    "does_not_contain",
    "is",
    "is_not",
}


def check_alerts_source_alert_source_urgency_rules_attributes_item_operator(
    value: str | None,
) -> AlertsSourceAlertSourceUrgencyRulesAttributesItemOperator | None:
    if value is None:
        return None
    if value in ALERTS_SOURCE_ALERT_SOURCE_URGENCY_RULES_ATTRIBUTES_ITEM_OPERATOR_VALUES:
        return cast(AlertsSourceAlertSourceUrgencyRulesAttributesItemOperator, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERTS_SOURCE_ALERT_SOURCE_URGENCY_RULES_ATTRIBUTES_ITEM_OPERATOR_VALUES!r}"
    )
