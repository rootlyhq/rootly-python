from typing import Literal, cast

NewAlertsSourceDataAttributesAlertSourceUrgencyRulesAttributesItemOperator = Literal[
    "contains", "does_not_contain", "is", "is_not"
]

NEW_ALERTS_SOURCE_DATA_ATTRIBUTES_ALERT_SOURCE_URGENCY_RULES_ATTRIBUTES_ITEM_OPERATOR_VALUES: set[
    NewAlertsSourceDataAttributesAlertSourceUrgencyRulesAttributesItemOperator
] = {
    "contains",
    "does_not_contain",
    "is",
    "is_not",
}


def check_new_alerts_source_data_attributes_alert_source_urgency_rules_attributes_item_operator(
    value: str | None,
) -> NewAlertsSourceDataAttributesAlertSourceUrgencyRulesAttributesItemOperator | None:
    if value is None:
        return None
    if value in NEW_ALERTS_SOURCE_DATA_ATTRIBUTES_ALERT_SOURCE_URGENCY_RULES_ATTRIBUTES_ITEM_OPERATOR_VALUES:
        return cast(NewAlertsSourceDataAttributesAlertSourceUrgencyRulesAttributesItemOperator, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ALERTS_SOURCE_DATA_ATTRIBUTES_ALERT_SOURCE_URGENCY_RULES_ATTRIBUTES_ITEM_OPERATOR_VALUES!r}"
    )
