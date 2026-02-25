from typing import Literal, cast

UpdateEdgeConnectorBodyDataAttributesStatus = Literal["active", "paused"]

UPDATE_EDGE_CONNECTOR_BODY_DATA_ATTRIBUTES_STATUS_VALUES: set[UpdateEdgeConnectorBodyDataAttributesStatus] = {
    "active",
    "paused",
}


def check_update_edge_connector_body_data_attributes_status(
    value: str | None,
) -> UpdateEdgeConnectorBodyDataAttributesStatus | None:
    if value is None:
        return None
    if value in UPDATE_EDGE_CONNECTOR_BODY_DATA_ATTRIBUTES_STATUS_VALUES:
        return cast(UpdateEdgeConnectorBodyDataAttributesStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_EDGE_CONNECTOR_BODY_DATA_ATTRIBUTES_STATUS_VALUES!r}"
    )
