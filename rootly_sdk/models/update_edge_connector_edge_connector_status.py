from typing import Literal, cast

UpdateEdgeConnectorEdgeConnectorStatus = Literal["active", "paused"]

UPDATE_EDGE_CONNECTOR_EDGE_CONNECTOR_STATUS_VALUES: set[UpdateEdgeConnectorEdgeConnectorStatus] = {
    "active",
    "paused",
}


def check_update_edge_connector_edge_connector_status(
    value: str | None,
) -> UpdateEdgeConnectorEdgeConnectorStatus | None:
    if value is None:
        return None
    if value in UPDATE_EDGE_CONNECTOR_EDGE_CONNECTOR_STATUS_VALUES:
        return cast(UpdateEdgeConnectorEdgeConnectorStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_EDGE_CONNECTOR_EDGE_CONNECTOR_STATUS_VALUES!r}"
    )
