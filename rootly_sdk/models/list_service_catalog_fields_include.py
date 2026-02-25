from typing import Literal, cast

ListServiceCatalogFieldsInclude = Literal["catalog"]

LIST_SERVICE_CATALOG_FIELDS_INCLUDE_VALUES: set[ListServiceCatalogFieldsInclude] = {
    "catalog",
}


def check_list_service_catalog_fields_include(value: str | None) -> ListServiceCatalogFieldsInclude | None:
    if value is None:
        return None
    if value in LIST_SERVICE_CATALOG_FIELDS_INCLUDE_VALUES:
        return cast(ListServiceCatalogFieldsInclude, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_SERVICE_CATALOG_FIELDS_INCLUDE_VALUES!r}")
