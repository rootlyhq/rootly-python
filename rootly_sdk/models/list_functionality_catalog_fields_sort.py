from typing import Literal, cast

ListFunctionalityCatalogFieldsSort = Literal[
    "-created_at", "-position", "-updated_at", "created_at", "position", "updated_at"
]

LIST_FUNCTIONALITY_CATALOG_FIELDS_SORT_VALUES: set[ListFunctionalityCatalogFieldsSort] = {
    "-created_at",
    "-position",
    "-updated_at",
    "created_at",
    "position",
    "updated_at",
}


def check_list_functionality_catalog_fields_sort(value: str | None) -> ListFunctionalityCatalogFieldsSort | None:
    if value is None:
        return None
    if value in LIST_FUNCTIONALITY_CATALOG_FIELDS_SORT_VALUES:
        return cast(ListFunctionalityCatalogFieldsSort, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_FUNCTIONALITY_CATALOG_FIELDS_SORT_VALUES!r}")
