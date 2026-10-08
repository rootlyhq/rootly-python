from typing import Literal

PrivateAgentSummaryAttributesDeploymentMode = Literal["combined", "split-core"]

PRIVATE_AGENT_SUMMARY_ATTRIBUTES_DEPLOYMENT_MODE_VALUES: set[PrivateAgentSummaryAttributesDeploymentMode] = {
    "combined",
    "split-core",
}


def check_private_agent_summary_attributes_deployment_mode(
    value: str | None,
) -> PrivateAgentSummaryAttributesDeploymentMode | None:
    if value is None:
        return None
    if value in PRIVATE_AGENT_SUMMARY_ATTRIBUTES_DEPLOYMENT_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PRIVATE_AGENT_SUMMARY_ATTRIBUTES_DEPLOYMENT_MODE_VALUES!r}"
    )
