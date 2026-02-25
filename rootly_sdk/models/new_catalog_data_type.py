from typing import Literal, cast

NewCatalogDataType = Literal["catalogs"]

NEW_CATALOG_DATA_TYPE_VALUES: set[NewCatalogDataType] = {
    "catalogs",
}


def check_new_catalog_data_type(value: str | None) -> NewCatalogDataType | None:
    if value is None:
        return None
    if value in NEW_CATALOG_DATA_TYPE_VALUES:
        return cast(NewCatalogDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_CATALOG_DATA_TYPE_VALUES!r}")
