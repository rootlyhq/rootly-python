from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.communications_group_communication_group_conditions_type_0_item_property_type import (
    CommunicationsGroupCommunicationGroupConditionsType0ItemPropertyType,
    check_communications_group_communication_group_conditions_type_0_item_property_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CommunicationsGroupCommunicationGroupConditionsType0Item")


@_attrs_define
class CommunicationsGroupCommunicationGroupConditionsType0Item:
    """
    Attributes:
        property_type (Union[Unset, CommunicationsGroupCommunicationGroupConditionsType0ItemPropertyType]): Property
            type
        service_ids (Union[None, Unset, list[str]]): Array of service IDs
        severity_ids (Union[None, Unset, list[str]]): Array of severity IDs
        functionality_ids (Union[None, Unset, list[str]]): Array of functionality IDs
        group_ids (Union[None, Unset, list[str]]): Array of group IDs
        incident_type_ids (Union[None, Unset, list[str]]): Array of incident type IDs
    """

    property_type: Unset | CommunicationsGroupCommunicationGroupConditionsType0ItemPropertyType = UNSET
    service_ids: None | Unset | list[str] = UNSET
    severity_ids: None | Unset | list[str] = UNSET
    functionality_ids: None | Unset | list[str] = UNSET
    group_ids: None | Unset | list[str] = UNSET
    incident_type_ids: None | Unset | list[str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        property_type: Unset | str = UNSET
        if not isinstance(self.property_type, Unset):
            property_type = self.property_type

        service_ids: None | Unset | list[str]
        if isinstance(self.service_ids, Unset):
            service_ids = UNSET
        elif isinstance(self.service_ids, list):
            service_ids = self.service_ids

        else:
            service_ids = self.service_ids

        severity_ids: None | Unset | list[str]
        if isinstance(self.severity_ids, Unset):
            severity_ids = UNSET
        elif isinstance(self.severity_ids, list):
            severity_ids = self.severity_ids

        else:
            severity_ids = self.severity_ids

        functionality_ids: None | Unset | list[str]
        if isinstance(self.functionality_ids, Unset):
            functionality_ids = UNSET
        elif isinstance(self.functionality_ids, list):
            functionality_ids = self.functionality_ids

        else:
            functionality_ids = self.functionality_ids

        group_ids: None | Unset | list[str]
        if isinstance(self.group_ids, Unset):
            group_ids = UNSET
        elif isinstance(self.group_ids, list):
            group_ids = self.group_ids

        else:
            group_ids = self.group_ids

        incident_type_ids: None | Unset | list[str]
        if isinstance(self.incident_type_ids, Unset):
            incident_type_ids = UNSET
        elif isinstance(self.incident_type_ids, list):
            incident_type_ids = self.incident_type_ids

        else:
            incident_type_ids = self.incident_type_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if property_type is not UNSET:
            field_dict["property_type"] = property_type
        if service_ids is not UNSET:
            field_dict["service_ids"] = service_ids
        if severity_ids is not UNSET:
            field_dict["severity_ids"] = severity_ids
        if functionality_ids is not UNSET:
            field_dict["functionality_ids"] = functionality_ids
        if group_ids is not UNSET:
            field_dict["group_ids"] = group_ids
        if incident_type_ids is not UNSET:
            field_dict["incident_type_ids"] = incident_type_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _property_type = d.pop("property_type", UNSET)
        property_type: Unset | CommunicationsGroupCommunicationGroupConditionsType0ItemPropertyType
        if isinstance(_property_type, Unset):
            property_type = UNSET
        else:
            property_type = check_communications_group_communication_group_conditions_type_0_item_property_type(
                _property_type
            )

        def _parse_service_ids(data: object) -> None | Unset | list[str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                service_ids_type_0 = cast(list[str], data)

                return service_ids_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | list[str], data)

        service_ids = _parse_service_ids(d.pop("service_ids", UNSET))

        def _parse_severity_ids(data: object) -> None | Unset | list[str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                severity_ids_type_0 = cast(list[str], data)

                return severity_ids_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | list[str], data)

        severity_ids = _parse_severity_ids(d.pop("severity_ids", UNSET))

        def _parse_functionality_ids(data: object) -> None | Unset | list[str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                functionality_ids_type_0 = cast(list[str], data)

                return functionality_ids_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | list[str], data)

        functionality_ids = _parse_functionality_ids(d.pop("functionality_ids", UNSET))

        def _parse_group_ids(data: object) -> None | Unset | list[str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                group_ids_type_0 = cast(list[str], data)

                return group_ids_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | list[str], data)

        group_ids = _parse_group_ids(d.pop("group_ids", UNSET))

        def _parse_incident_type_ids(data: object) -> None | Unset | list[str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                incident_type_ids_type_0 = cast(list[str], data)

                return incident_type_ids_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | list[str], data)

        incident_type_ids = _parse_incident_type_ids(d.pop("incident_type_ids", UNSET))

        communications_group_communication_group_conditions_type_0_item = cls(
            property_type=property_type,
            service_ids=service_ids,
            severity_ids=severity_ids,
            functionality_ids=functionality_ids,
            group_ids=group_ids,
            incident_type_ids=incident_type_ids,
        )

        communications_group_communication_group_conditions_type_0_item.additional_properties = d
        return communications_group_communication_group_conditions_type_0_item

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
