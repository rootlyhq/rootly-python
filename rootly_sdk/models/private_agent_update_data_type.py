from typing import Literal

PrivateAgentUpdateDataType = Literal["private_agents"]

PRIVATE_AGENT_UPDATE_DATA_TYPE_VALUES: set[PrivateAgentUpdateDataType] = {
    "private_agents",
}


def check_private_agent_update_data_type(value: str | None) -> PrivateAgentUpdateDataType | None:
    if value is None:
        return None
    if value in PRIVATE_AGENT_UPDATE_DATA_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRIVATE_AGENT_UPDATE_DATA_TYPE_VALUES!r}")
