from enum import Enum


class UpdateEscalationPolicyLevelDataAttributesPagingStrategyConfigurationScheduleStrategy(str, Enum):
    EVERYONE = "everyone"
    ON_CALL_ONLY = "on_call_only"

    def __str__(self) -> str:
        return str(self.value)
