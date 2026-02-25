from typing import Literal, cast

EnvironmentListDataItemType = Literal["environments"]

ENVIRONMENT_LIST_DATA_ITEM_TYPE_VALUES: set[EnvironmentListDataItemType] = {
    "environments",
}


def check_environment_list_data_item_type(value: str | None) -> EnvironmentListDataItemType | None:
    if value is None:
        return None
    if value in ENVIRONMENT_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(EnvironmentListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ENVIRONMENT_LIST_DATA_ITEM_TYPE_VALUES!r}")
