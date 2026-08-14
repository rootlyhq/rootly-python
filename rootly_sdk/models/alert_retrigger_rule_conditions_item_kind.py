from typing import Literal, cast

AlertRetriggerRuleConditionsItemKind = Literal["alert_field", "group", "payload", "service", "source", "urgency"]

ALERT_RETRIGGER_RULE_CONDITIONS_ITEM_KIND_VALUES: set[AlertRetriggerRuleConditionsItemKind] = {
    "alert_field",
    "group",
    "payload",
    "service",
    "source",
    "urgency",
}


def check_alert_retrigger_rule_conditions_item_kind(value: str | None) -> AlertRetriggerRuleConditionsItemKind | None:
    if value is None:
        return None
    if value in ALERT_RETRIGGER_RULE_CONDITIONS_ITEM_KIND_VALUES:
        return cast(AlertRetriggerRuleConditionsItemKind, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_RETRIGGER_RULE_CONDITIONS_ITEM_KIND_VALUES!r}")
