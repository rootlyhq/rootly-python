from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.update_communications_type_data import UpdateCommunicationsTypeData


T = TypeVar("T", bound="UpdateCommunicationsType")


@_attrs_define
class UpdateCommunicationsType:
    """
    Attributes:
        data (UpdateCommunicationsTypeData):
    """

    data: UpdateCommunicationsTypeData

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
        from ..models.update_communications_type_data import UpdateCommunicationsTypeData

        d = dict(src_dict)
        data = UpdateCommunicationsTypeData.from_dict(d.pop("data"))

        update_communications_type = cls(
            data=data,
        )

        return update_communications_type
