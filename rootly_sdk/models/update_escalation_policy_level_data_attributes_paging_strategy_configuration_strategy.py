from typing import Literal, cast

UpdateEscalationPolicyLevelDataAttributesPagingStrategyConfigurationStrategy = Literal[
    "alert", "cycle", "default", "random"
]

UPDATE_ESCALATION_POLICY_LEVEL_DATA_ATTRIBUTES_PAGING_STRATEGY_CONFIGURATION_STRATEGY_VALUES: set[
    UpdateEscalationPolicyLevelDataAttributesPagingStrategyConfigurationStrategy
] = {
    "alert",
    "cycle",
    "default",
    "random",
}


def check_update_escalation_policy_level_data_attributes_paging_strategy_configuration_strategy(
    value: str | None,
) -> UpdateEscalationPolicyLevelDataAttributesPagingStrategyConfigurationStrategy | None:
    if value is None:
        return None
    if value in UPDATE_ESCALATION_POLICY_LEVEL_DATA_ATTRIBUTES_PAGING_STRATEGY_CONFIGURATION_STRATEGY_VALUES:
        return cast(UpdateEscalationPolicyLevelDataAttributesPagingStrategyConfigurationStrategy, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ESCALATION_POLICY_LEVEL_DATA_ATTRIBUTES_PAGING_STRATEGY_CONFIGURATION_STRATEGY_VALUES!r}"
    )
