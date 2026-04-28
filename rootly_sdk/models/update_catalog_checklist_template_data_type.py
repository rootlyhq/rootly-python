from typing import Literal, cast

UpdateCatalogChecklistTemplateDataType = Literal["catalog_checklist_templates"]

UPDATE_CATALOG_CHECKLIST_TEMPLATE_DATA_TYPE_VALUES: set[UpdateCatalogChecklistTemplateDataType] = {
    "catalog_checklist_templates",
}


def check_update_catalog_checklist_template_data_type(
    value: str | None,
) -> UpdateCatalogChecklistTemplateDataType | None:
    if value is None:
        return None
    if value in UPDATE_CATALOG_CHECKLIST_TEMPLATE_DATA_TYPE_VALUES:
        return cast(UpdateCatalogChecklistTemplateDataType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_CATALOG_CHECKLIST_TEMPLATE_DATA_TYPE_VALUES!r}"
    )
