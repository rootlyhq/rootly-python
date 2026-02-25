from typing import Literal, cast

CatalogFieldResponseDataType = Literal["catalog_fields"]

CATALOG_FIELD_RESPONSE_DATA_TYPE_VALUES: set[CatalogFieldResponseDataType] = {
    "catalog_fields",
}


def check_catalog_field_response_data_type(value: str | None) -> CatalogFieldResponseDataType | None:
    if value is None:
        return None
    if value in CATALOG_FIELD_RESPONSE_DATA_TYPE_VALUES:
        return cast(CatalogFieldResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CATALOG_FIELD_RESPONSE_DATA_TYPE_VALUES!r}")
