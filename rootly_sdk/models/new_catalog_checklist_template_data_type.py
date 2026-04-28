from typing import Literal, cast

NewCatalogChecklistTemplateDataType = Literal["catalog_checklist_templates"]

NEW_CATALOG_CHECKLIST_TEMPLATE_DATA_TYPE_VALUES: set[NewCatalogChecklistTemplateDataType] = {
    "catalog_checklist_templates",
}


def check_new_catalog_checklist_template_data_type(value: str | None) -> NewCatalogChecklistTemplateDataType | None:
    if value is None:
        return None
    if value in NEW_CATALOG_CHECKLIST_TEMPLATE_DATA_TYPE_VALUES:
        return cast(NewCatalogChecklistTemplateDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_CATALOG_CHECKLIST_TEMPLATE_DATA_TYPE_VALUES!r}")
