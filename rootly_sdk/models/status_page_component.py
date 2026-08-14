import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.status_page_component_status import StatusPageComponentStatus, check_status_page_component_status
from ..types import UNSET, Unset

T = TypeVar("T", bound="StatusPageComponent")


@_attrs_define
class StatusPageComponent:
    """
    Attributes:
        status_page_id (str):
        position (int): Position of the component
        created_at (datetime.datetime): Date of creation
        updated_at (datetime.datetime): Date of last update
        status_page_component_group_id (Union[None, Unset, str]): ID of the component group the component belongs to
        name (Union[None, Unset, str]): Name of the component (derived from the source for catalog-backed components)
        description (Union[None, Unset, str]): Description of the component (derived from the source for catalog-backed
            components)
        source_type (Union[None, Unset, str]): Catalog source type backing the component (null for ad-hoc components)
        source_id (Union[None, Unset, str]): ID of the catalog source backing the component (null for ad-hoc components)
        status (Union[Unset, StatusPageComponentStatus]): Latest recorded status of the component
    """

    status_page_id: str
    position: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    status_page_component_group_id: None | Unset | str = UNSET
    name: None | Unset | str = UNSET
    description: None | Unset | str = UNSET
    source_type: None | Unset | str = UNSET
    source_id: None | Unset | str = UNSET
    status: Unset | StatusPageComponentStatus = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status_page_id = self.status_page_id

        position = self.position

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        status_page_component_group_id: None | Unset | str
        if isinstance(self.status_page_component_group_id, Unset):
            status_page_component_group_id = UNSET
        else:
            status_page_component_group_id = self.status_page_component_group_id

        name: None | Unset | str
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        source_type: None | Unset | str
        if isinstance(self.source_type, Unset):
            source_type = UNSET
        else:
            source_type = self.source_type

        source_id: None | Unset | str
        if isinstance(self.source_id, Unset):
            source_id = UNSET
        else:
            source_id = self.source_id

        status: Unset | str = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status_page_id": status_page_id,
                "position": position,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if status_page_component_group_id is not UNSET:
            field_dict["status_page_component_group_id"] = status_page_component_group_id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if source_type is not UNSET:
            field_dict["source_type"] = source_type
        if source_id is not UNSET:
            field_dict["source_id"] = source_id
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status_page_id = d.pop("status_page_id")

        position = d.pop("position")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        def _parse_status_page_component_group_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        status_page_component_group_id = _parse_status_page_component_group_id(
            d.pop("status_page_component_group_id", UNSET)
        )

        def _parse_name(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_source_type(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        source_type = _parse_source_type(d.pop("source_type", UNSET))

        def _parse_source_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        source_id = _parse_source_id(d.pop("source_id", UNSET))

        _status = d.pop("status", UNSET)
        status: Unset | StatusPageComponentStatus
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_status_page_component_status(_status)

        status_page_component = cls(
            status_page_id=status_page_id,
            position=position,
            created_at=created_at,
            updated_at=updated_at,
            status_page_component_group_id=status_page_component_group_id,
            name=name,
            description=description,
            source_type=source_type,
            source_id=source_id,
            status=status,
        )

        status_page_component.additional_properties = d
        return status_page_component

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
