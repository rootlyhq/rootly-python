from typing import Literal, cast

CatalogEntityChecklistChecklistFieldsType0ItemDataType = Literal["catalog_entity_checklist_fields"]

CATALOG_ENTITY_CHECKLIST_CHECKLIST_FIELDS_TYPE_0_ITEM_DATA_TYPE_VALUES: set[
    CatalogEntityChecklistChecklistFieldsType0ItemDataType
] = {
    "catalog_entity_checklist_fields",
}


def check_catalog_entity_checklist_checklist_fields_type_0_item_data_type(
    value: str | None,
) -> CatalogEntityChecklistChecklistFieldsType0ItemDataType | None:
    if value is None:
        return None
    if value in CATALOG_ENTITY_CHECKLIST_CHECKLIST_FIELDS_TYPE_0_ITEM_DATA_TYPE_VALUES:
        return cast(CatalogEntityChecklistChecklistFieldsType0ItemDataType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CATALOG_ENTITY_CHECKLIST_CHECKLIST_FIELDS_TYPE_0_ITEM_DATA_TYPE_VALUES!r}"
    )
