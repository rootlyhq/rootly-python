from typing import Literal, cast

ListIncidentTypeCatalogFieldsInclude = Literal["catalog"]

LIST_INCIDENT_TYPE_CATALOG_FIELDS_INCLUDE_VALUES: set[ListIncidentTypeCatalogFieldsInclude] = {
    "catalog",
}


def check_list_incident_type_catalog_fields_include(value: str | None) -> ListIncidentTypeCatalogFieldsInclude | None:
    if value is None:
        return None
    if value in LIST_INCIDENT_TYPE_CATALOG_FIELDS_INCLUDE_VALUES:
        return cast(ListIncidentTypeCatalogFieldsInclude, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_INCIDENT_TYPE_CATALOG_FIELDS_INCLUDE_VALUES!r}")
