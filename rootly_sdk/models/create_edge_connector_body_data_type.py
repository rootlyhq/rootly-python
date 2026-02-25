from typing import Literal, cast

CreateEdgeConnectorBodyDataType = Literal["edge_connectors"]

CREATE_EDGE_CONNECTOR_BODY_DATA_TYPE_VALUES: set[CreateEdgeConnectorBodyDataType] = {
    "edge_connectors",
}


def check_create_edge_connector_body_data_type(value: str | None) -> CreateEdgeConnectorBodyDataType | None:
    if value is None:
        return None
    if value in CREATE_EDGE_CONNECTOR_BODY_DATA_TYPE_VALUES:
        return cast(CreateEdgeConnectorBodyDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREATE_EDGE_CONNECTOR_BODY_DATA_TYPE_VALUES!r}")
