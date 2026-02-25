from typing import Literal, cast

UpdateMotionTaskTaskParamsTaskType = Literal["update_motion_task"]

UPDATE_MOTION_TASK_TASK_PARAMS_TASK_TYPE_VALUES: set[UpdateMotionTaskTaskParamsTaskType] = {
    "update_motion_task",
}


def check_update_motion_task_task_params_task_type(value: str | None) -> UpdateMotionTaskTaskParamsTaskType | None:
    if value is None:
        return None
    if value in UPDATE_MOTION_TASK_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(UpdateMotionTaskTaskParamsTaskType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_MOTION_TASK_TASK_PARAMS_TASK_TYPE_VALUES!r}")
