from typing import Literal, cast

ApiKeyListDataItemType = Literal["api_keys"]

API_KEY_LIST_DATA_ITEM_TYPE_VALUES: set[ApiKeyListDataItemType] = {
    "api_keys",
}


def check_api_key_list_data_item_type(value: str | None) -> ApiKeyListDataItemType | None:
    if value is None:
        return None
    if value in API_KEY_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(ApiKeyListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_KEY_LIST_DATA_ITEM_TYPE_VALUES!r}")
