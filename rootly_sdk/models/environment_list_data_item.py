from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.environment_list_data_item_type import EnvironmentListDataItemType

if TYPE_CHECKING:
    from ..models.environment import Environment


T = TypeVar("T", bound="EnvironmentListDataItem")


@_attrs_define
class EnvironmentListDataItem:
    """
    Attributes:
        id (str): Unique ID of the environment
        type_ (EnvironmentListDataItemType):
        attributes (Environment):
    """

    id: str
    type_: EnvironmentListDataItemType
    attributes: "Environment"
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
        from ..models.environment import Environment

        d = src_dict.copy()
        id = d.pop("id")

        type_ = EnvironmentListDataItemType(d.pop("type"))

        attributes = Environment.from_dict(d.pop("attributes"))

        environment_list_data_item = cls(
            id=id,
            type_=type_,
            attributes=attributes,
        )

        environment_list_data_item.additional_properties = d
        return environment_list_data_item

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
