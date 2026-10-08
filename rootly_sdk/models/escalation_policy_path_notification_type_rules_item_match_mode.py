from typing import Literal

EscalationPolicyPathNotificationTypeRulesItemMatchMode = Literal["match-all-rules", "match-any-rule"]

ESCALATION_POLICY_PATH_NOTIFICATION_TYPE_RULES_ITEM_MATCH_MODE_VALUES: set[
    EscalationPolicyPathNotificationTypeRulesItemMatchMode
] = {
    "match-all-rules",
    "match-any-rule",
}


def check_escalation_policy_path_notification_type_rules_item_match_mode(
    value: str | None,
) -> EscalationPolicyPathNotificationTypeRulesItemMatchMode | None:
    if value is None:
        return None
    if value in ESCALATION_POLICY_PATH_NOTIFICATION_TYPE_RULES_ITEM_MATCH_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ESCALATION_POLICY_PATH_NOTIFICATION_TYPE_RULES_ITEM_MATCH_MODE_VALUES!r}"
    )
