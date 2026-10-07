from typing import Literal

ListCatalogEntitiesSort = Literal[
    "-created_at", "-name", "-position", "-updated_at", "created_at", "name", "position", "updated_at"
]

LIST_CATALOG_ENTITIES_SORT_VALUES: set[ListCatalogEntitiesSort] = {
    "-created_at",
    "-name",
    "-position",
    "-updated_at",
    "created_at",
    "name",
    "position",
    "updated_at",
}


def check_list_catalog_entities_sort(value: str | None) -> ListCatalogEntitiesSort | None:
    if value is None:
        return None
    if value in LIST_CATALOG_ENTITIES_SORT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_CATALOG_ENTITIES_SORT_VALUES!r}")
