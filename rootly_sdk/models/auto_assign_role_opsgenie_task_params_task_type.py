from typing import Literal, cast

AutoAssignRoleOpsgenieTaskParamsTaskType = Literal["auto_assign_role_opsgenie"]

AUTO_ASSIGN_ROLE_OPSGENIE_TASK_PARAMS_TASK_TYPE_VALUES: set[AutoAssignRoleOpsgenieTaskParamsTaskType] = {
    "auto_assign_role_opsgenie",
}


def check_auto_assign_role_opsgenie_task_params_task_type(value: str | None) -> AutoAssignRoleOpsgenieTaskParamsTaskType | None:
    if value is None:
        return None
    if value in AUTO_ASSIGN_ROLE_OPSGENIE_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(AutoAssignRoleOpsgenieTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AUTO_ASSIGN_ROLE_OPSGENIE_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
