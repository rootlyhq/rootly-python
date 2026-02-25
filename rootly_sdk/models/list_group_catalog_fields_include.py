from typing import Literal, cast

ListGroupCatalogFieldsInclude = Literal["catalog"]

LIST_GROUP_CATALOG_FIELDS_INCLUDE_VALUES: set[ListGroupCatalogFieldsInclude] = {
    "catalog",
}


def check_list_group_catalog_fields_include(value: str | None) -> ListGroupCatalogFieldsInclude | None:
    if value is None:
        return None
    if value in LIST_GROUP_CATALOG_FIELDS_INCLUDE_VALUES:
        return cast(ListGroupCatalogFieldsInclude, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_GROUP_CATALOG_FIELDS_INCLUDE_VALUES!r}")
