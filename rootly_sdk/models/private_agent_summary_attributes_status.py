from typing import Literal

PrivateAgentSummaryAttributesStatus = Literal["active", "revoked"]

PRIVATE_AGENT_SUMMARY_ATTRIBUTES_STATUS_VALUES: set[PrivateAgentSummaryAttributesStatus] = {
    "active",
    "revoked",
}


def check_private_agent_summary_attributes_status(value: str | None) -> PrivateAgentSummaryAttributesStatus | None:
    if value is None:
        return None
    if value in PRIVATE_AGENT_SUMMARY_ATTRIBUTES_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRIVATE_AGENT_SUMMARY_ATTRIBUTES_STATUS_VALUES!r}")
