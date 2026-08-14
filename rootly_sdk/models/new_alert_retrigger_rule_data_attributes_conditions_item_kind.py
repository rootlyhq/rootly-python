from typing import Literal, cast

NewAlertRetriggerRuleDataAttributesConditionsItemKind = Literal[
    "alert_field", "group", "payload", "service", "source", "urgency"
]

NEW_ALERT_RETRIGGER_RULE_DATA_ATTRIBUTES_CONDITIONS_ITEM_KIND_VALUES: set[
    NewAlertRetriggerRuleDataAttributesConditionsItemKind
] = {
    "alert_field",
    "group",
    "payload",
    "service",
    "source",
    "urgency",
}


def check_new_alert_retrigger_rule_data_attributes_conditions_item_kind(
    value: str | None,
) -> NewAlertRetriggerRuleDataAttributesConditionsItemKind | None:
    if value is None:
        return None
    if value in NEW_ALERT_RETRIGGER_RULE_DATA_ATTRIBUTES_CONDITIONS_ITEM_KIND_VALUES:
        return cast(NewAlertRetriggerRuleDataAttributesConditionsItemKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ALERT_RETRIGGER_RULE_DATA_ATTRIBUTES_CONDITIONS_ITEM_KIND_VALUES!r}"
    )
