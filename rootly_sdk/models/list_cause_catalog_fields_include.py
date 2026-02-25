from typing import Literal, cast

ListCauseCatalogFieldsInclude = Literal["catalog"]

LIST_CAUSE_CATALOG_FIELDS_INCLUDE_VALUES: set[ListCauseCatalogFieldsInclude] = {
    "catalog",
}


def check_list_cause_catalog_fields_include(value: str | None) -> ListCauseCatalogFieldsInclude | None:
    if value is None:
        return None
    if value in LIST_CAUSE_CATALOG_FIELDS_INCLUDE_VALUES:
        return cast(ListCauseCatalogFieldsInclude, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_CAUSE_CATALOG_FIELDS_INCLUDE_VALUES!r}")
