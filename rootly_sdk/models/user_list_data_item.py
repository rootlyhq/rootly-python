from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_list_data_item_type import UserListDataItemType, check_user_list_data_item_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user import User
    from ..models.user_relationships import UserRelationships


T = TypeVar("T", bound="UserListDataItem")


@_attrs_define
class UserListDataItem:
    """
    Attributes:
        id (str): Unique ID of the user
        type_ (UserListDataItemType):
        attributes (User):
        relationships (Union[Unset, UserRelationships]):
    """

    id: str
    type_: UserListDataItemType
    attributes: "User"
    relationships: Union[Unset, "UserRelationships"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_: str = self.type_

        attributes = self.attributes.to_dict()

        relationships: Unset | dict[str, Any] = UNSET
        if not isinstance(self.relationships, Unset):
            relationships = self.relationships.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "attributes": attributes,
            }
        )
        if relationships is not UNSET:
            field_dict["relationships"] = relationships

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user import User
        from ..models.user_relationships import UserRelationships

        d = dict(src_dict)
        id = d.pop("id")

        type_ = check_user_list_data_item_type(d.pop("type"))

        attributes = User.from_dict(d.pop("attributes"))

        _relationships = d.pop("relationships", UNSET)
        relationships: Unset | UserRelationships
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = UserRelationships.from_dict(_relationships)

        user_list_data_item = cls(
            id=id,
            type_=type_,
            attributes=attributes,
            relationships=relationships,
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
