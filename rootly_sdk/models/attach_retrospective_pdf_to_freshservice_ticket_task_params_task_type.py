from typing import Literal

AttachRetrospectivePdfToFreshserviceTicketTaskParamsTaskType = Literal[
    "attach_retrospective_pdf_to_freshservice_ticket"
]

ATTACH_RETROSPECTIVE_PDF_TO_FRESHSERVICE_TICKET_TASK_PARAMS_TASK_TYPE_VALUES: set[
    AttachRetrospectivePdfToFreshserviceTicketTaskParamsTaskType
] = {
    "attach_retrospective_pdf_to_freshservice_ticket",
}


def check_attach_retrospective_pdf_to_freshservice_ticket_task_params_task_type(
    value: str | None,
) -> AttachRetrospectivePdfToFreshserviceTicketTaskParamsTaskType | None:
    if value is None:
        return None
    if value in ATTACH_RETROSPECTIVE_PDF_TO_FRESHSERVICE_TICKET_TASK_PARAMS_TASK_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ATTACH_RETROSPECTIVE_PDF_TO_FRESHSERVICE_TICKET_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
