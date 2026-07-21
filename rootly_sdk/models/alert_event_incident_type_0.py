from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertEventIncidentType0")


@_attrs_define
class AlertEventIncidentType0:
    """
    Attributes:
        id (str | Unset):
        sequential_id (int | None | Unset):
        title (str | Unset):
        slug (str | Unset):
        kind (str | Unset):
        status (str | Unset):
        private (bool | Unset):
        description (None | str | Unset):
        started_at (None | str | Unset):
        duration (int | None | Unset): Duration in seconds.
        url (str | Unset):
        created_at (str | Unset):
        updated_at (str | Unset):
    """

    id: str | Unset = UNSET
    sequential_id: int | None | Unset = UNSET
    title: str | Unset = UNSET
    slug: str | Unset = UNSET
    kind: str | Unset = UNSET
    status: str | Unset = UNSET
    private: bool | Unset = UNSET
    description: None | str | Unset = UNSET
    started_at: None | str | Unset = UNSET
    duration: int | None | Unset = UNSET
    url: str | Unset = UNSET
    created_at: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        sequential_id: int | None | Unset
        if isinstance(self.sequential_id, Unset):
            sequential_id = UNSET
        else:
            sequential_id = self.sequential_id

        title = self.title

        slug = self.slug

        kind = self.kind

        status = self.status

        private = self.private

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        started_at: None | str | Unset
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        else:
            started_at = self.started_at

        duration: int | None | Unset
        if isinstance(self.duration, Unset):
            duration = UNSET
        else:
            duration = self.duration

        url = self.url

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if sequential_id is not UNSET:
            field_dict["sequential_id"] = sequential_id
        if title is not UNSET:
            field_dict["title"] = title
        if slug is not UNSET:
            field_dict["slug"] = slug
        if kind is not UNSET:
            field_dict["kind"] = kind
        if status is not UNSET:
            field_dict["status"] = status
        if private is not UNSET:
            field_dict["private"] = private
        if description is not UNSET:
            field_dict["description"] = description
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if duration is not UNSET:
            field_dict["duration"] = duration
        if url is not UNSET:
            field_dict["url"] = url
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_sequential_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sequential_id = _parse_sequential_id(d.pop("sequential_id", UNSET))

        title = d.pop("title", UNSET)

        slug = d.pop("slug", UNSET)

        kind = d.pop("kind", UNSET)

        status = d.pop("status", UNSET)

        private = d.pop("private", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_started_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        started_at = _parse_started_at(d.pop("started_at", UNSET))

        def _parse_duration(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        duration = _parse_duration(d.pop("duration", UNSET))

        url = d.pop("url", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        alert_event_incident_type_0 = cls(
            id=id,
            sequential_id=sequential_id,
            title=title,
            slug=slug,
            kind=kind,
            status=status,
            private=private,
            description=description,
            started_at=started_at,
            duration=duration,
            url=url,
            created_at=created_at,
            updated_at=updated_at,
        )

        alert_event_incident_type_0.additional_properties = d
        return alert_event_incident_type_0

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
