from typing import Literal, cast

UpdateCatalogEntityDataType = Literal["catalog_entities"]

UPDATE_CATALOG_ENTITY_DATA_TYPE_VALUES: set[UpdateCatalogEntityDataType] = {
    "catalog_entities",
}


def check_update_catalog_entity_data_type(value: str | None) -> UpdateCatalogEntityDataType | None:
    if value is None:
        return None
    if value in UPDATE_CATALOG_ENTITY_DATA_TYPE_VALUES:
        return cast(UpdateCatalogEntityDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_CATALOG_ENTITY_DATA_TYPE_VALUES!r}")
