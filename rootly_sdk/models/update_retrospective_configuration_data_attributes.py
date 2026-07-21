from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateRetrospectiveConfigurationDataAttributes")


@_attrs_define
class UpdateRetrospectiveConfigurationDataAttributes:
    """
    Attributes:
        severity_ids (list[str] | None | Unset): The Severity IDs to attach to the retrospective configuration
        group_ids (list[str] | None | Unset): The Team IDs to attach to the retrospective configuration
        incident_type_ids (list[str] | None | Unset): The Incident Type IDs to attach to the retrospective configuration
    """

    severity_ids: list[str] | None | Unset = UNSET
    group_ids: list[str] | None | Unset = UNSET
    incident_type_ids: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        severity_ids: list[str] | None | Unset
        if isinstance(self.severity_ids, Unset):
            severity_ids = UNSET
        elif isinstance(self.severity_ids, list):
            severity_ids = self.severity_ids

        else:
            severity_ids = self.severity_ids

        group_ids: list[str] | None | Unset
        if isinstance(self.group_ids, Unset):
            group_ids = UNSET
        elif isinstance(self.group_ids, list):
            group_ids = self.group_ids

        else:
            group_ids = self.group_ids

        incident_type_ids: list[str] | None | Unset
        if isinstance(self.incident_type_ids, Unset):
            incident_type_ids = UNSET
        elif isinstance(self.incident_type_ids, list):
            incident_type_ids = self.incident_type_ids

        else:
            incident_type_ids = self.incident_type_ids

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if severity_ids is not UNSET:
            field_dict["severity_ids"] = severity_ids
        if group_ids is not UNSET:
            field_dict["group_ids"] = group_ids
        if incident_type_ids is not UNSET:
            field_dict["incident_type_ids"] = incident_type_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_severity_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                severity_ids_type_0 = cast(list[str], data)

                return severity_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        severity_ids = _parse_severity_ids(d.pop("severity_ids", UNSET))

        def _parse_group_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                group_ids_type_0 = cast(list[str], data)

                return group_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        group_ids = _parse_group_ids(d.pop("group_ids", UNSET))

        def _parse_incident_type_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                incident_type_ids_type_0 = cast(list[str], data)

                return incident_type_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        incident_type_ids = _parse_incident_type_ids(d.pop("incident_type_ids", UNSET))

        update_retrospective_configuration_data_attributes = cls(
            severity_ids=severity_ids,
            group_ids=group_ids,
            incident_type_ids=incident_type_ids,
        )

        return update_retrospective_configuration_data_attributes
