from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_cause_data_attributes_fields_item import NewCauseDataAttributesFieldsItem


T = TypeVar("T", bound="NewCauseDataAttributes")


@_attrs_define
class NewCauseDataAttributes:
    """
    Attributes:
        name (str): The name of the cause
        description (Union[None, Unset, str]): The description of the cause
        position (Union[None, Unset, int]): Position of the cause
        fields (Union[Unset, list['NewCauseDataAttributesFieldsItem']]): Array of field values for this cause.
    """

    name: str
    description: Union[None, Unset, str] = UNSET
    position: Union[None, Unset, int] = UNSET
    fields: Union[Unset, list["NewCauseDataAttributesFieldsItem"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        position: Union[None, Unset, int]
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()
                fields.append(fields_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if position is not UNSET:
            field_dict["position"] = position
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_cause_data_attributes_fields_item import NewCauseDataAttributesFieldsItem

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_position(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        position = _parse_position(d.pop("position", UNSET))

        fields = []
        _fields = d.pop("fields", UNSET)
        for fields_item_data in _fields or []:
            fields_item = NewCauseDataAttributesFieldsItem.from_dict(fields_item_data)

            fields.append(fields_item)

        new_cause_data_attributes = cls(
            name=name,
            description=description,
            position=position,
            fields=fields,
        )

        return new_cause_data_attributes
