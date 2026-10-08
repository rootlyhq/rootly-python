from typing import Literal

ListCauseCatalogPropertiesInclude = Literal["catalog"]

LIST_CAUSE_CATALOG_PROPERTIES_INCLUDE_VALUES: set[ListCauseCatalogPropertiesInclude] = {
    "catalog",
}


def check_list_cause_catalog_properties_include(value: str | None) -> ListCauseCatalogPropertiesInclude | None:
    if value is None:
        return None
    if value in LIST_CAUSE_CATALOG_PROPERTIES_INCLUDE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_CAUSE_CATALOG_PROPERTIES_INCLUDE_VALUES!r}")
