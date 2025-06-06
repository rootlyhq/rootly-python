from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.role_response_data_type import RoleResponseDataType

if TYPE_CHECKING:
    from ..models.role import Role


T = TypeVar("T", bound="RoleResponseData")


@_attrs_define
class RoleResponseData:
    """
    Attributes:
        id (str): Unique ID of the role
        type_ (RoleResponseDataType):
        attributes (Role):
    """

    id: str
    type_: RoleResponseDataType
    attributes: "Role"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_.value

        attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "attributes": attributes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.role import Role

        d = src_dict.copy()
        id = d.pop("id")

        type_ = RoleResponseDataType(d.pop("type"))

        attributes = Role.from_dict(d.pop("attributes"))

        role_response_data = cls(
            id=id,
            type_=type_,
            attributes=attributes,
        )

        role_response_data.additional_properties = d
        return role_response_data

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
