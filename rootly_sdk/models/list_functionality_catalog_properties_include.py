from typing import Literal, cast

ListFunctionalityCatalogPropertiesInclude = Literal["catalog"]

LIST_FUNCTIONALITY_CATALOG_PROPERTIES_INCLUDE_VALUES: set[ListFunctionalityCatalogPropertiesInclude] = {
    "catalog",
}


def check_list_functionality_catalog_properties_include(
    value: str | None,
) -> ListFunctionalityCatalogPropertiesInclude | None:
    if value is None:
        return None
    if value in LIST_FUNCTIONALITY_CATALOG_PROPERTIES_INCLUDE_VALUES:
        return cast(ListFunctionalityCatalogPropertiesInclude, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_FUNCTIONALITY_CATALOG_PROPERTIES_INCLUDE_VALUES!r}"
    )
