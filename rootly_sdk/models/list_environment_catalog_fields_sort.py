from typing import Literal, cast

ListEnvironmentCatalogFieldsSort = Literal[
    "-created_at", "-position", "-updated_at", "created_at", "position", "updated_at"
]

LIST_ENVIRONMENT_CATALOG_FIELDS_SORT_VALUES: set[ListEnvironmentCatalogFieldsSort] = {
    "-created_at",
    "-position",
    "-updated_at",
    "created_at",
    "position",
    "updated_at",
}


def check_list_environment_catalog_fields_sort(value: str | None) -> ListEnvironmentCatalogFieldsSort | None:
    if value is None:
        return None
    if value in LIST_ENVIRONMENT_CATALOG_FIELDS_SORT_VALUES:
        return cast(ListEnvironmentCatalogFieldsSort, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_ENVIRONMENT_CATALOG_FIELDS_SORT_VALUES!r}")
