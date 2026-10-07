from typing import Literal

UpdateEscalationPolicyLevelDataAttributesPagingStrategyConfigurationRepeatsMode = Literal["all", "users"]

UPDATE_ESCALATION_POLICY_LEVEL_DATA_ATTRIBUTES_PAGING_STRATEGY_CONFIGURATION_REPEATS_MODE_VALUES: set[
    UpdateEscalationPolicyLevelDataAttributesPagingStrategyConfigurationRepeatsMode
] = {
    "all",
    "users",
}


def check_update_escalation_policy_level_data_attributes_paging_strategy_configuration_repeats_mode(
    value: str | None,
) -> UpdateEscalationPolicyLevelDataAttributesPagingStrategyConfigurationRepeatsMode | None:
    if value is None:
        return None
    if value in UPDATE_ESCALATION_POLICY_LEVEL_DATA_ATTRIBUTES_PAGING_STRATEGY_CONFIGURATION_REPEATS_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ESCALATION_POLICY_LEVEL_DATA_ATTRIBUTES_PAGING_STRATEGY_CONFIGURATION_REPEATS_MODE_VALUES!r}"
    )
