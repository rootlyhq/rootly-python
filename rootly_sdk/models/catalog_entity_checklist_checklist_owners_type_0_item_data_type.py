from typing import Literal, cast

CatalogEntityChecklistChecklistOwnersType0ItemDataType = Literal["catalog_entity_checklist_owners"]

CATALOG_ENTITY_CHECKLIST_CHECKLIST_OWNERS_TYPE_0_ITEM_DATA_TYPE_VALUES: set[
    CatalogEntityChecklistChecklistOwnersType0ItemDataType
] = {
    "catalog_entity_checklist_owners",
}


def check_catalog_entity_checklist_checklist_owners_type_0_item_data_type(
    value: str | None,
) -> CatalogEntityChecklistChecklistOwnersType0ItemDataType | None:
    if value is None:
        return None
    if value in CATALOG_ENTITY_CHECKLIST_CHECKLIST_OWNERS_TYPE_0_ITEM_DATA_TYPE_VALUES:
        return cast(CatalogEntityChecklistChecklistOwnersType0ItemDataType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CATALOG_ENTITY_CHECKLIST_CHECKLIST_OWNERS_TYPE_0_ITEM_DATA_TYPE_VALUES!r}"
    )
