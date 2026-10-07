from typing import Literal

NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemWorkingHoursRuleType = Literal["working_hour"]

NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_WORKING_HOURS_RULE_TYPE_VALUES: set[
    NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemWorkingHoursRuleType
] = {
    "working_hour",
}


def check_new_escalation_policy_path_data_attributes_notification_type_rules_item_working_hours_rule_type(
    value: str | None,
) -> NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemWorkingHoursRuleType | None:
    if value is None:
        return None
    if value in NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_WORKING_HOURS_RULE_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_WORKING_HOURS_RULE_TYPE_VALUES!r}"
    )
