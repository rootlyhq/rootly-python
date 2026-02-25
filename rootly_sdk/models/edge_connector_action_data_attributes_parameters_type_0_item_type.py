from typing import Literal, cast

EdgeConnectorActionDataAttributesParametersType0ItemType = Literal["boolean", "number", "string"]

EDGE_CONNECTOR_ACTION_DATA_ATTRIBUTES_PARAMETERS_TYPE_0_ITEM_TYPE_VALUES: set[
    EdgeConnectorActionDataAttributesParametersType0ItemType
] = {
    "boolean",
    "number",
    "string",
}


def check_edge_connector_action_data_attributes_parameters_type_0_item_type(
    value: str | None,
) -> EdgeConnectorActionDataAttributesParametersType0ItemType | None:
    if value is None:
        return None
    if value in EDGE_CONNECTOR_ACTION_DATA_ATTRIBUTES_PARAMETERS_TYPE_0_ITEM_TYPE_VALUES:
        return cast(EdgeConnectorActionDataAttributesParametersType0ItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {EDGE_CONNECTOR_ACTION_DATA_ATTRIBUTES_PARAMETERS_TYPE_0_ITEM_TYPE_VALUES!r}"
    )
