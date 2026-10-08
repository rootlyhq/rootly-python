from typing import Literal

NewEdgeConnectorEdgeConnectorStatus = Literal["active", "paused"]

NEW_EDGE_CONNECTOR_EDGE_CONNECTOR_STATUS_VALUES: set[NewEdgeConnectorEdgeConnectorStatus] = {
    "active",
    "paused",
}


def check_new_edge_connector_edge_connector_status(value: str | None) -> NewEdgeConnectorEdgeConnectorStatus | None:
    if value is None:
        return None
    if value in NEW_EDGE_CONNECTOR_EDGE_CONNECTOR_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_EDGE_CONNECTOR_EDGE_CONNECTOR_STATUS_VALUES!r}")
