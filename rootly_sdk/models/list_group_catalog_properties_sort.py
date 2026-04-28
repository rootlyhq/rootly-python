from typing import Literal, cast

ListGroupCatalogPropertiesSort = Literal[
    "-created_at", "-position", "-updated_at", "created_at", "position", "updated_at"
]

LIST_GROUP_CATALOG_PROPERTIES_SORT_VALUES: set[ListGroupCatalogPropertiesSort] = {
    "-created_at",
    "-position",
    "-updated_at",
    "created_at",
    "position",
    "updated_at",
}


def check_list_group_catalog_properties_sort(value: str | None) -> ListGroupCatalogPropertiesSort | None:
    if value is None:
        return None
    if value in LIST_GROUP_CATALOG_PROPERTIES_SORT_VALUES:
        return cast(ListGroupCatalogPropertiesSort, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_GROUP_CATALOG_PROPERTIES_SORT_VALUES!r}")
