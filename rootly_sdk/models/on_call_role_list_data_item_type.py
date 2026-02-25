from typing import Literal, cast

OnCallRoleListDataItemType = Literal["on_call_roles"]

ON_CALL_ROLE_LIST_DATA_ITEM_TYPE_VALUES: set[OnCallRoleListDataItemType] = {
    "on_call_roles",
}


def check_on_call_role_list_data_item_type(value: str | None) -> OnCallRoleListDataItemType | None:
    if value is None:
        return None
    if value in ON_CALL_ROLE_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(OnCallRoleListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ON_CALL_ROLE_LIST_DATA_ITEM_TYPE_VALUES!r}")
