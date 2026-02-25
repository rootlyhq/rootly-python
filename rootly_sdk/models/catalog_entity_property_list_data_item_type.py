from typing import Literal, cast

CatalogEntityPropertyListDataItemType = Literal["catalog_entity_properties"]

CATALOG_ENTITY_PROPERTY_LIST_DATA_ITEM_TYPE_VALUES: set[CatalogEntityPropertyListDataItemType] = {
    "catalog_entity_properties",
}


def check_catalog_entity_property_list_data_item_type(value: str | None) -> CatalogEntityPropertyListDataItemType | None:
    if value is None:
        return None
    if value in CATALOG_ENTITY_PROPERTY_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(CatalogEntityPropertyListDataItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CATALOG_ENTITY_PROPERTY_LIST_DATA_ITEM_TYPE_VALUES!r}"
    )
