from typing import Literal, cast

ListIncidentTypeCatalogFieldsSort = Literal[
    "-created_at", "-position", "-updated_at", "created_at", "position", "updated_at"
]

LIST_INCIDENT_TYPE_CATALOG_FIELDS_SORT_VALUES: set[ListIncidentTypeCatalogFieldsSort] = {
    "-created_at",
    "-position",
    "-updated_at",
    "created_at",
    "position",
    "updated_at",
}


def check_list_incident_type_catalog_fields_sort(value: str | None) -> ListIncidentTypeCatalogFieldsSort | None:
    if value is None:
        return None
    if value in LIST_INCIDENT_TYPE_CATALOG_FIELDS_SORT_VALUES:
        return cast(ListIncidentTypeCatalogFieldsSort, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_INCIDENT_TYPE_CATALOG_FIELDS_SORT_VALUES!r}")
