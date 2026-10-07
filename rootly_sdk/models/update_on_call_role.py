from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.update_on_call_role_data import UpdateOnCallRoleData


T = TypeVar("T", bound="UpdateOnCallRole")


@_attrs_define
class UpdateOnCallRole:
    """
    Attributes:
        data (UpdateOnCallRoleData):
    """

    data: UpdateOnCallRoleData

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
        from ..models.update_on_call_role_data import UpdateOnCallRoleData

        d = dict(src_dict)
        data = UpdateOnCallRoleData.from_dict(d.pop("data"))

        update_on_call_role = cls(
            data=data,
        )

        return update_on_call_role
