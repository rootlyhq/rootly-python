from typing import Literal, cast

CreateEdgeConnectorBodyDataAttributesStatus = Literal["active", "paused"]

CREATE_EDGE_CONNECTOR_BODY_DATA_ATTRIBUTES_STATUS_VALUES: set[CreateEdgeConnectorBodyDataAttributesStatus] = {
    "active",
    "paused",
}


def check_create_edge_connector_body_data_attributes_status(
    value: str | None,
) -> CreateEdgeConnectorBodyDataAttributesStatus | None:
    if value is None:
        return None
    if value in CREATE_EDGE_CONNECTOR_BODY_DATA_ATTRIBUTES_STATUS_VALUES:
        return cast(CreateEdgeConnectorBodyDataAttributesStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_EDGE_CONNECTOR_BODY_DATA_ATTRIBUTES_STATUS_VALUES!r}"
    )
