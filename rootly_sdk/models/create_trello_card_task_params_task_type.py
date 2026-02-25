from typing import Literal, cast

CreateTrelloCardTaskParamsTaskType = Literal["create_trello_card"]

CREATE_TRELLO_CARD_TASK_PARAMS_TASK_TYPE_VALUES: set[CreateTrelloCardTaskParamsTaskType] = {
    "create_trello_card",
}


def check_create_trello_card_task_params_task_type(value: str | None) -> CreateTrelloCardTaskParamsTaskType | None:
    if value is None:
        return None
    if value in CREATE_TRELLO_CARD_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(CreateTrelloCardTaskParamsTaskType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREATE_TRELLO_CARD_TASK_PARAMS_TASK_TYPE_VALUES!r}")
