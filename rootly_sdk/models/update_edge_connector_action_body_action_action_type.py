from typing import Literal, cast

UpdateEdgeConnectorActionBodyActionActionType = Literal["http", "script"]

UPDATE_EDGE_CONNECTOR_ACTION_BODY_ACTION_ACTION_TYPE_VALUES: set[UpdateEdgeConnectorActionBodyActionActionType] = {
    "http",
    "script",
}


def check_update_edge_connector_action_body_action_action_type(
    value: str | None,
) -> UpdateEdgeConnectorActionBodyActionActionType | None:
    if value is None:
        return None
    if value in UPDATE_EDGE_CONNECTOR_ACTION_BODY_ACTION_ACTION_TYPE_VALUES:
        return cast(UpdateEdgeConnectorActionBodyActionActionType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_EDGE_CONNECTOR_ACTION_BODY_ACTION_ACTION_TYPE_VALUES!r}"
    )
