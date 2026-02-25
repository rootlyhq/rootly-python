from typing import Literal, cast

CatalogResponseDataType = Literal["catalogs"]

CATALOG_RESPONSE_DATA_TYPE_VALUES: set[CatalogResponseDataType] = {
    "catalogs",
}


def check_catalog_response_data_type(value: str | None) -> CatalogResponseDataType | None:
    if value is None:
        return None
    if value in CATALOG_RESPONSE_DATA_TYPE_VALUES:
        return cast(CatalogResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CATALOG_RESPONSE_DATA_TYPE_VALUES!r}")
