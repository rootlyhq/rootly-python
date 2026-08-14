from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.assign_role_to_user_data import AssignRoleToUserData


T = TypeVar("T", bound="AssignRoleToUser")


@_attrs_define
class AssignRoleToUser:
    """
    Attributes:
        data (AssignRoleToUserData):
    """

    data: "AssignRoleToUserData"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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

        assign_role_to_user.additional_properties = d
        return assign_role_to_user

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
