from typing import Literal, cast

NewEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0Type = Literal[
    "schedule", "service", "slack_channel", "team", "user"
]

NEW_ESCALATION_POLICY_LEVEL_DATA_ATTRIBUTES_NOTIFICATION_TARGET_PARAMS_ITEM_TYPE_0_TYPE_VALUES: set[
    NewEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0Type
] = {
    "schedule",
    "service",
    "slack_channel",
    "team",
    "user",
}


def check_new_escalation_policy_level_data_attributes_notification_target_params_item_type_0_type(
    value: str | None,
) -> NewEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0Type | None:
    if value is None:
        return None
    if value in NEW_ESCALATION_POLICY_LEVEL_DATA_ATTRIBUTES_NOTIFICATION_TARGET_PARAMS_ITEM_TYPE_0_TYPE_VALUES:
        return cast(NewEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0Type, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ESCALATION_POLICY_LEVEL_DATA_ATTRIBUTES_NOTIFICATION_TARGET_PARAMS_ITEM_TYPE_0_TYPE_VALUES!r}"
    )
