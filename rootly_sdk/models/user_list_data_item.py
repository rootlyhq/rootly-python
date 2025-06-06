from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_list_data_item_type import UserListDataItemType

if TYPE_CHECKING:
    from ..models.user import User


T = TypeVar("T", bound="UserListDataItem")


@_attrs_define
class UserListDataItem:
    """
    Attributes:
        id (str): Unique ID of the user
        type_ (UserListDataItemType):
        attributes (User):
    """

    id: str
    type_: UserListDataItemType
    attributes: "User"
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
        from ..models.user import User

        d = src_dict.copy()
        id = d.pop("id")

        type_ = UserListDataItemType(d.pop("type"))

        attributes = User.from_dict(d.pop("attributes"))

        user_list_data_item = cls(
            id=id,
            type_=type_,
            attributes=attributes,
        )

        user_list_data_item.additional_properties = d
        return user_list_data_item

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
