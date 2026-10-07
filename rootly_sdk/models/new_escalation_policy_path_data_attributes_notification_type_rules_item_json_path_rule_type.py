from typing import Literal

NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemJSONPathRuleType = Literal["json_path"]

NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_JSON_PATH_RULE_TYPE_VALUES: set[
    NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemJSONPathRuleType
] = {
    "json_path",
}


def check_new_escalation_policy_path_data_attributes_notification_type_rules_item_json_path_rule_type(
    value: str | None,
) -> NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemJSONPathRuleType | None:
    if value is None:
        return None
    if value in NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_JSON_PATH_RULE_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_JSON_PATH_RULE_TYPE_VALUES!r}"
    )
