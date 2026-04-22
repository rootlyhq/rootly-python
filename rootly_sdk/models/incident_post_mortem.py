from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.incident_post_mortem_show_timeline_order import (
    IncidentPostMortemShowTimelineOrder,
    check_incident_post_mortem_show_timeline_order,
)
from ..models.incident_post_mortem_status import IncidentPostMortemStatus, check_incident_post_mortem_status
from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentPostMortem")


@_attrs_define
class IncidentPostMortem:
    """
    Attributes:
        title (str): The title of the incident retrospective
        created_at (str): Date of creation
        updated_at (str): Date of last update
        content (None | str | Unset): The content of the incident retrospective (Only if internal)
        status (IncidentPostMortemStatus | Unset): The status of the incident retrospective
        started_at (None | str | Unset): Date of started at
        mitigated_at (None | str | Unset): Date of mitigation
        resolved_at (None | str | Unset): Date of resolution
        show_timeline (bool | Unset): Show events timeline of the incident retrospective
        show_timeline_trail (bool | Unset): Show trail events in the timeline of the incident retrospective
        show_timeline_genius (bool | Unset): Show workflow events in the timeline of the incident retrospective
        show_timeline_tasks (bool | Unset): Show tasks in the timeline of the incident retrospective
        show_timeline_action_items (bool | Unset): Show action items in the timeline of the incident retrospective
        show_timeline_order (IncidentPostMortemShowTimelineOrder | Unset): The order of the incident retrospective
            timeline Default: 'desc'.
        show_services_impacted (bool | Unset): Show functionalities impacted of the incident retrospective
        show_functionalities_impacted (bool | Unset): Show services impacted of the incident retrospective
        show_groups_impacted (bool | Unset): Show groups impacted of the incident retrospective
        show_alerts_attached (bool | Unset): Show alerts attached to the incident
        url (str | Unset): The url to the incident retrospective
    """

    title: str
    created_at: str
    updated_at: str
    content: None | str | Unset = UNSET
    status: IncidentPostMortemStatus | Unset = UNSET
    started_at: None | str | Unset = UNSET
    mitigated_at: None | str | Unset = UNSET
    resolved_at: None | str | Unset = UNSET
    show_timeline: bool | Unset = UNSET
    show_timeline_trail: bool | Unset = UNSET
    show_timeline_genius: bool | Unset = UNSET
    show_timeline_tasks: bool | Unset = UNSET
    show_timeline_action_items: bool | Unset = UNSET
    show_timeline_order: IncidentPostMortemShowTimelineOrder | Unset = "desc"
    show_services_impacted: bool | Unset = UNSET
    show_functionalities_impacted: bool | Unset = UNSET
    show_groups_impacted: bool | Unset = UNSET
    show_alerts_attached: bool | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        created_at = self.created_at

        updated_at = self.updated_at

        content: None | str | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        started_at: None | str | Unset
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        else:
            started_at = self.started_at

        mitigated_at: None | str | Unset
        if isinstance(self.mitigated_at, Unset):
            mitigated_at = UNSET
        else:
            mitigated_at = self.mitigated_at

        resolved_at: None | str | Unset
        if isinstance(self.resolved_at, Unset):
            resolved_at = UNSET
        else:
            resolved_at = self.resolved_at

        show_timeline = self.show_timeline

        show_timeline_trail = self.show_timeline_trail

        show_timeline_genius = self.show_timeline_genius

        show_timeline_tasks = self.show_timeline_tasks

        show_timeline_action_items = self.show_timeline_action_items

        show_timeline_order: str | Unset = UNSET
        if not isinstance(self.show_timeline_order, Unset):
            show_timeline_order = self.show_timeline_order

        show_services_impacted = self.show_services_impacted

        show_functionalities_impacted = self.show_functionalities_impacted

        show_groups_impacted = self.show_groups_impacted

        show_alerts_attached = self.show_alerts_attached

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if content is not UNSET:
            field_dict["content"] = content
        if status is not UNSET:
            field_dict["status"] = status
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if mitigated_at is not UNSET:
            field_dict["mitigated_at"] = mitigated_at
        if resolved_at is not UNSET:
            field_dict["resolved_at"] = resolved_at
        if show_timeline is not UNSET:
            field_dict["show_timeline"] = show_timeline
        if show_timeline_trail is not UNSET:
            field_dict["show_timeline_trail"] = show_timeline_trail
        if show_timeline_genius is not UNSET:
            field_dict["show_timeline_genius"] = show_timeline_genius
        if show_timeline_tasks is not UNSET:
            field_dict["show_timeline_tasks"] = show_timeline_tasks
        if show_timeline_action_items is not UNSET:
            field_dict["show_timeline_action_items"] = show_timeline_action_items
        if show_timeline_order is not UNSET:
            field_dict["show_timeline_order"] = show_timeline_order
        if show_services_impacted is not UNSET:
            field_dict["show_services_impacted"] = show_services_impacted
        if show_functionalities_impacted is not UNSET:
            field_dict["show_functionalities_impacted"] = show_functionalities_impacted
        if show_groups_impacted is not UNSET:
            field_dict["show_groups_impacted"] = show_groups_impacted
        if show_alerts_attached is not UNSET:
            field_dict["show_alerts_attached"] = show_alerts_attached
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        def _parse_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content = _parse_content(d.pop("content", UNSET))

        _status = d.pop("status", UNSET)
        status: IncidentPostMortemStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_incident_post_mortem_status(_status)

        def _parse_started_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        started_at = _parse_started_at(d.pop("started_at", UNSET))

        def _parse_mitigated_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mitigated_at = _parse_mitigated_at(d.pop("mitigated_at", UNSET))

        def _parse_resolved_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resolved_at = _parse_resolved_at(d.pop("resolved_at", UNSET))

        show_timeline = d.pop("show_timeline", UNSET)

        show_timeline_trail = d.pop("show_timeline_trail", UNSET)

        show_timeline_genius = d.pop("show_timeline_genius", UNSET)

        show_timeline_tasks = d.pop("show_timeline_tasks", UNSET)

        show_timeline_action_items = d.pop("show_timeline_action_items", UNSET)

        _show_timeline_order = d.pop("show_timeline_order", UNSET)
        show_timeline_order: IncidentPostMortemShowTimelineOrder | Unset
        if isinstance(_show_timeline_order, Unset):
            show_timeline_order = UNSET
        else:
            show_timeline_order = check_incident_post_mortem_show_timeline_order(_show_timeline_order)

        show_services_impacted = d.pop("show_services_impacted", UNSET)

        show_functionalities_impacted = d.pop("show_functionalities_impacted", UNSET)

        show_groups_impacted = d.pop("show_groups_impacted", UNSET)

        show_alerts_attached = d.pop("show_alerts_attached", UNSET)

        url = d.pop("url", UNSET)

        incident_post_mortem = cls(
            title=title,
            created_at=created_at,
            updated_at=updated_at,
            content=content,
            status=status,
            started_at=started_at,
            mitigated_at=mitigated_at,
            resolved_at=resolved_at,
            show_timeline=show_timeline,
            show_timeline_trail=show_timeline_trail,
            show_timeline_genius=show_timeline_genius,
            show_timeline_tasks=show_timeline_tasks,
            show_timeline_action_items=show_timeline_action_items,
            show_timeline_order=show_timeline_order,
            show_services_impacted=show_services_impacted,
            show_functionalities_impacted=show_functionalities_impacted,
            show_groups_impacted=show_groups_impacted,
            show_alerts_attached=show_alerts_attached,
            url=url,
        )

        incident_post_mortem.additional_properties = d
        return incident_post_mortem

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
