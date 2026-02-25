from typing import Literal, cast

NewEscalationPolicyLevelDataAttributesPagingStrategyConfigurationStrategy = Literal[
    "alert", "cycle", "default", "random"
]

NEW_ESCALATION_POLICY_LEVEL_DATA_ATTRIBUTES_PAGING_STRATEGY_CONFIGURATION_STRATEGY_VALUES: set[
    NewEscalationPolicyLevelDataAttributesPagingStrategyConfigurationStrategy
] = {
    "alert",
    "cycle",
    "default",
    "random",
}


def check_new_escalation_policy_level_data_attributes_paging_strategy_configuration_strategy(
    value: str | None,
) -> NewEscalationPolicyLevelDataAttributesPagingStrategyConfigurationStrategy | None:
    if value is None:
        return None
    if value in NEW_ESCALATION_POLICY_LEVEL_DATA_ATTRIBUTES_PAGING_STRATEGY_CONFIGURATION_STRATEGY_VALUES:
        return cast(NewEscalationPolicyLevelDataAttributesPagingStrategyConfigurationStrategy, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ESCALATION_POLICY_LEVEL_DATA_ATTRIBUTES_PAGING_STRATEGY_CONFIGURATION_STRATEGY_VALUES!r}"
    )
