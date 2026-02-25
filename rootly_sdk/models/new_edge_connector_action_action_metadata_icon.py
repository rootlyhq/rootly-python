from typing import Literal, cast

NewEdgeConnectorActionActionMetadataIcon = Literal[
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

NEW_EDGE_CONNECTOR_ACTION_ACTION_METADATA_ICON_VALUES: set[NewEdgeConnectorActionActionMetadataIcon] = {
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


def check_new_edge_connector_action_action_metadata_icon(
    value: str | None,
) -> NewEdgeConnectorActionActionMetadataIcon | None:
    if value is None:
        return None
    if value in NEW_EDGE_CONNECTOR_ACTION_ACTION_METADATA_ICON_VALUES:
        return cast(NewEdgeConnectorActionActionMetadataIcon, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_EDGE_CONNECTOR_ACTION_ACTION_METADATA_ICON_VALUES!r}"
    )
