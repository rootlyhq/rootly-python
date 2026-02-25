from typing import Literal, cast

AlertsSourceAlertSourceUrgencyRulesAttributesItemKind = Literal["alert_field", "payload"]

ALERTS_SOURCE_ALERT_SOURCE_URGENCY_RULES_ATTRIBUTES_ITEM_KIND_VALUES: set[
    AlertsSourceAlertSourceUrgencyRulesAttributesItemKind
] = {
    "alert_field",
    "payload",
}


def check_alerts_source_alert_source_urgency_rules_attributes_item_kind(
    value: str | None,
) -> AlertsSourceAlertSourceUrgencyRulesAttributesItemKind | None:
    if value is None:
        return None
    if value in ALERTS_SOURCE_ALERT_SOURCE_URGENCY_RULES_ATTRIBUTES_ITEM_KIND_VALUES:
        return cast(AlertsSourceAlertSourceUrgencyRulesAttributesItemKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERTS_SOURCE_ALERT_SOURCE_URGENCY_RULES_ATTRIBUTES_ITEM_KIND_VALUES!r}"
    )
