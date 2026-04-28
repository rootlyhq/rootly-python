from typing import Literal, cast

ListEnvironmentCatalogPropertiesSort = Literal[
    "-created_at", "-position", "-updated_at", "created_at", "position", "updated_at"
]

LIST_ENVIRONMENT_CATALOG_PROPERTIES_SORT_VALUES: set[ListEnvironmentCatalogPropertiesSort] = {
    "-created_at",
    "-position",
    "-updated_at",
    "created_at",
    "position",
    "updated_at",
}


def check_list_environment_catalog_properties_sort(value: str | None) -> ListEnvironmentCatalogPropertiesSort | None:
    if value is None:
        return None
    if value in LIST_ENVIRONMENT_CATALOG_PROPERTIES_SORT_VALUES:
        return cast(ListEnvironmentCatalogPropertiesSort, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_ENVIRONMENT_CATALOG_PROPERTIES_SORT_VALUES!r}")
