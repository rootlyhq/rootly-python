from typing import Literal, cast

CatalogChecklistTemplateResponseDataType = Literal["catalog_checklist_templates"]

CATALOG_CHECKLIST_TEMPLATE_RESPONSE_DATA_TYPE_VALUES: set[CatalogChecklistTemplateResponseDataType] = {
    "catalog_checklist_templates",
}


def check_catalog_checklist_template_response_data_type(
    value: str | None,
) -> CatalogChecklistTemplateResponseDataType | None:
    if value is None:
        return None
    if value in CATALOG_CHECKLIST_TEMPLATE_RESPONSE_DATA_TYPE_VALUES:
        return cast(CatalogChecklistTemplateResponseDataType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CATALOG_CHECKLIST_TEMPLATE_RESPONSE_DATA_TYPE_VALUES!r}"
    )
