from typing import Literal, cast

NewAlertRetriggerRuleDataAttributesMatchMode = Literal["match-all-rules", "match-any-rule"]

NEW_ALERT_RETRIGGER_RULE_DATA_ATTRIBUTES_MATCH_MODE_VALUES: set[NewAlertRetriggerRuleDataAttributesMatchMode] = {
    "match-all-rules",
    "match-any-rule",
}


def check_new_alert_retrigger_rule_data_attributes_match_mode(
    value: str | None,
) -> NewAlertRetriggerRuleDataAttributesMatchMode | None:
    if value is None:
        return None
    if value in NEW_ALERT_RETRIGGER_RULE_DATA_ATTRIBUTES_MATCH_MODE_VALUES:
        return cast(NewAlertRetriggerRuleDataAttributesMatchMode, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ALERT_RETRIGGER_RULE_DATA_ATTRIBUTES_MATCH_MODE_VALUES!r}"
    )
