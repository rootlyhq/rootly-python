from typing import Literal

PrivateAgentAttributesDeploymentMode = Literal["combined", "split-core"]

PRIVATE_AGENT_ATTRIBUTES_DEPLOYMENT_MODE_VALUES: set[PrivateAgentAttributesDeploymentMode] = {
    "combined",
    "split-core",
}


def check_private_agent_attributes_deployment_mode(value: str | None) -> PrivateAgentAttributesDeploymentMode | None:
    if value is None:
        return None
    if value in PRIVATE_AGENT_ATTRIBUTES_DEPLOYMENT_MODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRIVATE_AGENT_ATTRIBUTES_DEPLOYMENT_MODE_VALUES!r}")
