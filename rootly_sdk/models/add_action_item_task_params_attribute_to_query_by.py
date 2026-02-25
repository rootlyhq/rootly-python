from typing import Literal, cast

AddActionItemTaskParamsAttributeToQueryBy = Literal["jira_issue_id"]

ADD_ACTION_ITEM_TASK_PARAMS_ATTRIBUTE_TO_QUERY_BY_VALUES: set[AddActionItemTaskParamsAttributeToQueryBy] = {
    "jira_issue_id",
}


def check_add_action_item_task_params_attribute_to_query_by(
    value: str | None,
) -> AddActionItemTaskParamsAttributeToQueryBy | None:
    if value is None:
        return None
    if value in ADD_ACTION_ITEM_TASK_PARAMS_ATTRIBUTE_TO_QUERY_BY_VALUES:
        return cast(AddActionItemTaskParamsAttributeToQueryBy, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ADD_ACTION_ITEM_TASK_PARAMS_ATTRIBUTE_TO_QUERY_BY_VALUES!r}"
    )
