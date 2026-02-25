from typing import Literal, cast

EdgeConnectorDataAttributesStatus = Literal["active", "paused"]

EDGE_CONNECTOR_DATA_ATTRIBUTES_STATUS_VALUES: set[EdgeConnectorDataAttributesStatus] = {
    "active",
    "paused",
}


def check_edge_connector_data_attributes_status(value: str | None) -> EdgeConnectorDataAttributesStatus | None:
    if value is None:
        return None
    if value in EDGE_CONNECTOR_DATA_ATTRIBUTES_STATUS_VALUES:
        return cast(EdgeConnectorDataAttributesStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {EDGE_CONNECTOR_DATA_ATTRIBUTES_STATUS_VALUES!r}")
