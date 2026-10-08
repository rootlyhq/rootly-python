from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.new_communications_template_data import NewCommunicationsTemplateData


T = TypeVar("T", bound="NewCommunicationsTemplate")


@_attrs_define
class NewCommunicationsTemplate:
    """
    Attributes:
        data (NewCommunicationsTemplateData):
    """

    data: NewCommunicationsTemplateData

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
        from ..models.new_communications_template_data import NewCommunicationsTemplateData

        d = dict(src_dict)
        data = NewCommunicationsTemplateData.from_dict(d.pop("data"))

        new_communications_template = cls(
            data=data,
        )

        return new_communications_template
