from typing import Literal, cast

ListServiceCatalogPropertiesInclude = Literal["catalog"]

LIST_SERVICE_CATALOG_PROPERTIES_INCLUDE_VALUES: set[ListServiceCatalogPropertiesInclude] = {
    "catalog",
}


def check_list_service_catalog_properties_include(value: str | None) -> ListServiceCatalogPropertiesInclude | None:
    if value is None:
        return None
    if value in LIST_SERVICE_CATALOG_PROPERTIES_INCLUDE_VALUES:
        return cast(ListServiceCatalogPropertiesInclude, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_SERVICE_CATALOG_PROPERTIES_INCLUDE_VALUES!r}")
