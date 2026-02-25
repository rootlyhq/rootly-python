from typing import Literal, cast

SecretListDataItemType = Literal["secrets"]

SECRET_LIST_DATA_ITEM_TYPE_VALUES: set[SecretListDataItemType] = {
    "secrets",
}


def check_secret_list_data_item_type(value: str | None) -> SecretListDataItemType | None:
    if value is None:
        return None
    if value in SECRET_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(SecretListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SECRET_LIST_DATA_ITEM_TYPE_VALUES!r}")
