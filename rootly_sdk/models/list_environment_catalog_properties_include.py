from typing import Literal, cast

ListEnvironmentCatalogPropertiesInclude = Literal["catalog"]

LIST_ENVIRONMENT_CATALOG_PROPERTIES_INCLUDE_VALUES: set[ListEnvironmentCatalogPropertiesInclude] = {
    "catalog",
}


def check_list_environment_catalog_properties_include(
    value: str | None,
) -> ListEnvironmentCatalogPropertiesInclude | None:
    if value is None:
        return None
    if value in LIST_ENVIRONMENT_CATALOG_PROPERTIES_INCLUDE_VALUES:
        return cast(ListEnvironmentCatalogPropertiesInclude, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_ENVIRONMENT_CATALOG_PROPERTIES_INCLUDE_VALUES!r}"
    )
