from typing import Literal, cast

ListGroupCatalogFieldsSort = Literal["-created_at", "-position", "-updated_at", "created_at", "position", "updated_at"]

LIST_GROUP_CATALOG_FIELDS_SORT_VALUES: set[ListGroupCatalogFieldsSort] = {
    "-created_at",
    "-position",
    "-updated_at",
    "created_at",
    "position",
    "updated_at",
}


def check_list_group_catalog_fields_sort(value: str | None) -> ListGroupCatalogFieldsSort | None:
    if value is None:
        return None
    if value in LIST_GROUP_CATALOG_FIELDS_SORT_VALUES:
        return cast(ListGroupCatalogFieldsSort, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_GROUP_CATALOG_FIELDS_SORT_VALUES!r}")
