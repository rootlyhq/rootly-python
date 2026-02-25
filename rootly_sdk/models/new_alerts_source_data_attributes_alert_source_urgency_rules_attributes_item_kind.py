from typing import Literal, cast

NewAlertsSourceDataAttributesAlertSourceUrgencyRulesAttributesItemKind = Literal["alert_field", "payload"]

NEW_ALERTS_SOURCE_DATA_ATTRIBUTES_ALERT_SOURCE_URGENCY_RULES_ATTRIBUTES_ITEM_KIND_VALUES: set[
    NewAlertsSourceDataAttributesAlertSourceUrgencyRulesAttributesItemKind
] = {
    "alert_field",
    "payload",
}


def check_new_alerts_source_data_attributes_alert_source_urgency_rules_attributes_item_kind(
    value: str | None,
) -> NewAlertsSourceDataAttributesAlertSourceUrgencyRulesAttributesItemKind | None:
    if value is None:
        return None
    if value in NEW_ALERTS_SOURCE_DATA_ATTRIBUTES_ALERT_SOURCE_URGENCY_RULES_ATTRIBUTES_ITEM_KIND_VALUES:
        return cast(NewAlertsSourceDataAttributesAlertSourceUrgencyRulesAttributesItemKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ALERTS_SOURCE_DATA_ATTRIBUTES_ALERT_SOURCE_URGENCY_RULES_ATTRIBUTES_ITEM_KIND_VALUES!r}"
    )
