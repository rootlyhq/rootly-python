from typing import Literal, cast

NewAlertsSourceDataAttributesAlertSourceUrgencyRulesAttributesItemConditionableType = Literal["AlertField"]

NEW_ALERTS_SOURCE_DATA_ATTRIBUTES_ALERT_SOURCE_URGENCY_RULES_ATTRIBUTES_ITEM_CONDITIONABLE_TYPE_VALUES: set[
    NewAlertsSourceDataAttributesAlertSourceUrgencyRulesAttributesItemConditionableType
] = {
    "AlertField",
}


def check_new_alerts_source_data_attributes_alert_source_urgency_rules_attributes_item_conditionable_type(
    value: str | None,
) -> NewAlertsSourceDataAttributesAlertSourceUrgencyRulesAttributesItemConditionableType | None:
    if value is None:
        return None
    if value in NEW_ALERTS_SOURCE_DATA_ATTRIBUTES_ALERT_SOURCE_URGENCY_RULES_ATTRIBUTES_ITEM_CONDITIONABLE_TYPE_VALUES:
        return cast(NewAlertsSourceDataAttributesAlertSourceUrgencyRulesAttributesItemConditionableType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ALERTS_SOURCE_DATA_ATTRIBUTES_ALERT_SOURCE_URGENCY_RULES_ATTRIBUTES_ITEM_CONDITIONABLE_TYPE_VALUES!r}"
    )
