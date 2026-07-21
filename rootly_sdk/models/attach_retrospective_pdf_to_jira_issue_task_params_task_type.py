from typing import Literal, cast

AttachRetrospectivePdfToJiraIssueTaskParamsTaskType = Literal["attach_retrospective_pdf_to_jira_issue"]

ATTACH_RETROSPECTIVE_PDF_TO_JIRA_ISSUE_TASK_PARAMS_TASK_TYPE_VALUES: set[
    AttachRetrospectivePdfToJiraIssueTaskParamsTaskType
] = {
    "attach_retrospective_pdf_to_jira_issue",
}


def check_attach_retrospective_pdf_to_jira_issue_task_params_task_type(
    value: str | None,
) -> AttachRetrospectivePdfToJiraIssueTaskParamsTaskType | None:
    if value is None:
        return None
    if value in ATTACH_RETROSPECTIVE_PDF_TO_JIRA_ISSUE_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(AttachRetrospectivePdfToJiraIssueTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ATTACH_RETROSPECTIVE_PDF_TO_JIRA_ISSUE_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
