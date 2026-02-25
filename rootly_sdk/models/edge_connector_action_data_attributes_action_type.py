from typing import Literal, cast

EdgeConnectorActionDataAttributesActionType = Literal["http", "script"]

EDGE_CONNECTOR_ACTION_DATA_ATTRIBUTES_ACTION_TYPE_VALUES: set[EdgeConnectorActionDataAttributesActionType] = {
    "http",
    "script",
}


def check_edge_connector_action_data_attributes_action_type(value: str | None) -> EdgeConnectorActionDataAttributesActionType | None:
    if value is None:
        return None
    if value in EDGE_CONNECTOR_ACTION_DATA_ATTRIBUTES_ACTION_TYPE_VALUES:
        return cast(EdgeConnectorActionDataAttributesActionType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {EDGE_CONNECTOR_ACTION_DATA_ATTRIBUTES_ACTION_TYPE_VALUES!r}"
    )
