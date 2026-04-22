from typing import Literal, cast

ListServiceCatalogPropertiesSort = Literal[
    "-created_at", "-position", "-updated_at", "created_at", "position", "updated_at"
]

LIST_SERVICE_CATALOG_PROPERTIES_SORT_VALUES: set[ListServiceCatalogPropertiesSort] = {
    "-created_at",
    "-position",
    "-updated_at",
    "created_at",
    "position",
    "updated_at",
}


def check_list_service_catalog_properties_sort(value: str | None) -> ListServiceCatalogPropertiesSort | None:
    if value is None:
        return None
    if value in LIST_SERVICE_CATALOG_PROPERTIES_SORT_VALUES:
        return cast(ListServiceCatalogPropertiesSort, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_SERVICE_CATALOG_PROPERTIES_SORT_VALUES!r}")
