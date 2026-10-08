from typing import Literal

CreateSlackCanvasTaskParamsTaskType = Literal["create_slack_canvas"]

CREATE_SLACK_CANVAS_TASK_PARAMS_TASK_TYPE_VALUES: set[CreateSlackCanvasTaskParamsTaskType] = {
    "create_slack_canvas",
}


def check_create_slack_canvas_task_params_task_type(value: str | None) -> CreateSlackCanvasTaskParamsTaskType | None:
    if value is None:
        return None
    if value in CREATE_SLACK_CANVAS_TASK_PARAMS_TASK_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREATE_SLACK_CANVAS_TASK_PARAMS_TASK_TYPE_VALUES!r}")
