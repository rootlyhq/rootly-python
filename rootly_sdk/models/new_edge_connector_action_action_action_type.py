from typing import Literal, cast

NewEdgeConnectorActionActionActionType = Literal["http", "script"]

NEW_EDGE_CONNECTOR_ACTION_ACTION_ACTION_TYPE_VALUES: set[NewEdgeConnectorActionActionActionType] = {
    "http",
    "script",
}


def check_new_edge_connector_action_action_action_type(
    value: str | None,
) -> NewEdgeConnectorActionActionActionType | None:
    if value is None:
        return None
    if value in NEW_EDGE_CONNECTOR_ACTION_ACTION_ACTION_TYPE_VALUES:
        return cast(NewEdgeConnectorActionActionActionType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_EDGE_CONNECTOR_ACTION_ACTION_ACTION_TYPE_VALUES!r}"
    )
