from typing import Literal

PrivateAgentType = Literal["private_agents"]

PRIVATE_AGENT_TYPE_VALUES: set[PrivateAgentType] = {
    "private_agents",
}


def check_private_agent_type(value: str | None) -> PrivateAgentType | None:
    if value is None:
        return None
    if value in PRIVATE_AGENT_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRIVATE_AGENT_TYPE_VALUES!r}")
