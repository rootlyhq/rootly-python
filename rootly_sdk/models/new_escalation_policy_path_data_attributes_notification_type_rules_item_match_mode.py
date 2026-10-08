from typing import Literal

NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemMatchMode = Literal["match-all-rules", "match-any-rule"]

NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_MATCH_MODE_VALUES: set[
    NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemMatchMode
] = {
    "match-all-rules",
    "match-any-rule",
}


def check_new_escalation_policy_path_data_attributes_notification_type_rules_item_match_mode(
    value: str | None,
) -> NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemMatchMode | None:
    if value is None:
        return None
    if value in NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_MATCH_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_MATCH_MODE_VALUES!r}"
    )
