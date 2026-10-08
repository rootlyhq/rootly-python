from typing import Literal

NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemDeferralWindowRuleType = Literal["deferral_window"]

NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_DEFERRAL_WINDOW_RULE_TYPE_VALUES: set[
    NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemDeferralWindowRuleType
] = {
    "deferral_window",
}


def check_new_escalation_policy_path_data_attributes_notification_type_rules_item_deferral_window_rule_type(
    value: str | None,
) -> NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemDeferralWindowRuleType | None:
    if value is None:
        return None
    if (
        value
        in NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_DEFERRAL_WINDOW_RULE_TYPE_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_DEFERRAL_WINDOW_RULE_TYPE_VALUES!r}"
    )
