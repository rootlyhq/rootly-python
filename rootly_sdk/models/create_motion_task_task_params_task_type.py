from typing import Literal, cast

CreateMotionTaskTaskParamsTaskType = Literal["create_motion_task"]

CREATE_MOTION_TASK_TASK_PARAMS_TASK_TYPE_VALUES: set[CreateMotionTaskTaskParamsTaskType] = {
    "create_motion_task",
}


def check_create_motion_task_task_params_task_type(value: str | None) -> CreateMotionTaskTaskParamsTaskType | None:
    if value is None:
        return None
    if value in CREATE_MOTION_TASK_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(CreateMotionTaskTaskParamsTaskType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREATE_MOTION_TASK_TASK_PARAMS_TASK_TYPE_VALUES!r}")
