from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.retrospective_configuration_kind import (
    RetrospectiveConfigurationKind,
    check_retrospective_configuration_kind,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RetrospectiveConfiguration")


@_attrs_define
class RetrospectiveConfiguration:
    """
    Attributes:
        kind (Union[Unset, RetrospectiveConfigurationKind]): The kind of the configuration.
        severity_ids (Union[None, Unset, list[str]]): The Severity IDs to attach to the retrospective configuration
        group_ids (Union[None, Unset, list[str]]): The Team IDs to attach to the retrospective configuration
        incident_type_ids (Union[None, Unset, list[str]]): The Incident Type IDs to attach to the retrospective
            configuration
        created_at (Union[Unset, str]): Date of creation
        updated_at (Union[Unset, str]): Date of last update
    """

    kind: Unset | RetrospectiveConfigurationKind = UNSET
    severity_ids: None | Unset | list[str] = UNSET
    group_ids: None | Unset | list[str] = UNSET
    incident_type_ids: None | Unset | list[str] = UNSET
    created_at: Unset | str = UNSET
    updated_at: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind: Unset | str = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        severity_ids: None | Unset | list[str]
        if isinstance(self.severity_ids, Unset):
            severity_ids = UNSET
        elif isinstance(self.severity_ids, list):
            severity_ids = self.severity_ids

        else:
            severity_ids = self.severity_ids

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

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if severity_ids is not UNSET:
            field_dict["severity_ids"] = severity_ids
        if group_ids is not UNSET:
            field_dict["group_ids"] = group_ids
        if incident_type_ids is not UNSET:
            field_dict["incident_type_ids"] = incident_type_ids
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _kind = d.pop("kind", UNSET)
        kind: Unset | RetrospectiveConfigurationKind
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_retrospective_configuration_kind(_kind)

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

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        retrospective_configuration = cls(
            kind=kind,
            severity_ids=severity_ids,
            group_ids=group_ids,
            incident_type_ids=incident_type_ids,
            created_at=created_at,
            updated_at=updated_at,
        )

        retrospective_configuration.additional_properties = d
        return retrospective_configuration

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
