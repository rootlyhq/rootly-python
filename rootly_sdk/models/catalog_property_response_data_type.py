from typing import Literal, cast

CatalogPropertyResponseDataType = Literal["catalog_properties"]

CATALOG_PROPERTY_RESPONSE_DATA_TYPE_VALUES: set[CatalogPropertyResponseDataType] = {
    "catalog_properties",
}


def check_catalog_property_response_data_type(value: str | None) -> CatalogPropertyResponseDataType | None:
    if value is None:
        return None
    if value in CATALOG_PROPERTY_RESPONSE_DATA_TYPE_VALUES:
        return cast(CatalogPropertyResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CATALOG_PROPERTY_RESPONSE_DATA_TYPE_VALUES!r}")
