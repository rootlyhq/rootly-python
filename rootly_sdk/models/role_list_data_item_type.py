from typing import Literal

RoleListDataItemType = Literal["roles"]

ROLE_LIST_DATA_ITEM_TYPE_VALUES: set[RoleListDataItemType] = {
    "roles",
}


def check_role_list_data_item_type(value: str | None) -> RoleListDataItemType | None:
    if value is None:
        return None
    if value in ROLE_LIST_DATA_ITEM_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ROLE_LIST_DATA_ITEM_TYPE_VALUES!r}")
