from typing import Literal, cast

AddRoleTaskParamsTaskType = Literal["add_role"]

ADD_ROLE_TASK_PARAMS_TASK_TYPE_VALUES: set[AddRoleTaskParamsTaskType] = {
    "add_role",
}


def check_add_role_task_params_task_type(value: str | None) -> AddRoleTaskParamsTaskType | None:
    if value is None:
        return None
    if value in ADD_ROLE_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(AddRoleTaskParamsTaskType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ADD_ROLE_TASK_PARAMS_TASK_TYPE_VALUES!r}")
