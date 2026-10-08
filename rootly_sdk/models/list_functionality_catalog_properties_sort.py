from typing import Literal

ListFunctionalityCatalogPropertiesSort = Literal[
    "-created_at", "-position", "-updated_at", "created_at", "position", "updated_at"
]

LIST_FUNCTIONALITY_CATALOG_PROPERTIES_SORT_VALUES: set[ListFunctionalityCatalogPropertiesSort] = {
    "-created_at",
    "-position",
    "-updated_at",
    "created_at",
    "position",
    "updated_at",
}


def check_list_functionality_catalog_properties_sort(
    value: str | None,
) -> ListFunctionalityCatalogPropertiesSort | None:
    if value is None:
        return None
    if value in LIST_FUNCTIONALITY_CATALOG_PROPERTIES_SORT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_FUNCTIONALITY_CATALOG_PROPERTIES_SORT_VALUES!r}"
    )
