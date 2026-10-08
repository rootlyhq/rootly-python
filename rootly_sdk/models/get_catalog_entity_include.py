from typing import Literal

GetCatalogEntityInclude = Literal["catalog", "properties"]

GET_CATALOG_ENTITY_INCLUDE_VALUES: set[GetCatalogEntityInclude] = {
    "catalog",
    "properties",
}


def check_get_catalog_entity_include(value: str | None) -> GetCatalogEntityInclude | None:
    if value is None:
        return None
    if value in GET_CATALOG_ENTITY_INCLUDE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_CATALOG_ENTITY_INCLUDE_VALUES!r}")
