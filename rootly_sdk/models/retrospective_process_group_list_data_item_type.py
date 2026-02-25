from typing import Literal, cast

RetrospectiveProcessGroupListDataItemType = Literal["retrospective_process_groups"]

RETROSPECTIVE_PROCESS_GROUP_LIST_DATA_ITEM_TYPE_VALUES: set[RetrospectiveProcessGroupListDataItemType] = {
    "retrospective_process_groups",
}


def check_retrospective_process_group_list_data_item_type(
    value: str | None,
) -> RetrospectiveProcessGroupListDataItemType | None:
    if value is None:
        return None
    if value in RETROSPECTIVE_PROCESS_GROUP_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(RetrospectiveProcessGroupListDataItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RETROSPECTIVE_PROCESS_GROUP_LIST_DATA_ITEM_TYPE_VALUES!r}"
    )
