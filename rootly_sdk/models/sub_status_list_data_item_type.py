from typing import Literal, cast

SubStatusListDataItemType = Literal["sub_statuses"]

SUB_STATUS_LIST_DATA_ITEM_TYPE_VALUES: set[SubStatusListDataItemType] = {
    "sub_statuses",
}


def check_sub_status_list_data_item_type(value: str | None) -> SubStatusListDataItemType | None:
    if value is None:
        return None
    if value in SUB_STATUS_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(SubStatusListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SUB_STATUS_LIST_DATA_ITEM_TYPE_VALUES!r}")
