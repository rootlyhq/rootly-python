from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.shift_list_data_item_type import ShiftListDataItemType, check_shift_list_data_item_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.shift import Shift
    from ..models.shift_relationships import ShiftRelationships


T = TypeVar("T", bound="ShiftListDataItem")


@_attrs_define
class ShiftListDataItem:
    """
    Attributes:
        id (str): Unique ID of the shift
        type_ (ShiftListDataItemType):
        attributes (Shift):
        relationships (Union[Unset, ShiftRelationships]):
    """

    id: str
    type_: ShiftListDataItemType
    attributes: "Shift"
    relationships: Union[Unset, "ShiftRelationships"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_: str = self.type_

        attributes = self.attributes.to_dict()

        relationships: Union[Unset, dict[str, Any]] = UNSET
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
        from ..models.shift import Shift
        from ..models.shift_relationships import ShiftRelationships

        d = dict(src_dict)
        id = d.pop("id")

        type_ = check_shift_list_data_item_type(d.pop("type"))

        attributes = Shift.from_dict(d.pop("attributes"))

        _relationships = d.pop("relationships", UNSET)
        relationships: Union[Unset, ShiftRelationships]
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = ShiftRelationships.from_dict(_relationships)

        shift_list_data_item = cls(
            id=id,
            type_=type_,
            attributes=attributes,
            relationships=relationships,
        )

        shift_list_data_item.additional_properties = d
        return shift_list_data_item

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
