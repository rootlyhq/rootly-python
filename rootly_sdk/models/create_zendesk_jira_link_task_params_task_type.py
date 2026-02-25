from typing import Literal, cast

CreateZendeskJiraLinkTaskParamsTaskType = Literal["create_zendesk_jira_link"]

CREATE_ZENDESK_JIRA_LINK_TASK_PARAMS_TASK_TYPE_VALUES: set[CreateZendeskJiraLinkTaskParamsTaskType] = {
    "create_zendesk_jira_link",
}


def check_create_zendesk_jira_link_task_params_task_type(
    value: str | None,
) -> CreateZendeskJiraLinkTaskParamsTaskType | None:
    if value is None:
        return None
    if value in CREATE_ZENDESK_JIRA_LINK_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(CreateZendeskJiraLinkTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_ZENDESK_JIRA_LINK_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
