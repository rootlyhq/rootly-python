from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.assign_role_to_user_data_type import AssignRoleToUserDataType, check_assign_role_to_user_data_type

if TYPE_CHECKING:
    from ..models.assign_role_to_user_data_attributes import AssignRoleToUserDataAttributes


T = TypeVar("T", bound="AssignRoleToUserData")


@_attrs_define
class AssignRoleToUserData:
    """
    Attributes:
        type_ (AssignRoleToUserDataType):
        attributes (AssignRoleToUserDataAttributes):
    """

    type_: AssignRoleToUserDataType
    attributes: "AssignRoleToUserDataAttributes"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str = self.type_

        attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "attributes": attributes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.assign_role_to_user_data_attributes import AssignRoleToUserDataAttributes

        d = dict(src_dict)
        type_ = check_assign_role_to_user_data_type(d.pop("type"))

        attributes = AssignRoleToUserDataAttributes.from_dict(d.pop("attributes"))

        assign_role_to_user_data = cls(
            type_=type_,
            attributes=attributes,
        )

        assign_role_to_user_data.additional_properties = d
        return assign_role_to_user_data

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
