from typing import Literal, cast

AuthorizationListDataItemType = Literal["authorizations"]

AUTHORIZATION_LIST_DATA_ITEM_TYPE_VALUES: set[AuthorizationListDataItemType] = {
    "authorizations",
}


def check_authorization_list_data_item_type(value: str | None) -> AuthorizationListDataItemType | None:
    if value is None:
        return None
    if value in AUTHORIZATION_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(AuthorizationListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AUTHORIZATION_LIST_DATA_ITEM_TYPE_VALUES!r}")
