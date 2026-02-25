from typing import Literal, cast

ListCatalogEntitiesInclude = Literal["catalog", "properties"]

LIST_CATALOG_ENTITIES_INCLUDE_VALUES: set[ListCatalogEntitiesInclude] = {
    "catalog",
    "properties",
}


def check_list_catalog_entities_include(value: str | None) -> ListCatalogEntitiesInclude | None:
    if value is None:
        return None
    if value in LIST_CATALOG_ENTITIES_INCLUDE_VALUES:
        return cast(ListCatalogEntitiesInclude, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_CATALOG_ENTITIES_INCLUDE_VALUES!r}")
