from typing import Literal

UpdateSlackCanvasTaskParamsOperation = Literal["insert_at_end", "replace"]

UPDATE_SLACK_CANVAS_TASK_PARAMS_OPERATION_VALUES: set[UpdateSlackCanvasTaskParamsOperation] = {
    "insert_at_end",
    "replace",
}


def check_update_slack_canvas_task_params_operation(value: str | None) -> UpdateSlackCanvasTaskParamsOperation | None:
    if value is None:
        return None
    if value in UPDATE_SLACK_CANVAS_TASK_PARAMS_OPERATION_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_SLACK_CANVAS_TASK_PARAMS_OPERATION_VALUES!r}")
