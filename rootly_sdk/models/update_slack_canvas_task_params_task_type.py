from typing import Literal

UpdateSlackCanvasTaskParamsTaskType = Literal["update_slack_canvas"]

UPDATE_SLACK_CANVAS_TASK_PARAMS_TASK_TYPE_VALUES: set[UpdateSlackCanvasTaskParamsTaskType] = {
    "update_slack_canvas",
}


def check_update_slack_canvas_task_params_task_type(value: str | None) -> UpdateSlackCanvasTaskParamsTaskType | None:
    if value is None:
        return None
    if value in UPDATE_SLACK_CANVAS_TASK_PARAMS_TASK_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_SLACK_CANVAS_TASK_PARAMS_TASK_TYPE_VALUES!r}")
