from typing import Literal, cast

NewCatalogChecklistTemplateDataAttributesOwnersType0ItemType = Literal["field", "user"]

NEW_CATALOG_CHECKLIST_TEMPLATE_DATA_ATTRIBUTES_OWNERS_TYPE_0_ITEM_TYPE_VALUES: set[
    NewCatalogChecklistTemplateDataAttributesOwnersType0ItemType
] = {
    "field",
    "user",
}


def check_new_catalog_checklist_template_data_attributes_owners_type_0_item_type(
    value: str | None,
) -> NewCatalogChecklistTemplateDataAttributesOwnersType0ItemType | None:
    if value is None:
        return None
    if value in NEW_CATALOG_CHECKLIST_TEMPLATE_DATA_ATTRIBUTES_OWNERS_TYPE_0_ITEM_TYPE_VALUES:
        return cast(NewCatalogChecklistTemplateDataAttributesOwnersType0ItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_CATALOG_CHECKLIST_TEMPLATE_DATA_ATTRIBUTES_OWNERS_TYPE_0_ITEM_TYPE_VALUES!r}"
    )
