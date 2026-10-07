from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.update_catalog_checklist_template_data import UpdateCatalogChecklistTemplateData


T = TypeVar("T", bound="UpdateCatalogChecklistTemplate")


@_attrs_define
class UpdateCatalogChecklistTemplate:
    """
    Attributes:
        data (UpdateCatalogChecklistTemplateData):
    """

    data: UpdateCatalogChecklistTemplateData

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_catalog_checklist_template_data import UpdateCatalogChecklistTemplateData

        d = dict(src_dict)
        data = UpdateCatalogChecklistTemplateData.from_dict(d.pop("data"))

        update_catalog_checklist_template = cls(
            data=data,
        )

        return update_catalog_checklist_template
