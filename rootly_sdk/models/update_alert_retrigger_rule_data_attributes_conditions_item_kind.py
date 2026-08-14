from typing import Literal, cast

UpdateAlertRetriggerRuleDataAttributesConditionsItemKind = Literal[
    "alert_field", "group", "payload", "service", "source", "urgency"
]

UPDATE_ALERT_RETRIGGER_RULE_DATA_ATTRIBUTES_CONDITIONS_ITEM_KIND_VALUES: set[
    UpdateAlertRetriggerRuleDataAttributesConditionsItemKind
] = {
    "alert_field",
    "group",
    "payload",
    "service",
    "source",
    "urgency",
}


def check_update_alert_retrigger_rule_data_attributes_conditions_item_kind(
    value: str | None,
) -> UpdateAlertRetriggerRuleDataAttributesConditionsItemKind | None:
    if value is None:
        return None
    if value in UPDATE_ALERT_RETRIGGER_RULE_DATA_ATTRIBUTES_CONDITIONS_ITEM_KIND_VALUES:
        return cast(UpdateAlertRetriggerRuleDataAttributesConditionsItemKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ALERT_RETRIGGER_RULE_DATA_ATTRIBUTES_CONDITIONS_ITEM_KIND_VALUES!r}"
    )
