from typing import Literal, cast

UpdateShortcutTaskTaskParamsTaskType = Literal["update_shortcut_task"]

UPDATE_SHORTCUT_TASK_TASK_PARAMS_TASK_TYPE_VALUES: set[UpdateShortcutTaskTaskParamsTaskType] = {
    "update_shortcut_task",
}


def check_update_shortcut_task_task_params_task_type(value: str | None) -> UpdateShortcutTaskTaskParamsTaskType | None:
    if value is None:
        return None
    if value in UPDATE_SHORTCUT_TASK_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(UpdateShortcutTaskTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_SHORTCUT_TASK_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
