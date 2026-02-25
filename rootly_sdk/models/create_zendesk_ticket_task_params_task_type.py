from typing import Literal, cast

CreateZendeskTicketTaskParamsTaskType = Literal["create_zendesk_ticket"]

CREATE_ZENDESK_TICKET_TASK_PARAMS_TASK_TYPE_VALUES: set[CreateZendeskTicketTaskParamsTaskType] = {
    "create_zendesk_ticket",
}


def check_create_zendesk_ticket_task_params_task_type(
    value: str | None,
) -> CreateZendeskTicketTaskParamsTaskType | None:
    if value is None:
        return None
    if value in CREATE_ZENDESK_TICKET_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(CreateZendeskTicketTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_ZENDESK_TICKET_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
