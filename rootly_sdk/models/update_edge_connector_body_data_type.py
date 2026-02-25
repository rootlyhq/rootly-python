from typing import Literal, cast

UpdateEdgeConnectorBodyDataType = Literal["edge_connectors"]

UPDATE_EDGE_CONNECTOR_BODY_DATA_TYPE_VALUES: set[UpdateEdgeConnectorBodyDataType] = {
    "edge_connectors",
}


def check_update_edge_connector_body_data_type(value: str | None) -> UpdateEdgeConnectorBodyDataType | None:
    if value is None:
        return None
    if value in UPDATE_EDGE_CONNECTOR_BODY_DATA_TYPE_VALUES:
        return cast(UpdateEdgeConnectorBodyDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_EDGE_CONNECTOR_BODY_DATA_TYPE_VALUES!r}")
