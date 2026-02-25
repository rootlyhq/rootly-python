from typing import Literal, cast

ListCatalogEntityPropertiesInclude = Literal["catalog_entity", "catalog_field"]

LIST_CATALOG_ENTITY_PROPERTIES_INCLUDE_VALUES: set[ListCatalogEntityPropertiesInclude] = {
    "catalog_entity",
    "catalog_field",
}


def check_list_catalog_entity_properties_include(value: str | None) -> ListCatalogEntityPropertiesInclude | None:
    if value is None:
        return None
    if value in LIST_CATALOG_ENTITY_PROPERTIES_INCLUDE_VALUES:
        return cast(ListCatalogEntityPropertiesInclude, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_CATALOG_ENTITY_PROPERTIES_INCLUDE_VALUES!r}")
