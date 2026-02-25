from typing import Literal, cast

CreateEdgeConnectorActionBodyActionActionType = Literal["http", "script"]

CREATE_EDGE_CONNECTOR_ACTION_BODY_ACTION_ACTION_TYPE_VALUES: set[CreateEdgeConnectorActionBodyActionActionType] = {
    "http",
    "script",
}


def check_create_edge_connector_action_body_action_action_type(
    value: str | None,
) -> CreateEdgeConnectorActionBodyActionActionType | None:
    if value is None:
        return None
    if value in CREATE_EDGE_CONNECTOR_ACTION_BODY_ACTION_ACTION_TYPE_VALUES:
        return cast(CreateEdgeConnectorActionBodyActionActionType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_EDGE_CONNECTOR_ACTION_BODY_ACTION_ACTION_TYPE_VALUES!r}"
    )
