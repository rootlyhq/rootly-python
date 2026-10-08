from typing import Literal

UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemJSONPathRuleType = Literal["json_path"]

UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_JSON_PATH_RULE_TYPE_VALUES: set[
    UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemJSONPathRuleType
] = {
    "json_path",
}


def check_update_escalation_policy_path_data_attributes_notification_type_rules_item_json_path_rule_type(
    value: str | None,
) -> UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemJSONPathRuleType | None:
    if value is None:
        return None
    if value in UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_JSON_PATH_RULE_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_JSON_PATH_RULE_TYPE_VALUES!r}"
    )
