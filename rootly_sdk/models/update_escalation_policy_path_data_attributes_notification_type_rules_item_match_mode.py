from typing import Literal

UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemMatchMode = Literal[
    "match-all-rules", "match-any-rule"
]

UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_MATCH_MODE_VALUES: set[
    UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemMatchMode
] = {
    "match-all-rules",
    "match-any-rule",
}


def check_update_escalation_policy_path_data_attributes_notification_type_rules_item_match_mode(
    value: str | None,
) -> UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemMatchMode | None:
    if value is None:
        return None
    if value in UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_MATCH_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_MATCH_MODE_VALUES!r}"
    )
