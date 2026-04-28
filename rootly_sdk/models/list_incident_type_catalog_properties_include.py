from typing import Literal, cast

ListIncidentTypeCatalogPropertiesInclude = Literal["catalog"]

LIST_INCIDENT_TYPE_CATALOG_PROPERTIES_INCLUDE_VALUES: set[ListIncidentTypeCatalogPropertiesInclude] = {
    "catalog",
}


def check_list_incident_type_catalog_properties_include(
    value: str | None,
) -> ListIncidentTypeCatalogPropertiesInclude | None:
    if value is None:
        return None
    if value in LIST_INCIDENT_TYPE_CATALOG_PROPERTIES_INCLUDE_VALUES:
        return cast(ListIncidentTypeCatalogPropertiesInclude, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INCIDENT_TYPE_CATALOG_PROPERTIES_INCLUDE_VALUES!r}"
    )
