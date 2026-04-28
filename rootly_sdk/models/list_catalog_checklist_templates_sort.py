from typing import Literal, cast

ListCatalogChecklistTemplatesSort = Literal["-created_at", "-name", "-updated_at", "created_at", "name", "updated_at"]

LIST_CATALOG_CHECKLIST_TEMPLATES_SORT_VALUES: set[ListCatalogChecklistTemplatesSort] = {
    "-created_at",
    "-name",
    "-updated_at",
    "created_at",
    "name",
    "updated_at",
}


def check_list_catalog_checklist_templates_sort(value: str | None) -> ListCatalogChecklistTemplatesSort | None:
    if value is None:
        return None
    if value in LIST_CATALOG_CHECKLIST_TEMPLATES_SORT_VALUES:
        return cast(ListCatalogChecklistTemplatesSort, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_CATALOG_CHECKLIST_TEMPLATES_SORT_VALUES!r}")
