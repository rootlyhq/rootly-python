from typing import Literal, cast

UpdateAlertsSourceDataAttributesAlertSourceUrgencyRulesAttributesItemKind = Literal["alert_field", "payload"]

UPDATE_ALERTS_SOURCE_DATA_ATTRIBUTES_ALERT_SOURCE_URGENCY_RULES_ATTRIBUTES_ITEM_KIND_VALUES: set[
    UpdateAlertsSourceDataAttributesAlertSourceUrgencyRulesAttributesItemKind
] = {
    "alert_field",
    "payload",
}


def check_update_alerts_source_data_attributes_alert_source_urgency_rules_attributes_item_kind(
    value: str | None,
) -> UpdateAlertsSourceDataAttributesAlertSourceUrgencyRulesAttributesItemKind | None:
    if value is None:
        return None
    if value in UPDATE_ALERTS_SOURCE_DATA_ATTRIBUTES_ALERT_SOURCE_URGENCY_RULES_ATTRIBUTES_ITEM_KIND_VALUES:
        return cast(UpdateAlertsSourceDataAttributesAlertSourceUrgencyRulesAttributesItemKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ALERTS_SOURCE_DATA_ATTRIBUTES_ALERT_SOURCE_URGENCY_RULES_ATTRIBUTES_ITEM_KIND_VALUES!r}"
    )
