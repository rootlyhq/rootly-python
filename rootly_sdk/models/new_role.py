from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.new_role_data import NewRoleData


T = TypeVar("T", bound="NewRole")


@_attrs_define
class NewRole:
    """
    Attributes:
        data (NewRoleData):
    """

    data: NewRoleData

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
        from ..models.new_role_data import NewRoleData

        d = dict(src_dict)
        data = NewRoleData.from_dict(d.pop("data"))

        new_role = cls(
            data=data,
        )

        return new_role
