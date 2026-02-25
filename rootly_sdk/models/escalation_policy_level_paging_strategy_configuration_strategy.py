from typing import Literal, cast

EscalationPolicyLevelPagingStrategyConfigurationStrategy = Literal["alert", "cycle", "default", "random"]

ESCALATION_POLICY_LEVEL_PAGING_STRATEGY_CONFIGURATION_STRATEGY_VALUES: set[
    EscalationPolicyLevelPagingStrategyConfigurationStrategy
] = {
    "alert",
    "cycle",
    "default",
    "random",
}


def check_escalation_policy_level_paging_strategy_configuration_strategy(
    value: str | None,
) -> EscalationPolicyLevelPagingStrategyConfigurationStrategy | None:
    if value is None:
        return None
    if value in ESCALATION_POLICY_LEVEL_PAGING_STRATEGY_CONFIGURATION_STRATEGY_VALUES:
        return cast(EscalationPolicyLevelPagingStrategyConfigurationStrategy, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ESCALATION_POLICY_LEVEL_PAGING_STRATEGY_CONFIGURATION_STRATEGY_VALUES!r}"
    )
