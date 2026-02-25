from typing import Literal, cast

ListServiceCatalogFieldsSort = Literal[
    "-created_at", "-position", "-updated_at", "created_at", "position", "updated_at"
]

LIST_SERVICE_CATALOG_FIELDS_SORT_VALUES: set[ListServiceCatalogFieldsSort] = {
    "-created_at",
    "-position",
    "-updated_at",
    "created_at",
    "position",
    "updated_at",
}


def check_list_service_catalog_fields_sort(value: str | None) -> ListServiceCatalogFieldsSort | None:
    if value is None:
        return None
    if value in LIST_SERVICE_CATALOG_FIELDS_SORT_VALUES:
        return cast(ListServiceCatalogFieldsSort, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_SERVICE_CATALOG_FIELDS_SORT_VALUES!r}")
