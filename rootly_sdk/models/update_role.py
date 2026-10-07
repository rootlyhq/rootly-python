from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.update_role_data import UpdateRoleData


T = TypeVar("T", bound="UpdateRole")


@_attrs_define
class UpdateRole:
    """
    Attributes:
        data (UpdateRoleData):
    """

    data: UpdateRoleData

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
        from ..models.update_role_data import UpdateRoleData

        d = dict(src_dict)
        data = UpdateRoleData.from_dict(d.pop("data"))

        update_role = cls(
            data=data,
        )

        return update_role
