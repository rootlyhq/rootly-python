from typing import Literal, cast

UpdateEdgeConnectorActionActionActionType = Literal["http", "script"]

UPDATE_EDGE_CONNECTOR_ACTION_ACTION_ACTION_TYPE_VALUES: set[UpdateEdgeConnectorActionActionActionType] = {
    "http",
    "script",
}


def check_update_edge_connector_action_action_action_type(
    value: str | None,
) -> UpdateEdgeConnectorActionActionActionType | None:
    if value is None:
        return None
    if value in UPDATE_EDGE_CONNECTOR_ACTION_ACTION_ACTION_TYPE_VALUES:
        return cast(UpdateEdgeConnectorActionActionActionType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_EDGE_CONNECTOR_ACTION_ACTION_ACTION_TYPE_VALUES!r}"
    )
