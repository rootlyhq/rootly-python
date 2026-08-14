from typing import Literal, cast

NewEscalationPolicyLevelDataAttributesPagingStrategyConfigurationRotationScope = Literal[
    "active_rotation", "entire_schedule"
]

NEW_ESCALATION_POLICY_LEVEL_DATA_ATTRIBUTES_PAGING_STRATEGY_CONFIGURATION_ROTATION_SCOPE_VALUES: set[
    NewEscalationPolicyLevelDataAttributesPagingStrategyConfigurationRotationScope
] = {
    "active_rotation",
    "entire_schedule",
}


def check_new_escalation_policy_level_data_attributes_paging_strategy_configuration_rotation_scope(
    value: str | None,
) -> NewEscalationPolicyLevelDataAttributesPagingStrategyConfigurationRotationScope | None:
    if value is None:
        return None
    if value in NEW_ESCALATION_POLICY_LEVEL_DATA_ATTRIBUTES_PAGING_STRATEGY_CONFIGURATION_ROTATION_SCOPE_VALUES:
        return cast(NewEscalationPolicyLevelDataAttributesPagingStrategyConfigurationRotationScope, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ESCALATION_POLICY_LEVEL_DATA_ATTRIBUTES_PAGING_STRATEGY_CONFIGURATION_ROTATION_SCOPE_VALUES!r}"
    )
