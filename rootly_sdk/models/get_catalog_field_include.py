from typing import Literal, cast

GetCatalogFieldInclude = Literal["catalog"]

GET_CATALOG_FIELD_INCLUDE_VALUES: set[GetCatalogFieldInclude] = {
    "catalog",
}


def check_get_catalog_field_include(value: str | None) -> GetCatalogFieldInclude | None:
    if value is None:
        return None
    if value in GET_CATALOG_FIELD_INCLUDE_VALUES:
        return cast(GetCatalogFieldInclude, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_CATALOG_FIELD_INCLUDE_VALUES!r}")
