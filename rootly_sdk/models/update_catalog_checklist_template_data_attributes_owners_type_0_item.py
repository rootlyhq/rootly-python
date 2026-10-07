from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.update_catalog_checklist_template_data_attributes_owners_type_0_item_type import (
    UpdateCatalogChecklistTemplateDataAttributesOwnersType0ItemType,
    check_update_catalog_checklist_template_data_attributes_owners_type_0_item_type,
)

T = TypeVar("T", bound="UpdateCatalogChecklistTemplateDataAttributesOwnersType0Item")


@_attrs_define
class UpdateCatalogChecklistTemplateDataAttributesOwnersType0Item:
    """
    Attributes:
        id (str): User ID for user owners, or field key for field owners
        type_ (UpdateCatalogChecklistTemplateDataAttributesOwnersType0ItemType): Type of owner
    """

    id: str
    type_: UpdateCatalogChecklistTemplateDataAttributesOwnersType0ItemType

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_: str = self.type_

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        type_ = check_update_catalog_checklist_template_data_attributes_owners_type_0_item_type(d.pop("type"))

        update_catalog_checklist_template_data_attributes_owners_type_0_item = cls(
            id=id,
            type_=type_,
        )

        return update_catalog_checklist_template_data_attributes_owners_type_0_item
