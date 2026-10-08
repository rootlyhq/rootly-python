from typing import Literal

PrivateAgentAttributesStatus = Literal["active", "revoked"]

PRIVATE_AGENT_ATTRIBUTES_STATUS_VALUES: set[PrivateAgentAttributesStatus] = {
    "active",
    "revoked",
}


def check_private_agent_attributes_status(value: str | None) -> PrivateAgentAttributesStatus | None:
    if value is None:
        return None
    if value in PRIVATE_AGENT_ATTRIBUTES_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRIVATE_AGENT_ATTRIBUTES_STATUS_VALUES!r}")
