from typing import Literal, cast

UpdateAlertRetriggerRuleDataAttributesMatchMode = Literal["match-all-rules", "match-any-rule"]

UPDATE_ALERT_RETRIGGER_RULE_DATA_ATTRIBUTES_MATCH_MODE_VALUES: set[UpdateAlertRetriggerRuleDataAttributesMatchMode] = {
    "match-all-rules",
    "match-any-rule",
}


def check_update_alert_retrigger_rule_data_attributes_match_mode(
    value: str | None,
) -> UpdateAlertRetriggerRuleDataAttributesMatchMode | None:
    if value is None:
        return None
    if value in UPDATE_ALERT_RETRIGGER_RULE_DATA_ATTRIBUTES_MATCH_MODE_VALUES:
        return cast(UpdateAlertRetriggerRuleDataAttributesMatchMode, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ALERT_RETRIGGER_RULE_DATA_ATTRIBUTES_MATCH_MODE_VALUES!r}"
    )
