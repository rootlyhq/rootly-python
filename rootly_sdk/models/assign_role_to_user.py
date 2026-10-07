from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.assign_role_to_user_data import AssignRoleToUserData


T = TypeVar("T", bound="AssignRoleToUser")


@_attrs_define
class AssignRoleToUser:
    """
    Attributes:
        data (AssignRoleToUserData):
    """

    data: AssignRoleToUserData

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
        from ..models.assign_role_to_user_data import AssignRoleToUserData

        d = dict(src_dict)
        data = AssignRoleToUserData.from_dict(d.pop("data"))

        assign_role_to_user = cls(
            data=data,
        )

        return assign_role_to_user
