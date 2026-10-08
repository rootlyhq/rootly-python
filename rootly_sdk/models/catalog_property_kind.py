from typing import Literal

CatalogPropertyKind = Literal["reference", "text"]

CATALOG_PROPERTY_KIND_VALUES: set[CatalogPropertyKind] = {
    "reference",
    "text",
}


def check_catalog_property_kind(value: str | None) -> CatalogPropertyKind | None:
    if value is None:
        return None
    if value in CATALOG_PROPERTY_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CATALOG_PROPERTY_KIND_VALUES!r}")
