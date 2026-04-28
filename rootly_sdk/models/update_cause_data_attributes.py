from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_cause_data_attributes_properties_item import UpdateCauseDataAttributesPropertiesItem


T = TypeVar("T", bound="UpdateCauseDataAttributes")


@_attrs_define
class UpdateCauseDataAttributes:
    """
    Attributes:
        name (str | Unset): The name of the cause
        description (None | str | Unset): The description of the cause
        position (int | None | Unset): Position of the cause
        properties (list[UpdateCauseDataAttributesPropertiesItem] | Unset): Array of property values for this cause.
    """

    name: str | Unset = UNSET
    description: None | str | Unset = UNSET
    position: int | None | Unset = UNSET
    properties: list[UpdateCauseDataAttributesPropertiesItem] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        position: int | None | Unset
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        properties: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = []
            for properties_item_data in self.properties:
                properties_item = properties_item_data.to_dict()
                properties.append(properties_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if position is not UNSET:
            field_dict["position"] = position
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_cause_data_attributes_properties_item import UpdateCauseDataAttributesPropertiesItem

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_position(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        position = _parse_position(d.pop("position", UNSET))

        _properties = d.pop("properties", UNSET)
        properties: list[UpdateCauseDataAttributesPropertiesItem] | Unset = UNSET
        if _properties is not UNSET:
            properties = []
            for properties_item_data in _properties:
                properties_item = UpdateCauseDataAttributesPropertiesItem.from_dict(properties_item_data)

                properties.append(properties_item)

        update_cause_data_attributes = cls(
            name=name,
            description=description,
            position=position,
            properties=properties,
        )

        return update_cause_data_attributes
