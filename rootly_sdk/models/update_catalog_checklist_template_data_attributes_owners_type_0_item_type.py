from typing import Literal, cast

UpdateCatalogChecklistTemplateDataAttributesOwnersType0ItemType = Literal["field", "user"]

UPDATE_CATALOG_CHECKLIST_TEMPLATE_DATA_ATTRIBUTES_OWNERS_TYPE_0_ITEM_TYPE_VALUES: set[
    UpdateCatalogChecklistTemplateDataAttributesOwnersType0ItemType
] = {
    "field",
    "user",
}


def check_update_catalog_checklist_template_data_attributes_owners_type_0_item_type(
    value: str | None,
) -> UpdateCatalogChecklistTemplateDataAttributesOwnersType0ItemType | None:
    if value is None:
        return None
    if value in UPDATE_CATALOG_CHECKLIST_TEMPLATE_DATA_ATTRIBUTES_OWNERS_TYPE_0_ITEM_TYPE_VALUES:
        return cast(UpdateCatalogChecklistTemplateDataAttributesOwnersType0ItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_CATALOG_CHECKLIST_TEMPLATE_DATA_ATTRIBUTES_OWNERS_TYPE_0_ITEM_TYPE_VALUES!r}"
    )
