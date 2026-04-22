from typing import Literal, cast

CatalogEntityChecklistResponseDataType = Literal["catalog_entity_checklists"]

CATALOG_ENTITY_CHECKLIST_RESPONSE_DATA_TYPE_VALUES: set[CatalogEntityChecklistResponseDataType] = {
    "catalog_entity_checklists",
}


def check_catalog_entity_checklist_response_data_type(
    value: str | None,
) -> CatalogEntityChecklistResponseDataType | None:
    if value is None:
        return None
    if value in CATALOG_ENTITY_CHECKLIST_RESPONSE_DATA_TYPE_VALUES:
        return cast(CatalogEntityChecklistResponseDataType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CATALOG_ENTITY_CHECKLIST_RESPONSE_DATA_TYPE_VALUES!r}"
    )
