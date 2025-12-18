from typing import Literal, cast

StatusListDataItemType = Literal["statuses"]

STATUS_LIST_DATA_ITEM_TYPE_VALUES: set[StatusListDataItemType] = {
    "statuses",
}


def check_status_list_data_item_type(value: str) -> StatusListDataItemType:
    if value in STATUS_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(StatusListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STATUS_LIST_DATA_ITEM_TYPE_VALUES!r}")
