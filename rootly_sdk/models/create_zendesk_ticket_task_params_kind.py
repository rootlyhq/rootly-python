from typing import Literal, cast

CreateZendeskTicketTaskParamsKind = Literal["incident", "problem", "question", "task"]

CREATE_ZENDESK_TICKET_TASK_PARAMS_KIND_VALUES: set[CreateZendeskTicketTaskParamsKind] = {
    "incident",
    "problem",
    "question",
    "task",
}


def check_create_zendesk_ticket_task_params_kind(value: str | None) -> CreateZendeskTicketTaskParamsKind | None:
    if value is None:
        return None
    if value in CREATE_ZENDESK_TICKET_TASK_PARAMS_KIND_VALUES:
        return cast(CreateZendeskTicketTaskParamsKind, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREATE_ZENDESK_TICKET_TASK_PARAMS_KIND_VALUES!r}")
