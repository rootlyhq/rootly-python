from typing import Literal, cast

ListIncidentTypeCatalogPropertiesSort = Literal[
    "-created_at", "-position", "-updated_at", "created_at", "position", "updated_at"
]

LIST_INCIDENT_TYPE_CATALOG_PROPERTIES_SORT_VALUES: set[ListIncidentTypeCatalogPropertiesSort] = {
    "-created_at",
    "-position",
    "-updated_at",
    "created_at",
    "position",
    "updated_at",
}


def check_list_incident_type_catalog_properties_sort(value: str | None) -> ListIncidentTypeCatalogPropertiesSort | None:
    if value is None:
        return None
    if value in LIST_INCIDENT_TYPE_CATALOG_PROPERTIES_SORT_VALUES:
        return cast(ListIncidentTypeCatalogPropertiesSort, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INCIDENT_TYPE_CATALOG_PROPERTIES_SORT_VALUES!r}"
    )
