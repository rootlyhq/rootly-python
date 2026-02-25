from typing import Literal, cast

NewEdgeConnectorActionActionMetadataParametersType0ItemType = Literal["boolean", "number", "string"]

NEW_EDGE_CONNECTOR_ACTION_ACTION_METADATA_PARAMETERS_TYPE_0_ITEM_TYPE_VALUES: set[
    NewEdgeConnectorActionActionMetadataParametersType0ItemType
] = {
    "boolean",
    "number",
    "string",
}


def check_new_edge_connector_action_action_metadata_parameters_type_0_item_type(
    value: str | None,
) -> NewEdgeConnectorActionActionMetadataParametersType0ItemType | None:
    if value is None:
        return None
    if value in NEW_EDGE_CONNECTOR_ACTION_ACTION_METADATA_PARAMETERS_TYPE_0_ITEM_TYPE_VALUES:
        return cast(NewEdgeConnectorActionActionMetadataParametersType0ItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_EDGE_CONNECTOR_ACTION_ACTION_METADATA_PARAMETERS_TYPE_0_ITEM_TYPE_VALUES!r}"
    )
