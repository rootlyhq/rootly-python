from typing import Literal, cast

CatalogFieldListDataItemType = Literal["catalog_fields"]

CATALOG_FIELD_LIST_DATA_ITEM_TYPE_VALUES: set[CatalogFieldListDataItemType] = {
    "catalog_fields",
}


def check_catalog_field_list_data_item_type(value: str | None) -> CatalogFieldListDataItemType | None:
    if value is None:
        return None
    if value in CATALOG_FIELD_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(CatalogFieldListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CATALOG_FIELD_LIST_DATA_ITEM_TYPE_VALUES!r}")
