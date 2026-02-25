from typing import Literal, cast

ListFunctionalityCatalogFieldsInclude = Literal["catalog"]

LIST_FUNCTIONALITY_CATALOG_FIELDS_INCLUDE_VALUES: set[ListFunctionalityCatalogFieldsInclude] = {
    "catalog",
}


def check_list_functionality_catalog_fields_include(value: str | None) -> ListFunctionalityCatalogFieldsInclude | None:
    if value is None:
        return None
    if value in LIST_FUNCTIONALITY_CATALOG_FIELDS_INCLUDE_VALUES:
        return cast(ListFunctionalityCatalogFieldsInclude, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_FUNCTIONALITY_CATALOG_FIELDS_INCLUDE_VALUES!r}")
