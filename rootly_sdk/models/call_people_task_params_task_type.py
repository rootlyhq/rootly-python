from typing import Literal, cast

CallPeopleTaskParamsTaskType = Literal["call_people"]

CALL_PEOPLE_TASK_PARAMS_TASK_TYPE_VALUES: set[CallPeopleTaskParamsTaskType] = {
    "call_people",
}


def check_call_people_task_params_task_type(value: str | None) -> CallPeopleTaskParamsTaskType | None:
    if value is None:
        return None
    if value in CALL_PEOPLE_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(CallPeopleTaskParamsTaskType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CALL_PEOPLE_TASK_PARAMS_TASK_TYPE_VALUES!r}")
