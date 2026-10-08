from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.update_playbook_data_attributes_kind import (
    UpdatePlaybookDataAttributesKind,
    check_update_playbook_data_attributes_kind,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdatePlaybookDataAttributes")


@_attrs_define
class UpdatePlaybookDataAttributes:
    """
    Attributes:
        title (str | Unset): The title of the playbook
        summary (None | str | Unset): The summary of the playbook
        kind (UpdatePlaybookDataAttributesKind | Unset): Whether the playbook body lives in Rootly (`internal_document`)
            or at an external link (`external_url`).
        content (None | str | Unset): Sanitized HTML instructions. Still returned when `kind` is `external_url`, where
            the body may be stale — branch on `kind`, not on `content` being present.
        external_url (None | str | Unset): The external url of the playbook
        severity_ids (list[str] | None | Unset): The Severity IDs to attach to the incident
        environment_ids (list[str] | None | Unset): The Environment IDs to attach to the incident
        service_ids (list[str] | None | Unset): The Service IDs to attach to the incident
        functionality_ids (list[str] | None | Unset): The Functionality IDs to attach to the incident
        group_ids (list[str] | None | Unset): The Team IDs to attach to the incident
        incident_type_ids (list[str] | None | Unset): The Incident Type IDs to attach to the incident
        cause_ids (list[str] | None | Unset): The Cause IDs to attach to the incident
    """

    title: str | Unset = UNSET
    summary: None | str | Unset = UNSET
    kind: UpdatePlaybookDataAttributesKind | Unset = UNSET
    content: None | str | Unset = UNSET
    external_url: None | str | Unset = UNSET
    severity_ids: list[str] | None | Unset = UNSET
    environment_ids: list[str] | None | Unset = UNSET
    service_ids: list[str] | None | Unset = UNSET
    functionality_ids: list[str] | None | Unset = UNSET
    group_ids: list[str] | None | Unset = UNSET
    incident_type_ids: list[str] | None | Unset = UNSET
    cause_ids: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        summary: None | str | Unset
        if isinstance(self.summary, Unset):
            summary = UNSET
        else:
            summary = self.summary

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        content: None | str | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

        external_url: None | str | Unset
        if isinstance(self.external_url, Unset):
            external_url = UNSET
        else:
            external_url = self.external_url

        severity_ids: list[str] | None | Unset
        if isinstance(self.severity_ids, Unset):
            severity_ids = UNSET
        elif isinstance(self.severity_ids, list):
            severity_ids = self.severity_ids

        else:
            severity_ids = self.severity_ids

        environment_ids: list[str] | None | Unset
        if isinstance(self.environment_ids, Unset):
            environment_ids = UNSET
        elif isinstance(self.environment_ids, list):
            environment_ids = self.environment_ids

        else:
            environment_ids = self.environment_ids

        service_ids: list[str] | None | Unset
        if isinstance(self.service_ids, Unset):
            service_ids = UNSET
        elif isinstance(self.service_ids, list):
            service_ids = self.service_ids

        else:
            service_ids = self.service_ids

        functionality_ids: list[str] | None | Unset
        if isinstance(self.functionality_ids, Unset):
            functionality_ids = UNSET
        elif isinstance(self.functionality_ids, list):
            functionality_ids = self.functionality_ids

        else:
            functionality_ids = self.functionality_ids

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

        cause_ids: list[str] | None | Unset
        if isinstance(self.cause_ids, Unset):
            cause_ids = UNSET
        elif isinstance(self.cause_ids, list):
            cause_ids = self.cause_ids

        else:
            cause_ids = self.cause_ids

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if summary is not UNSET:
            field_dict["summary"] = summary
        if kind is not UNSET:
            field_dict["kind"] = kind
        if content is not UNSET:
            field_dict["content"] = content
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
        if cause_ids is not UNSET:
            field_dict["cause_ids"] = cause_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title", UNSET)

        def _parse_summary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        summary = _parse_summary(d.pop("summary", UNSET))

        _kind = d.pop("kind", UNSET)
        kind: UpdatePlaybookDataAttributesKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_update_playbook_data_attributes_kind(_kind)

        def _parse_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content = _parse_content(d.pop("content", UNSET))

        def _parse_external_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_url = _parse_external_url(d.pop("external_url", UNSET))

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

        def _parse_environment_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                environment_ids_type_0 = cast(list[str], data)

                return environment_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        environment_ids = _parse_environment_ids(d.pop("environment_ids", UNSET))

        def _parse_service_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                service_ids_type_0 = cast(list[str], data)

                return service_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        service_ids = _parse_service_ids(d.pop("service_ids", UNSET))

        def _parse_functionality_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                functionality_ids_type_0 = cast(list[str], data)

                return functionality_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        functionality_ids = _parse_functionality_ids(d.pop("functionality_ids", UNSET))

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

        def _parse_cause_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cause_ids_type_0 = cast(list[str], data)

                return cause_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        cause_ids = _parse_cause_ids(d.pop("cause_ids", UNSET))

        update_playbook_data_attributes = cls(
            title=title,
            summary=summary,
            kind=kind,
            content=content,
            external_url=external_url,
            severity_ids=severity_ids,
            environment_ids=environment_ids,
            service_ids=service_ids,
            functionality_ids=functionality_ids,
            group_ids=group_ids,
            incident_type_ids=incident_type_ids,
            cause_ids=cause_ids,
        )

        return update_playbook_data_attributes
