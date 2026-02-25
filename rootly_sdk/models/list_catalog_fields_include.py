from typing import Literal, cast

ListCatalogFieldsInclude = Literal["catalog"]

LIST_CATALOG_FIELDS_INCLUDE_VALUES: set[ListCatalogFieldsInclude] = {
    "catalog",
}


def check_list_catalog_fields_include(value: str | None) -> ListCatalogFieldsInclude | None:
    if value is None:
        return None
    if value in LIST_CATALOG_FIELDS_INCLUDE_VALUES:
        return cast(ListCatalogFieldsInclude, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_CATALOG_FIELDS_INCLUDE_VALUES!r}")
