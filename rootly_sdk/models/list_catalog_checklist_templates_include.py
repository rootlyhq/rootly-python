from typing import Literal, cast

ListCatalogChecklistTemplatesInclude = Literal["template_fields", "template_owners"]

LIST_CATALOG_CHECKLIST_TEMPLATES_INCLUDE_VALUES: set[ListCatalogChecklistTemplatesInclude] = {
    "template_fields",
    "template_owners",
}


def check_list_catalog_checklist_templates_include(value: str | None) -> ListCatalogChecklistTemplatesInclude | None:
    if value is None:
        return None
    if value in LIST_CATALOG_CHECKLIST_TEMPLATES_INCLUDE_VALUES:
        return cast(ListCatalogChecklistTemplatesInclude, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_CATALOG_CHECKLIST_TEMPLATES_INCLUDE_VALUES!r}")
