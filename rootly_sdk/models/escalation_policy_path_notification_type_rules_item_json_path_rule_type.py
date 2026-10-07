from typing import Literal

EscalationPolicyPathNotificationTypeRulesItemJSONPathRuleType = Literal["json_path"]

ESCALATION_POLICY_PATH_NOTIFICATION_TYPE_RULES_ITEM_JSON_PATH_RULE_TYPE_VALUES: set[
    EscalationPolicyPathNotificationTypeRulesItemJSONPathRuleType
] = {
    "json_path",
}


def check_escalation_policy_path_notification_type_rules_item_json_path_rule_type(
    value: str | None,
) -> EscalationPolicyPathNotificationTypeRulesItemJSONPathRuleType | None:
    if value is None:
        return None
    if value in ESCALATION_POLICY_PATH_NOTIFICATION_TYPE_RULES_ITEM_JSON_PATH_RULE_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ESCALATION_POLICY_PATH_NOTIFICATION_TYPE_RULES_ITEM_JSON_PATH_RULE_TYPE_VALUES!r}"
    )
