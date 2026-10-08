from typing import Literal

UpdateEscalationPolicyLevelDataAttributesPagingStrategyConfigurationRotationScope = Literal[
    "active_rotation", "entire_schedule"
]

UPDATE_ESCALATION_POLICY_LEVEL_DATA_ATTRIBUTES_PAGING_STRATEGY_CONFIGURATION_ROTATION_SCOPE_VALUES: set[
    UpdateEscalationPolicyLevelDataAttributesPagingStrategyConfigurationRotationScope
] = {
    "active_rotation",
    "entire_schedule",
}


def check_update_escalation_policy_level_data_attributes_paging_strategy_configuration_rotation_scope(
    value: str | None,
) -> UpdateEscalationPolicyLevelDataAttributesPagingStrategyConfigurationRotationScope | None:
    if value is None:
        return None
    if value in UPDATE_ESCALATION_POLICY_LEVEL_DATA_ATTRIBUTES_PAGING_STRATEGY_CONFIGURATION_ROTATION_SCOPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ESCALATION_POLICY_LEVEL_DATA_ATTRIBUTES_PAGING_STRATEGY_CONFIGURATION_ROTATION_SCOPE_VALUES!r}"
    )
