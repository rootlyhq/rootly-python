from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.new_communications_group_data import NewCommunicationsGroupData


T = TypeVar("T", bound="NewCommunicationsGroup")


@_attrs_define
class NewCommunicationsGroup:
    """
    Attributes:
        data (NewCommunicationsGroupData):
    """

    data: NewCommunicationsGroupData

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
        from ..models.new_communications_group_data import NewCommunicationsGroupData

        d = dict(src_dict)
        data = NewCommunicationsGroupData.from_dict(d.pop("data"))

        new_communications_group = cls(
            data=data,
        )

        return new_communications_group
