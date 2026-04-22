from typing import Literal, cast

NewCatalogPropertyDataAttributesCatalogType = Literal[
    "catalog", "cause", "environment", "functionality", "incident_type", "service", "team"
]

NEW_CATALOG_PROPERTY_DATA_ATTRIBUTES_CATALOG_TYPE_VALUES: set[NewCatalogPropertyDataAttributesCatalogType] = {
    "catalog",
    "cause",
    "environment",
    "functionality",
    "incident_type",
    "service",
    "team",
}


def check_new_catalog_property_data_attributes_catalog_type(
    value: str | None,
) -> NewCatalogPropertyDataAttributesCatalogType | None:
    if value is None:
        return None
    if value in NEW_CATALOG_PROPERTY_DATA_ATTRIBUTES_CATALOG_TYPE_VALUES:
        return cast(NewCatalogPropertyDataAttributesCatalogType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_CATALOG_PROPERTY_DATA_ATTRIBUTES_CATALOG_TYPE_VALUES!r}"
    )
