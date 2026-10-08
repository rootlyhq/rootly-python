from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.new_catalog_checklist_template_data import NewCatalogChecklistTemplateData


T = TypeVar("T", bound="NewCatalogChecklistTemplate")


@_attrs_define
class NewCatalogChecklistTemplate:
    """
    Attributes:
        data (NewCatalogChecklistTemplateData):
    """

    data: NewCatalogChecklistTemplateData

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
        from ..models.new_catalog_checklist_template_data import NewCatalogChecklistTemplateData

        d = dict(src_dict)
        data = NewCatalogChecklistTemplateData.from_dict(d.pop("data"))

        new_catalog_checklist_template = cls(
            data=data,
        )

        return new_catalog_checklist_template
