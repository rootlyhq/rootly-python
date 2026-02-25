from typing import Literal, cast

NewCatalogFieldDataAttributesKind = Literal[
    "boolean", "cause", "environment", "functionality", "group", "incident_type", "reference", "service", "text", "user"
]

NEW_CATALOG_FIELD_DATA_ATTRIBUTES_KIND_VALUES: set[NewCatalogFieldDataAttributesKind] = {
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


def check_new_catalog_field_data_attributes_kind(value: str | None) -> NewCatalogFieldDataAttributesKind | None:
    if value is None:
        return None
    if value in NEW_CATALOG_FIELD_DATA_ATTRIBUTES_KIND_VALUES:
        return cast(NewCatalogFieldDataAttributesKind, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_CATALOG_FIELD_DATA_ATTRIBUTES_KIND_VALUES!r}")
