from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdatePlaybookDataAttributes")


@_attrs_define
class UpdatePlaybookDataAttributes:
    """
    Attributes:
        title (Union[Unset, str]): The title of the playbook
        summary (Union[None, Unset, str]): The summary of the playbook
        external_url (Union[None, Unset, str]): The external url of the playbook
        severity_ids (Union[None, Unset, list[str]]): The Severity IDs to attach to the incident
        environment_ids (Union[None, Unset, list[str]]): The Environment IDs to attach to the incident
        service_ids (Union[None, Unset, list[str]]): The Service IDs to attach to the incident
        functionality_ids (Union[None, Unset, list[str]]): The Functionality IDs to attach to the incident
        group_ids (Union[None, Unset, list[str]]): The Team IDs to attach to the incident
        incident_type_ids (Union[None, Unset, list[str]]): The Incident Type IDs to attach to the incident
    """

    title: Union[Unset, str] = UNSET
    summary: Union[None, Unset, str] = UNSET
    external_url: Union[None, Unset, str] = UNSET
    severity_ids: Union[None, Unset, list[str]] = UNSET
    environment_ids: Union[None, Unset, list[str]] = UNSET
    service_ids: Union[None, Unset, list[str]] = UNSET
    functionality_ids: Union[None, Unset, list[str]] = UNSET
    group_ids: Union[None, Unset, list[str]] = UNSET
    incident_type_ids: Union[None, Unset, list[str]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        summary: Union[None, Unset, str]
        if isinstance(self.summary, Unset):
            summary = UNSET
        else:
            summary = self.summary

        external_url: Union[None, Unset, str]
        if isinstance(self.external_url, Unset):
            external_url = UNSET
        else:
            external_url = self.external_url

        severity_ids: Union[None, Unset, list[str]]
        if isinstance(self.severity_ids, Unset):
            severity_ids = UNSET
        elif isinstance(self.severity_ids, list):
            severity_ids = self.severity_ids

        else:
            severity_ids = self.severity_ids

        environment_ids: Union[None, Unset, list[str]]
        if isinstance(self.environment_ids, Unset):
            environment_ids = UNSET
        elif isinstance(self.environment_ids, list):
            environment_ids = self.environment_ids

        else:
            environment_ids = self.environment_ids

        service_ids: Union[None, Unset, list[str]]
        if isinstance(self.service_ids, Unset):
            service_ids = UNSET
        elif isinstance(self.service_ids, list):
            service_ids = self.service_ids

        else:
            service_ids = self.service_ids

        functionality_ids: Union[None, Unset, list[str]]
        if isinstance(self.functionality_ids, Unset):
            functionality_ids = UNSET
        elif isinstance(self.functionality_ids, list):
            functionality_ids = self.functionality_ids

        else:
            functionality_ids = self.functionality_ids

        group_ids: Union[None, Unset, list[str]]
        if isinstance(self.group_ids, Unset):
            group_ids = UNSET
        elif isinstance(self.group_ids, list):
            group_ids = self.group_ids

        else:
            group_ids = self.group_ids

        incident_type_ids: Union[None, Unset, list[str]]
        if isinstance(self.incident_type_ids, Unset):
            incident_type_ids = UNSET
        elif isinstance(self.incident_type_ids, list):
            incident_type_ids = self.incident_type_ids

        else:
            incident_type_ids = self.incident_type_ids

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if summary is not UNSET:
            field_dict["summary"] = summary
        if external_url is not UNSET:
            field_dict["external_url"] = external_url
        if severity_ids is not UNSET:
            field_dict["severity_ids"] = severity_ids
        if environment_ids is not UNSET:
            field_dict["environment_ids"] = environment_ids
        if service_ids is not UNSET:
            field_dict["service_ids"] = service_ids
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
        title = d.pop("title", UNSET)

        def _parse_summary(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        summary = _parse_summary(d.pop("summary", UNSET))

        def _parse_external_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_url = _parse_external_url(d.pop("external_url", UNSET))

        def _parse_severity_ids(data: object) -> Union[None, Unset, list[str]]:
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
            return cast(Union[None, Unset, list[str]], data)

        severity_ids = _parse_severity_ids(d.pop("severity_ids", UNSET))

        def _parse_environment_ids(data: object) -> Union[None, Unset, list[str]]:
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
            return cast(Union[None, Unset, list[str]], data)

        environment_ids = _parse_environment_ids(d.pop("environment_ids", UNSET))

        def _parse_service_ids(data: object) -> Union[None, Unset, list[str]]:
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
            return cast(Union[None, Unset, list[str]], data)

        service_ids = _parse_service_ids(d.pop("service_ids", UNSET))

        def _parse_functionality_ids(data: object) -> Union[None, Unset, list[str]]:
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
            return cast(Union[None, Unset, list[str]], data)

        functionality_ids = _parse_functionality_ids(d.pop("functionality_ids", UNSET))

        def _parse_group_ids(data: object) -> Union[None, Unset, list[str]]:
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
            return cast(Union[None, Unset, list[str]], data)

        group_ids = _parse_group_ids(d.pop("group_ids", UNSET))

        def _parse_incident_type_ids(data: object) -> Union[None, Unset, list[str]]:
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
            return cast(Union[None, Unset, list[str]], data)

        incident_type_ids = _parse_incident_type_ids(d.pop("incident_type_ids", UNSET))

        update_playbook_data_attributes = cls(
            title=title,
            summary=summary,
            external_url=external_url,
            severity_ids=severity_ids,
            environment_ids=environment_ids,
            service_ids=service_ids,
            functionality_ids=functionality_ids,
            group_ids=group_ids,
            incident_type_ids=incident_type_ids,
        )

        return update_playbook_data_attributes
