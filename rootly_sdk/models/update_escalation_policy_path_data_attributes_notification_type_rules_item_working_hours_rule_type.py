from typing import Literal

UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemWorkingHoursRuleType = Literal["working_hour"]

UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_WORKING_HOURS_RULE_TYPE_VALUES: set[
    UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemWorkingHoursRuleType
] = {
    "working_hour",
}


def check_update_escalation_policy_path_data_attributes_notification_type_rules_item_working_hours_rule_type(
    value: str | None,
) -> UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemWorkingHoursRuleType | None:
    if value is None:
        return None
    if (
        value
        in UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_WORKING_HOURS_RULE_TYPE_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_WORKING_HOURS_RULE_TYPE_VALUES!r}"
    )
