from typing import Literal, cast

CatalogChecklistTemplateListDataItemType = Literal["catalog_checklist_templates"]

CATALOG_CHECKLIST_TEMPLATE_LIST_DATA_ITEM_TYPE_VALUES: set[CatalogChecklistTemplateListDataItemType] = {
    "catalog_checklist_templates",
}


def check_catalog_checklist_template_list_data_item_type(
    value: str | None,
) -> CatalogChecklistTemplateListDataItemType | None:
    if value is None:
        return None
    if value in CATALOG_CHECKLIST_TEMPLATE_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(CatalogChecklistTemplateListDataItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CATALOG_CHECKLIST_TEMPLATE_LIST_DATA_ITEM_TYPE_VALUES!r}"
    )
