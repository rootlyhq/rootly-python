from typing import Literal, cast

NewEscalationPolicyLevelDataAttributesPagingStrategyConfigurationRepeatsMode = Literal["all", "users"]

NEW_ESCALATION_POLICY_LEVEL_DATA_ATTRIBUTES_PAGING_STRATEGY_CONFIGURATION_REPEATS_MODE_VALUES: set[
    NewEscalationPolicyLevelDataAttributesPagingStrategyConfigurationRepeatsMode
] = {
    "all",
    "users",
}


def check_new_escalation_policy_level_data_attributes_paging_strategy_configuration_repeats_mode(
    value: str | None,
) -> NewEscalationPolicyLevelDataAttributesPagingStrategyConfigurationRepeatsMode | None:
    if value is None:
        return None
    if value in NEW_ESCALATION_POLICY_LEVEL_DATA_ATTRIBUTES_PAGING_STRATEGY_CONFIGURATION_REPEATS_MODE_VALUES:
        return cast(NewEscalationPolicyLevelDataAttributesPagingStrategyConfigurationRepeatsMode, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ESCALATION_POLICY_LEVEL_DATA_ATTRIBUTES_PAGING_STRATEGY_CONFIGURATION_REPEATS_MODE_VALUES!r}"
    )
