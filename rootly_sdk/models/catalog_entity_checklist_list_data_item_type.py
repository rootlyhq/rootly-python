from typing import Literal, cast

CatalogEntityChecklistListDataItemType = Literal["catalog_entity_checklists"]

CATALOG_ENTITY_CHECKLIST_LIST_DATA_ITEM_TYPE_VALUES: set[CatalogEntityChecklistListDataItemType] = {
    "catalog_entity_checklists",
}


def check_catalog_entity_checklist_list_data_item_type(
    value: str | None,
) -> CatalogEntityChecklistListDataItemType | None:
    if value is None:
        return None
    if value in CATALOG_ENTITY_CHECKLIST_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(CatalogEntityChecklistListDataItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CATALOG_ENTITY_CHECKLIST_LIST_DATA_ITEM_TYPE_VALUES!r}"
    )
