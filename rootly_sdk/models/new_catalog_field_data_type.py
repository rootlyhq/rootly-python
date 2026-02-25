from typing import Literal, cast

NewCatalogFieldDataType = Literal["catalog_fields"]

NEW_CATALOG_FIELD_DATA_TYPE_VALUES: set[NewCatalogFieldDataType] = {
    "catalog_fields",
}


def check_new_catalog_field_data_type(value: str | None) -> NewCatalogFieldDataType | None:
    if value is None:
        return None
    if value in NEW_CATALOG_FIELD_DATA_TYPE_VALUES:
        return cast(NewCatalogFieldDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_CATALOG_FIELD_DATA_TYPE_VALUES!r}")
