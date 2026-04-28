from typing import Literal, cast

CatalogChecklistTemplateOwnersType0ItemType = Literal["field", "user"]

CATALOG_CHECKLIST_TEMPLATE_OWNERS_TYPE_0_ITEM_TYPE_VALUES: set[CatalogChecklistTemplateOwnersType0ItemType] = {
    "field",
    "user",
}


def check_catalog_checklist_template_owners_type_0_item_type(
    value: str | None,
) -> CatalogChecklistTemplateOwnersType0ItemType | None:
    if value is None:
        return None
    if value in CATALOG_CHECKLIST_TEMPLATE_OWNERS_TYPE_0_ITEM_TYPE_VALUES:
        return cast(CatalogChecklistTemplateOwnersType0ItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CATALOG_CHECKLIST_TEMPLATE_OWNERS_TYPE_0_ITEM_TYPE_VALUES!r}"
    )
