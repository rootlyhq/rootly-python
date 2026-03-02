from typing import Literal, cast

UpdateAlertsSourceDataAttributesAlertSourceUrgencyRulesAttributesItemConditionableType = Literal["AlertField"]

UPDATE_ALERTS_SOURCE_DATA_ATTRIBUTES_ALERT_SOURCE_URGENCY_RULES_ATTRIBUTES_ITEM_CONDITIONABLE_TYPE_VALUES: set[
    UpdateAlertsSourceDataAttributesAlertSourceUrgencyRulesAttributesItemConditionableType
] = {
    "AlertField",
}


def check_update_alerts_source_data_attributes_alert_source_urgency_rules_attributes_item_conditionable_type(
    value: str | None,
) -> UpdateAlertsSourceDataAttributesAlertSourceUrgencyRulesAttributesItemConditionableType | None:
    if value is None:
        return None
    if (
        value
        in UPDATE_ALERTS_SOURCE_DATA_ATTRIBUTES_ALERT_SOURCE_URGENCY_RULES_ATTRIBUTES_ITEM_CONDITIONABLE_TYPE_VALUES
    ):
        return cast(UpdateAlertsSourceDataAttributesAlertSourceUrgencyRulesAttributesItemConditionableType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ALERTS_SOURCE_DATA_ATTRIBUTES_ALERT_SOURCE_URGENCY_RULES_ATTRIBUTES_ITEM_CONDITIONABLE_TYPE_VALUES!r}"
    )
