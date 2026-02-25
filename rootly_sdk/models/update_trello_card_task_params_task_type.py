from typing import Literal, cast

UpdateTrelloCardTaskParamsTaskType = Literal["update_trello_card"]

UPDATE_TRELLO_CARD_TASK_PARAMS_TASK_TYPE_VALUES: set[UpdateTrelloCardTaskParamsTaskType] = {
    "update_trello_card",
}


def check_update_trello_card_task_params_task_type(value: str | None) -> UpdateTrelloCardTaskParamsTaskType | None:
    if value is None:
        return None
    if value in UPDATE_TRELLO_CARD_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(UpdateTrelloCardTaskParamsTaskType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_TRELLO_CARD_TASK_PARAMS_TASK_TYPE_VALUES!r}")
