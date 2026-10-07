from typing import Literal

CreateShortcutTaskTaskParamsTaskType = Literal["create_shortcut_task"]

CREATE_SHORTCUT_TASK_TASK_PARAMS_TASK_TYPE_VALUES: set[CreateShortcutTaskTaskParamsTaskType] = {
    "create_shortcut_task",
}


def check_create_shortcut_task_task_params_task_type(value: str | None) -> CreateShortcutTaskTaskParamsTaskType | None:
    if value is None:
        return None
    if value in CREATE_SHORTCUT_TASK_TASK_PARAMS_TASK_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_SHORTCUT_TASK_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
