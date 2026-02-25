from typing import Literal, cast

GetPulsesTaskParamsTaskType = Literal["get_pulses"]

GET_PULSES_TASK_PARAMS_TASK_TYPE_VALUES: set[GetPulsesTaskParamsTaskType] = {
    "get_pulses",
}


def check_get_pulses_task_params_task_type(value: str | None) -> GetPulsesTaskParamsTaskType | None:
    if value is None:
        return None
    if value in GET_PULSES_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(GetPulsesTaskParamsTaskType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_PULSES_TASK_PARAMS_TASK_TYPE_VALUES!r}")
