from typing import Literal, cast

ListCatalogFieldsSort = Literal["-created_at", "-position", "-updated_at", "created_at", "position", "updated_at"]

LIST_CATALOG_FIELDS_SORT_VALUES: set[ListCatalogFieldsSort] = {
    "-created_at",
    "-position",
    "-updated_at",
    "created_at",
    "position",
    "updated_at",
}


def check_list_catalog_fields_sort(value: str | None) -> ListCatalogFieldsSort | None:
    if value is None:
        return None
    if value in LIST_CATALOG_FIELDS_SORT_VALUES:
        return cast(ListCatalogFieldsSort, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_CATALOG_FIELDS_SORT_VALUES!r}")
