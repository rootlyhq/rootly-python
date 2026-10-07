from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.unassign_role_from_user_data import UnassignRoleFromUserData


T = TypeVar("T", bound="UnassignRoleFromUser")


@_attrs_define
class UnassignRoleFromUser:
    """
    Attributes:
        data (UnassignRoleFromUserData):
    """

    data: UnassignRoleFromUserData

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
        from ..models.unassign_role_from_user_data import UnassignRoleFromUserData

        d = dict(src_dict)
        data = UnassignRoleFromUserData.from_dict(d.pop("data"))

        unassign_role_from_user = cls(
            data=data,
        )

        return unassign_role_from_user
