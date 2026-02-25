from typing import Literal, cast

UpdateShortcutStoryTaskParamsTaskType = Literal["update_shortcut_story"]

UPDATE_SHORTCUT_STORY_TASK_PARAMS_TASK_TYPE_VALUES: set[UpdateShortcutStoryTaskParamsTaskType] = {
    "update_shortcut_story",
}


def check_update_shortcut_story_task_params_task_type(value: str | None) -> UpdateShortcutStoryTaskParamsTaskType | None:
    if value is None:
        return None
    if value in UPDATE_SHORTCUT_STORY_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(UpdateShortcutStoryTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_SHORTCUT_STORY_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
