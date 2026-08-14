from typing import Literal, cast

EscalationPolicyLevelPagingStrategyConfigurationRepeatsMode = Literal["all", "users"]

ESCALATION_POLICY_LEVEL_PAGING_STRATEGY_CONFIGURATION_REPEATS_MODE_VALUES: set[
    EscalationPolicyLevelPagingStrategyConfigurationRepeatsMode
] = {
    "all",
    "users",
}


def check_escalation_policy_level_paging_strategy_configuration_repeats_mode(
    value: str | None,
) -> EscalationPolicyLevelPagingStrategyConfigurationRepeatsMode | None:
    if value is None:
        return None
    if value in ESCALATION_POLICY_LEVEL_PAGING_STRATEGY_CONFIGURATION_REPEATS_MODE_VALUES:
        return cast(EscalationPolicyLevelPagingStrategyConfigurationRepeatsMode, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ESCALATION_POLICY_LEVEL_PAGING_STRATEGY_CONFIGURATION_REPEATS_MODE_VALUES!r}"
    )
