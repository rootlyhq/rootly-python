from typing import Literal, cast

GetCatalogEntityPropertyInclude = Literal["catalog_entity", "catalog_field"]

GET_CATALOG_ENTITY_PROPERTY_INCLUDE_VALUES: set[GetCatalogEntityPropertyInclude] = {
    "catalog_entity",
    "catalog_field",
}


def check_get_catalog_entity_property_include(value: str | None) -> GetCatalogEntityPropertyInclude | None:
    if value is None:
        return None
    if value in GET_CATALOG_ENTITY_PROPERTY_INCLUDE_VALUES:
        return cast(GetCatalogEntityPropertyInclude, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_CATALOG_ENTITY_PROPERTY_INCLUDE_VALUES!r}")
