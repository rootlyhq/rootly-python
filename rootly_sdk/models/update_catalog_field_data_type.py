from typing import Literal, cast

UpdateCatalogFieldDataType = Literal["catalog_fields"]

UPDATE_CATALOG_FIELD_DATA_TYPE_VALUES: set[UpdateCatalogFieldDataType] = {
    "catalog_fields",
}


def check_update_catalog_field_data_type(value: str | None) -> UpdateCatalogFieldDataType | None:
    if value is None:
        return None
    if value in UPDATE_CATALOG_FIELD_DATA_TYPE_VALUES:
        return cast(UpdateCatalogFieldDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_CATALOG_FIELD_DATA_TYPE_VALUES!r}")
