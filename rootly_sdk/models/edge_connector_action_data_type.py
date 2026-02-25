from typing import Literal, cast

EdgeConnectorActionDataType = Literal["edge_connector_actions"]

EDGE_CONNECTOR_ACTION_DATA_TYPE_VALUES: set[EdgeConnectorActionDataType] = {
    "edge_connector_actions",
}


def check_edge_connector_action_data_type(value: str | None) -> EdgeConnectorActionDataType | None:
    if value is None:
        return None
    if value in EDGE_CONNECTOR_ACTION_DATA_TYPE_VALUES:
        return cast(EdgeConnectorActionDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {EDGE_CONNECTOR_ACTION_DATA_TYPE_VALUES!r}")
