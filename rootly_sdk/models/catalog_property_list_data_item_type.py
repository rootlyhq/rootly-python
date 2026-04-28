from typing import Literal, cast

CatalogPropertyListDataItemType = Literal["catalog_properties"]

CATALOG_PROPERTY_LIST_DATA_ITEM_TYPE_VALUES: set[CatalogPropertyListDataItemType] = {
    "catalog_properties",
}


def check_catalog_property_list_data_item_type(value: str | None) -> CatalogPropertyListDataItemType | None:
    if value is None:
        return None
    if value in CATALOG_PROPERTY_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(CatalogPropertyListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CATALOG_PROPERTY_LIST_DATA_ITEM_TYPE_VALUES!r}")
