from typing import Literal, cast

RetrospectiveProcessGroupStepListDataItemType = Literal["retrospective_process_group_steps"]

RETROSPECTIVE_PROCESS_GROUP_STEP_LIST_DATA_ITEM_TYPE_VALUES: set[RetrospectiveProcessGroupStepListDataItemType] = {
    "retrospective_process_group_steps",
}


def check_retrospective_process_group_step_list_data_item_type(
    value: str | None,
) -> RetrospectiveProcessGroupStepListDataItemType | None:
    if value is None:
        return None
    if value in RETROSPECTIVE_PROCESS_GROUP_STEP_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(RetrospectiveProcessGroupStepListDataItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RETROSPECTIVE_PROCESS_GROUP_STEP_LIST_DATA_ITEM_TYPE_VALUES!r}"
    )
