from typing import Literal, cast

AddToTimelineTaskParamsTaskType = Literal["add_to_timeline"]

ADD_TO_TIMELINE_TASK_PARAMS_TASK_TYPE_VALUES: set[AddToTimelineTaskParamsTaskType] = {
    "add_to_timeline",
}


def check_add_to_timeline_task_params_task_type(value: str | None) -> AddToTimelineTaskParamsTaskType | None:
    if value is None:
        return None
    if value in ADD_TO_TIMELINE_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(AddToTimelineTaskParamsTaskType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ADD_TO_TIMELINE_TASK_PARAMS_TASK_TYPE_VALUES!r}")
