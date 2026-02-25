from typing import Literal, cast

ServiceListDataItemType = Literal["services"]

SERVICE_LIST_DATA_ITEM_TYPE_VALUES: set[ServiceListDataItemType] = {
    "services",
}


def check_service_list_data_item_type(value: str | None) -> ServiceListDataItemType | None:
    if value is None:
        return None
    if value in SERVICE_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(ServiceListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SERVICE_LIST_DATA_ITEM_TYPE_VALUES!r}")
