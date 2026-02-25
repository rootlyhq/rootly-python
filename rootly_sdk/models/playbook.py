from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Playbook")


@_attrs_define
class Playbook:
    """
    Attributes:
        title (str): The title of the playbook
        created_at (str): Date of creation
        updated_at (str): Date of last update
        summary (Union[None, Unset, str]): The summary of the playbook
        external_url (Union[None, Unset, str]): The external url of the playbook
        severity_ids (Union[None, Unset, list[str]]): The Severity IDs to attach to the incident
        environment_ids (Union[None, Unset, list[str]]): The Environment IDs to attach to the incident
        functionality_ids (Union[None, Unset, list[str]]): The Functionality IDs to attach to the incident
        service_ids (Union[None, Unset, list[str]]): The Service IDs to attach to the incident
        group_ids (Union[None, Unset, list[str]]): The Team IDs to attach to the incident
        incident_type_ids (Union[None, Unset, list[str]]): The Incident Type IDs to attach to the incident
    """

    title: str
    created_at: str
    updated_at: str
    summary: None | Unset | str = UNSET
    external_url: None | Unset | str = UNSET
    severity_ids: None | Unset | list[str] = UNSET
    environment_ids: None | Unset | list[str] = UNSET
    functionality_ids: None | Unset | list[str] = UNSET
    service_ids: None | Unset | list[str] = UNSET
    group_ids: None | Unset | list[str] = UNSET
    incident_type_ids: None | Unset | list[str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        created_at = self.created_at

        updated_at = self.updated_at

        summary: None | Unset | str
        if isinstance(self.summary, Unset):
            summary = UNSET
        else:
            summary = self.summary

        external_url: None | Unset | str
        if isinstance(self.external_url, Unset):
            external_url = UNSET
        else:
            external_url = self.external_url

        severity_ids: None | Unset | list[str]
        if isinstance(self.severity_ids, Unset):
            severity_ids = UNSET
        elif isinstance(self.severity_ids, list):
            severity_ids = self.severity_ids

        else:
            severity_ids = self.severity_ids

        environment_ids: None | Unset | list[str]
        if isinstance(self.environment_ids, Unset):
            environment_ids = UNSET
        elif isinstance(self.environment_ids, list):
            environment_ids = self.environment_ids

        else:
            environment_ids = self.environment_ids

        functionality_ids: None | Unset | list[str]
        if isinstance(self.functionality_ids, Unset):
            functionality_ids = UNSET
        elif isinstance(self.functionality_ids, list):
            functionality_ids = self.functionality_ids

        else:
            functionality_ids = self.functionality_ids

        service_ids: None | Unset | list[str]
        if isinstance(self.service_ids, Unset):
            service_ids = UNSET
        elif isinstance(self.service_ids, list):
            service_ids = self.service_ids

        else:
            service_ids = self.service_ids

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
        field_dict.update(
            {
                "title": title,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if summary is not UNSET:
            field_dict["summary"] = summary
        if external_url is not UNSET:
            field_dict["external_url"] = external_url
        if severity_ids is not UNSET:
            field_dict["severity_ids"] = severity_ids
        if environment_ids is not UNSET:
            field_dict["environment_ids"] = environment_ids
        if functionality_ids is not UNSET:
            field_dict["functionality_ids"] = functionality_ids
        if service_ids is not UNSET:
            field_dict["service_ids"] = service_ids
        if group_ids is not UNSET:
            field_dict["group_ids"] = group_ids
        if incident_type_ids is not UNSET:
            field_dict["incident_type_ids"] = incident_type_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        def _parse_summary(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        summary = _parse_summary(d.pop("summary", UNSET))

        def _parse_external_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        external_url = _parse_external_url(d.pop("external_url", UNSET))

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

        def _parse_environment_ids(data: object) -> None | Unset | list[str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                environment_ids_type_0 = cast(list[str], data)

                return environment_ids_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | list[str], data)

        environment_ids = _parse_environment_ids(d.pop("environment_ids", UNSET))

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

        playbook = cls(
            title=title,
            created_at=created_at,
            updated_at=updated_at,
            summary=summary,
            external_url=external_url,
            severity_ids=severity_ids,
            environment_ids=environment_ids,
            functionality_ids=functionality_ids,
            service_ids=service_ids,
            group_ids=group_ids,
            incident_type_ids=incident_type_ids,
        )

        playbook.additional_properties = d
        return playbook

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
