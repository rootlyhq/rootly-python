from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.unassign_role_from_user_data_type import (
    UnassignRoleFromUserDataType,
    check_unassign_role_from_user_data_type,
)

if TYPE_CHECKING:
    from ..models.unassign_role_from_user_data_attributes import UnassignRoleFromUserDataAttributes


T = TypeVar("T", bound="UnassignRoleFromUserData")


@_attrs_define
class UnassignRoleFromUserData:
    """
    Attributes:
        type_ (UnassignRoleFromUserDataType):
        attributes (UnassignRoleFromUserDataAttributes):
    """

    type_: UnassignRoleFromUserDataType
    attributes: UnassignRoleFromUserDataAttributes

    def to_dict(self) -> dict[str, Any]:
        type_: str = self.type_

        attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "attributes": attributes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.unassign_role_from_user_data_attributes import UnassignRoleFromUserDataAttributes

        d = dict(src_dict)
        type_ = check_unassign_role_from_user_data_type(d.pop("type"))

        attributes = UnassignRoleFromUserDataAttributes.from_dict(d.pop("attributes"))

        unassign_role_from_user_data = cls(
            type_=type_,
            attributes=attributes,
        )

        return unassign_role_from_user_data
