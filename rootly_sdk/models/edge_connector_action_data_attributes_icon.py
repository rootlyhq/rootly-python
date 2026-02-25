from typing import Literal, cast

EdgeConnectorActionDataAttributesIcon = Literal[
    "arrow-path",
    "bolt",
    "bolt-slash",
    "code-bracket",
    "cog",
    "command-line",
    "cube",
    "play",
    "rocket-launch",
    "server",
    "server-stack",
    "wrench-screwdriver",
]

EDGE_CONNECTOR_ACTION_DATA_ATTRIBUTES_ICON_VALUES: set[EdgeConnectorActionDataAttributesIcon] = {
    "arrow-path",
    "bolt",
    "bolt-slash",
    "code-bracket",
    "cog",
    "command-line",
    "cube",
    "play",
    "rocket-launch",
    "server",
    "server-stack",
    "wrench-screwdriver",
}


def check_edge_connector_action_data_attributes_icon(value: str | None) -> EdgeConnectorActionDataAttributesIcon | None:
    if value is None:
        return None
    if value in EDGE_CONNECTOR_ACTION_DATA_ATTRIBUTES_ICON_VALUES:
        return cast(EdgeConnectorActionDataAttributesIcon, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {EDGE_CONNECTOR_ACTION_DATA_ATTRIBUTES_ICON_VALUES!r}"
    )
