from typing import Literal, cast

ListCauseCatalogPropertiesSort = Literal[
    "-created_at", "-position", "-updated_at", "created_at", "position", "updated_at"
]

LIST_CAUSE_CATALOG_PROPERTIES_SORT_VALUES: set[ListCauseCatalogPropertiesSort] = {
    "-created_at",
    "-position",
    "-updated_at",
    "created_at",
    "position",
    "updated_at",
}


def check_list_cause_catalog_properties_sort(value: str | None) -> ListCauseCatalogPropertiesSort | None:
    if value is None:
        return None
    if value in LIST_CAUSE_CATALOG_PROPERTIES_SORT_VALUES:
        return cast(ListCauseCatalogPropertiesSort, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_CAUSE_CATALOG_PROPERTIES_SORT_VALUES!r}")
