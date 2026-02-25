from typing import Literal, cast

UpdateZendeskTicketTaskParamsTaskType = Literal["update_zendesk_ticket"]

UPDATE_ZENDESK_TICKET_TASK_PARAMS_TASK_TYPE_VALUES: set[UpdateZendeskTicketTaskParamsTaskType] = {
    "update_zendesk_ticket",
}


def check_update_zendesk_ticket_task_params_task_type(
    value: str | None,
) -> UpdateZendeskTicketTaskParamsTaskType | None:
    if value is None:
        return None
    if value in UPDATE_ZENDESK_TICKET_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(UpdateZendeskTicketTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ZENDESK_TICKET_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
