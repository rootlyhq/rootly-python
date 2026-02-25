from typing import Literal, cast

EscalationPolicyLevelPagingStrategyConfigurationScheduleStrategy = Literal["everyone", "on_call_only"]

ESCALATION_POLICY_LEVEL_PAGING_STRATEGY_CONFIGURATION_SCHEDULE_STRATEGY_VALUES: set[
    EscalationPolicyLevelPagingStrategyConfigurationScheduleStrategy
] = {
    "everyone",
    "on_call_only",
}


def check_escalation_policy_level_paging_strategy_configuration_schedule_strategy(
    value: str | None,
) -> EscalationPolicyLevelPagingStrategyConfigurationScheduleStrategy | None:
    if value is None:
        return None
    if value in ESCALATION_POLICY_LEVEL_PAGING_STRATEGY_CONFIGURATION_SCHEDULE_STRATEGY_VALUES:
        return cast(EscalationPolicyLevelPagingStrategyConfigurationScheduleStrategy, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ESCALATION_POLICY_LEVEL_PAGING_STRATEGY_CONFIGURATION_SCHEDULE_STRATEGY_VALUES!r}"
    )
