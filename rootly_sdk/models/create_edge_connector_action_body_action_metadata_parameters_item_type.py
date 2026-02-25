from typing import Literal, cast

CreateEdgeConnectorActionBodyActionMetadataParametersItemType = Literal["boolean", "number", "string"]

CREATE_EDGE_CONNECTOR_ACTION_BODY_ACTION_METADATA_PARAMETERS_ITEM_TYPE_VALUES: set[
    CreateEdgeConnectorActionBodyActionMetadataParametersItemType
] = {
    "boolean",
    "number",
    "string",
}


def check_create_edge_connector_action_body_action_metadata_parameters_item_type(
    value: str | None,
) -> CreateEdgeConnectorActionBodyActionMetadataParametersItemType | None:
    if value is None:
        return None
    if value in CREATE_EDGE_CONNECTOR_ACTION_BODY_ACTION_METADATA_PARAMETERS_ITEM_TYPE_VALUES:
        return cast(CreateEdgeConnectorActionBodyActionMetadataParametersItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_EDGE_CONNECTOR_ACTION_BODY_ACTION_METADATA_PARAMETERS_ITEM_TYPE_VALUES!r}"
    )
