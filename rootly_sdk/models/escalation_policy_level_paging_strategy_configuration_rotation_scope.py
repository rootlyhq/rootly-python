from typing import Literal

EscalationPolicyLevelPagingStrategyConfigurationRotationScope = Literal["active_rotation", "entire_schedule"]

ESCALATION_POLICY_LEVEL_PAGING_STRATEGY_CONFIGURATION_ROTATION_SCOPE_VALUES: set[
    EscalationPolicyLevelPagingStrategyConfigurationRotationScope
] = {
    "active_rotation",
    "entire_schedule",
}


def check_escalation_policy_level_paging_strategy_configuration_rotation_scope(
    value: str | None,
) -> EscalationPolicyLevelPagingStrategyConfigurationRotationScope | None:
    if value is None:
        return None
    if value in ESCALATION_POLICY_LEVEL_PAGING_STRATEGY_CONFIGURATION_ROTATION_SCOPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ESCALATION_POLICY_LEVEL_PAGING_STRATEGY_CONFIGURATION_ROTATION_SCOPE_VALUES!r}"
    )
