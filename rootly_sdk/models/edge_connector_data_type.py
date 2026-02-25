from typing import Literal, cast

EdgeConnectorDataType = Literal["edge_connectors"]

EDGE_CONNECTOR_DATA_TYPE_VALUES: set[EdgeConnectorDataType] = {
    "edge_connectors",
}


def check_edge_connector_data_type(value: str | None) -> EdgeConnectorDataType | None:
    if value is None:
        return None
    if value in EDGE_CONNECTOR_DATA_TYPE_VALUES:
        return cast(EdgeConnectorDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {EDGE_CONNECTOR_DATA_TYPE_VALUES!r}")
