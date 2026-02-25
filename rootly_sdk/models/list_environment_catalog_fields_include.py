from typing import Literal, cast

ListEnvironmentCatalogFieldsInclude = Literal["catalog"]

LIST_ENVIRONMENT_CATALOG_FIELDS_INCLUDE_VALUES: set[ListEnvironmentCatalogFieldsInclude] = {
    "catalog",
}


def check_list_environment_catalog_fields_include(value: str | None) -> ListEnvironmentCatalogFieldsInclude | None:
    if value is None:
        return None
    if value in LIST_ENVIRONMENT_CATALOG_FIELDS_INCLUDE_VALUES:
        return cast(ListEnvironmentCatalogFieldsInclude, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_ENVIRONMENT_CATALOG_FIELDS_INCLUDE_VALUES!r}")
