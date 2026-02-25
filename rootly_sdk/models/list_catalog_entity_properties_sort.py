from typing import Literal, cast

ListCatalogEntityPropertiesSort = Literal["-created_at", "-updated_at", "created_at", "updated_at"]

LIST_CATALOG_ENTITY_PROPERTIES_SORT_VALUES: set[ListCatalogEntityPropertiesSort] = {
    "-created_at",
    "-updated_at",
    "created_at",
    "updated_at",
}


def check_list_catalog_entity_properties_sort(value: str | None) -> ListCatalogEntityPropertiesSort | None:
    if value is None:
        return None
    if value in LIST_CATALOG_ENTITY_PROPERTIES_SORT_VALUES:
        return cast(ListCatalogEntityPropertiesSort, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_CATALOG_ENTITY_PROPERTIES_SORT_VALUES!r}")
