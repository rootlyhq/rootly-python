from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.update_incident_post_mortem_data_attributes_status import (
    UpdateIncidentPostMortemDataAttributesStatus,
    check_update_incident_post_mortem_data_attributes_status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateIncidentPostMortemDataAttributes")


@_attrs_define
class UpdateIncidentPostMortemDataAttributes:
    """
    Attributes:
        title (str | Unset): The title of the incident retrospective
        status (UpdateIncidentPostMortemDataAttributesStatus | Unset): The status of the incident retrospective
        started_at (None | str | Unset): Date of started at
        mitigated_at (None | str | Unset): Date of mitigation
        resolved_at (None | str | Unset): Date of resolution
        show_timeline (bool | Unset): Show events timeline of the incident retrospective
        show_timeline_trail (bool | Unset): Show trail events in the timeline of the incident retrospective
        show_timeline_genius (bool | Unset): Show workflow events in the timeline of the incident retrospective
        show_timeline_tasks (bool | Unset): Show tasks in the timeline of the incident retrospective
        show_timeline_action_items (bool | Unset): Show action items in the timeline of the incident retrospective
        show_services_impacted (bool | Unset): Show functionalities impacted of the incident retrospective
        show_functionalities_impacted (bool | Unset): Show services impacted of the incident retrospective
        show_groups_impacted (bool | Unset): Show groups impacted of the incident retrospective
        show_alerts_attached (bool | Unset): Show alerts attached to the incident
        show_action_items (bool | Unset): Show action items (follow-ups) in the incident retrospective
        cause_ids (list[str] | None | Unset): The Cause IDs to attach to the incident retrospective
    """

    title: str | Unset = UNSET
    status: UpdateIncidentPostMortemDataAttributesStatus | Unset = UNSET
    started_at: None | str | Unset = UNSET
    mitigated_at: None | str | Unset = UNSET
    resolved_at: None | str | Unset = UNSET
    show_timeline: bool | Unset = UNSET
    show_timeline_trail: bool | Unset = UNSET
    show_timeline_genius: bool | Unset = UNSET
    show_timeline_tasks: bool | Unset = UNSET
    show_timeline_action_items: bool | Unset = UNSET
    show_services_impacted: bool | Unset = UNSET
    show_functionalities_impacted: bool | Unset = UNSET
    show_groups_impacted: bool | Unset = UNSET
    show_alerts_attached: bool | Unset = UNSET
    show_action_items: bool | Unset = UNSET
    cause_ids: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        title = self.title

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

        show_services_impacted = self.show_services_impacted

        show_functionalities_impacted = self.show_functionalities_impacted

        show_groups_impacted = self.show_groups_impacted

        show_alerts_attached = self.show_alerts_attached

        show_action_items = self.show_action_items

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
        if show_services_impacted is not UNSET:
            field_dict["show_services_impacted"] = show_services_impacted
        if show_functionalities_impacted is not UNSET:
            field_dict["show_functionalities_impacted"] = show_functionalities_impacted
        if show_groups_impacted is not UNSET:
            field_dict["show_groups_impacted"] = show_groups_impacted
        if show_alerts_attached is not UNSET:
            field_dict["show_alerts_attached"] = show_alerts_attached
        if show_action_items is not UNSET:
            field_dict["show_action_items"] = show_action_items
        if cause_ids is not UNSET:
            field_dict["cause_ids"] = cause_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title", UNSET)

        _status = d.pop("status", UNSET)
        status: UpdateIncidentPostMortemDataAttributesStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_update_incident_post_mortem_data_attributes_status(_status)

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

        show_services_impacted = d.pop("show_services_impacted", UNSET)

        show_functionalities_impacted = d.pop("show_functionalities_impacted", UNSET)

        show_groups_impacted = d.pop("show_groups_impacted", UNSET)

        show_alerts_attached = d.pop("show_alerts_attached", UNSET)

        show_action_items = d.pop("show_action_items", UNSET)

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

        update_incident_post_mortem_data_attributes = cls(
            title=title,
            status=status,
            started_at=started_at,
            mitigated_at=mitigated_at,
            resolved_at=resolved_at,
            show_timeline=show_timeline,
            show_timeline_trail=show_timeline_trail,
            show_timeline_genius=show_timeline_genius,
            show_timeline_tasks=show_timeline_tasks,
            show_timeline_action_items=show_timeline_action_items,
            show_services_impacted=show_services_impacted,
            show_functionalities_impacted=show_functionalities_impacted,
            show_groups_impacted=show_groups_impacted,
            show_alerts_attached=show_alerts_attached,
            show_action_items=show_action_items,
            cause_ids=cause_ids,
        )

        return update_incident_post_mortem_data_attributes
