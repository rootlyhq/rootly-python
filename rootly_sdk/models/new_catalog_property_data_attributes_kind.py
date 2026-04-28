from typing import Literal, cast

NewCatalogPropertyDataAttributesKind = Literal[
    "boolean", "cause", "environment", "functionality", "group", "incident_type", "reference", "service", "text", "user"
]

NEW_CATALOG_PROPERTY_DATA_ATTRIBUTES_KIND_VALUES: set[NewCatalogPropertyDataAttributesKind] = {
    "boolean",
    "cause",
    "environment",
    "functionality",
    "group",
    "incident_type",
    "reference",
    "service",
    "text",
    "user",
}


def check_new_catalog_property_data_attributes_kind(value: str | None) -> NewCatalogPropertyDataAttributesKind | None:
    if value is None:
        return None
    if value in NEW_CATALOG_PROPERTY_DATA_ATTRIBUTES_KIND_VALUES:
        return cast(NewCatalogPropertyDataAttributesKind, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_CATALOG_PROPERTY_DATA_ATTRIBUTES_KIND_VALUES!r}")
