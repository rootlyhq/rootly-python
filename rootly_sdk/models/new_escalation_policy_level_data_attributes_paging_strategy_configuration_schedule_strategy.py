from typing import Literal, cast

NewEscalationPolicyLevelDataAttributesPagingStrategyConfigurationScheduleStrategy = Literal["everyone", "on_call_only"]

NEW_ESCALATION_POLICY_LEVEL_DATA_ATTRIBUTES_PAGING_STRATEGY_CONFIGURATION_SCHEDULE_STRATEGY_VALUES: set[
    NewEscalationPolicyLevelDataAttributesPagingStrategyConfigurationScheduleStrategy
] = {
    "everyone",
    "on_call_only",
}


def check_new_escalation_policy_level_data_attributes_paging_strategy_configuration_schedule_strategy(
    value: str | None,
) -> NewEscalationPolicyLevelDataAttributesPagingStrategyConfigurationScheduleStrategy | None:
    if value is None:
        return None
    if value in NEW_ESCALATION_POLICY_LEVEL_DATA_ATTRIBUTES_PAGING_STRATEGY_CONFIGURATION_SCHEDULE_STRATEGY_VALUES:
        return cast(NewEscalationPolicyLevelDataAttributesPagingStrategyConfigurationScheduleStrategy, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ESCALATION_POLICY_LEVEL_DATA_ATTRIBUTES_PAGING_STRATEGY_CONFIGURATION_SCHEDULE_STRATEGY_VALUES!r}"
    )
