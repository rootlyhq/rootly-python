from typing import Literal, cast

ListGroupCatalogPropertiesInclude = Literal["catalog"]

LIST_GROUP_CATALOG_PROPERTIES_INCLUDE_VALUES: set[ListGroupCatalogPropertiesInclude] = {
    "catalog",
}


def check_list_group_catalog_properties_include(value: str | None) -> ListGroupCatalogPropertiesInclude | None:
    if value is None:
        return None
    if value in LIST_GROUP_CATALOG_PROPERTIES_INCLUDE_VALUES:
        return cast(ListGroupCatalogPropertiesInclude, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_GROUP_CATALOG_PROPERTIES_INCLUDE_VALUES!r}")
