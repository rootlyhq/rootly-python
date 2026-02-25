from typing import Literal, cast

AutoAssignRoleVictorOpsTaskParamsTaskType = Literal["auto_assign_role_victor_ops"]

AUTO_ASSIGN_ROLE_VICTOR_OPS_TASK_PARAMS_TASK_TYPE_VALUES: set[AutoAssignRoleVictorOpsTaskParamsTaskType] = {
    "auto_assign_role_victor_ops",
}


def check_auto_assign_role_victor_ops_task_params_task_type(
    value: str | None,
) -> AutoAssignRoleVictorOpsTaskParamsTaskType | None:
    if value is None:
        return None
    if value in AUTO_ASSIGN_ROLE_VICTOR_OPS_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(AutoAssignRoleVictorOpsTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AUTO_ASSIGN_ROLE_VICTOR_OPS_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
