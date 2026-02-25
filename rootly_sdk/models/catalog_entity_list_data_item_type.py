from typing import Literal, cast

CatalogEntityListDataItemType = Literal["catalog_entities"]

CATALOG_ENTITY_LIST_DATA_ITEM_TYPE_VALUES: set[CatalogEntityListDataItemType] = {
    "catalog_entities",
}


def check_catalog_entity_list_data_item_type(value: str | None) -> CatalogEntityListDataItemType | None:
    if value is None:
        return None
    if value in CATALOG_ENTITY_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(CatalogEntityListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CATALOG_ENTITY_LIST_DATA_ITEM_TYPE_VALUES!r}")
