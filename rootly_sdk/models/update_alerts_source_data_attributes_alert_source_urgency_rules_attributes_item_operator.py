from typing import Literal, cast

UpdateAlertsSourceDataAttributesAlertSourceUrgencyRulesAttributesItemOperator = Literal[
    "contains", "does_not_contain", "is", "is_not"
]

UPDATE_ALERTS_SOURCE_DATA_ATTRIBUTES_ALERT_SOURCE_URGENCY_RULES_ATTRIBUTES_ITEM_OPERATOR_VALUES: set[
    UpdateAlertsSourceDataAttributesAlertSourceUrgencyRulesAttributesItemOperator
] = {
    "contains",
    "does_not_contain",
    "is",
    "is_not",
}


def check_update_alerts_source_data_attributes_alert_source_urgency_rules_attributes_item_operator(
    value: str | None,
) -> UpdateAlertsSourceDataAttributesAlertSourceUrgencyRulesAttributesItemOperator | None:
    if value is None:
        return None
    if value in UPDATE_ALERTS_SOURCE_DATA_ATTRIBUTES_ALERT_SOURCE_URGENCY_RULES_ATTRIBUTES_ITEM_OPERATOR_VALUES:
        return cast(UpdateAlertsSourceDataAttributesAlertSourceUrgencyRulesAttributesItemOperator, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ALERTS_SOURCE_DATA_ATTRIBUTES_ALERT_SOURCE_URGENCY_RULES_ATTRIBUTES_ITEM_OPERATOR_VALUES!r}"
    )
