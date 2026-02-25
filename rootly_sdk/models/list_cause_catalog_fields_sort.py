from typing import Literal, cast

ListCauseCatalogFieldsSort = Literal["-created_at", "-position", "-updated_at", "created_at", "position", "updated_at"]

LIST_CAUSE_CATALOG_FIELDS_SORT_VALUES: set[ListCauseCatalogFieldsSort] = {
    "-created_at",
    "-position",
    "-updated_at",
    "created_at",
    "position",
    "updated_at",
}


def check_list_cause_catalog_fields_sort(value: str | None) -> ListCauseCatalogFieldsSort | None:
    if value is None:
        return None
    if value in LIST_CAUSE_CATALOG_FIELDS_SORT_VALUES:
        return cast(ListCauseCatalogFieldsSort, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_CAUSE_CATALOG_FIELDS_SORT_VALUES!r}")
