from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.new_status_page_component_data_attributes_source_type import (
    NewStatusPageComponentDataAttributesSourceType,
    check_new_status_page_component_data_attributes_source_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="NewStatusPageComponentDataAttributes")


@_attrs_define
class NewStatusPageComponentDataAttributes:
    """
    Attributes:
        name (None | str | Unset): Name of the component (required for ad-hoc components; derived from the source for
            catalog-backed ones)
        description (None | str | Unset): Description of the component (ad-hoc components only)
        status_page_component_group_id (None | str | Unset): ID of the component group on the same status page
        position (int | Unset): Position of the component (within its group, or on the page's top-level list when
            ungrouped)
        source_type (NewStatusPageComponentDataAttributesSourceType | Unset): Catalog source type backing the component
        source_id (None | str | Unset): ID of the catalog source backing the component
    """

    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    status_page_component_group_id: None | str | Unset = UNSET
    position: int | Unset = UNSET
    source_type: NewStatusPageComponentDataAttributesSourceType | Unset = UNSET
    source_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        status_page_component_group_id: None | str | Unset
        if isinstance(self.status_page_component_group_id, Unset):
            status_page_component_group_id = UNSET
        else:
            status_page_component_group_id = self.status_page_component_group_id

        position = self.position

        source_type: str | Unset = UNSET
        if not isinstance(self.source_type, Unset):
            source_type = self.source_type

        source_id: None | str | Unset
        if isinstance(self.source_id, Unset):
            source_id = UNSET
        else:
            source_id = self.source_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if status_page_component_group_id is not UNSET:
            field_dict["status_page_component_group_id"] = status_page_component_group_id
        if position is not UNSET:
            field_dict["position"] = position
        if source_type is not UNSET:
            field_dict["source_type"] = source_type
        if source_id is not UNSET:
            field_dict["source_id"] = source_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_status_page_component_group_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status_page_component_group_id = _parse_status_page_component_group_id(
            d.pop("status_page_component_group_id", UNSET)
        )

        position = d.pop("position", UNSET)

        _source_type = d.pop("source_type", UNSET)
        source_type: NewStatusPageComponentDataAttributesSourceType | Unset
        if isinstance(_source_type, Unset):
            source_type = UNSET
        else:
            source_type = check_new_status_page_component_data_attributes_source_type(_source_type)

        def _parse_source_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_id = _parse_source_id(d.pop("source_id", UNSET))

        new_status_page_component_data_attributes = cls(
            name=name,
            description=description,
            status_page_component_group_id=status_page_component_group_id,
            position=position,
            source_type=source_type,
            source_id=source_id,
        )

        return new_status_page_component_data_attributes
