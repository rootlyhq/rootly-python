from typing import Literal, cast

AutoAssignRoleRootlyTaskParamsTaskType = Literal["auto_assign_role_rootly"]

AUTO_ASSIGN_ROLE_ROOTLY_TASK_PARAMS_TASK_TYPE_VALUES: set[AutoAssignRoleRootlyTaskParamsTaskType] = {
    "auto_assign_role_rootly",
}


def check_auto_assign_role_rootly_task_params_task_type(value: str | None) -> AutoAssignRoleRootlyTaskParamsTaskType | None:
    if value is None:
        return None
    if value in AUTO_ASSIGN_ROLE_ROOTLY_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(AutoAssignRoleRootlyTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AUTO_ASSIGN_ROLE_ROOTLY_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
