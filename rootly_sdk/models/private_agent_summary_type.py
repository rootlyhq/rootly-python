from typing import Literal

PrivateAgentSummaryType = Literal["private_agents"]

PRIVATE_AGENT_SUMMARY_TYPE_VALUES: set[PrivateAgentSummaryType] = {
    "private_agents",
}


def check_private_agent_summary_type(value: str | None) -> PrivateAgentSummaryType | None:
    if value is None:
        return None
    if value in PRIVATE_AGENT_SUMMARY_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRIVATE_AGENT_SUMMARY_TYPE_VALUES!r}")
