from typing import Literal, cast

UpdateEscalationPolicyLevelDataAttributesPagingStrategyConfigurationScheduleStrategy = Literal[
    "everyone", "on_call_only"
]

UPDATE_ESCALATION_POLICY_LEVEL_DATA_ATTRIBUTES_PAGING_STRATEGY_CONFIGURATION_SCHEDULE_STRATEGY_VALUES: set[
    UpdateEscalationPolicyLevelDataAttributesPagingStrategyConfigurationScheduleStrategy
] = {
    "everyone",
    "on_call_only",
}


def check_update_escalation_policy_level_data_attributes_paging_strategy_configuration_schedule_strategy(
    value: str | None,
) -> UpdateEscalationPolicyLevelDataAttributesPagingStrategyConfigurationScheduleStrategy | None:
    if value is None:
        return None
    if value in UPDATE_ESCALATION_POLICY_LEVEL_DATA_ATTRIBUTES_PAGING_STRATEGY_CONFIGURATION_SCHEDULE_STRATEGY_VALUES:
        return cast(UpdateEscalationPolicyLevelDataAttributesPagingStrategyConfigurationScheduleStrategy, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ESCALATION_POLICY_LEVEL_DATA_ATTRIBUTES_PAGING_STRATEGY_CONFIGURATION_SCHEDULE_STRATEGY_VALUES!r}"
    )
