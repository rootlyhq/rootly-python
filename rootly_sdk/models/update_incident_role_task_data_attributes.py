from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.update_incident_role_task_data_attributes_priority import (
    UpdateIncidentRoleTaskDataAttributesPriority,
    check_update_incident_role_task_data_attributes_priority,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateIncidentRoleTaskDataAttributes")


@_attrs_define
class UpdateIncidentRoleTaskDataAttributes:
    """
    Attributes:
        task (str | Unset): The task of the incident task
        description (None | str | Unset): The description of the incident task
        priority (UpdateIncidentRoleTaskDataAttributesPriority | Unset): The priority of the incident task
    """

    task: str | Unset = UNSET
    description: None | str | Unset = UNSET
    priority: UpdateIncidentRoleTaskDataAttributesPriority | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        task = self.task

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        priority: str | Unset = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if task is not UNSET:
            field_dict["task"] = task
        if description is not UNSET:
            field_dict["description"] = description
        if priority is not UNSET:
            field_dict["priority"] = priority

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        task = d.pop("task", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _priority = d.pop("priority", UNSET)
        priority: UpdateIncidentRoleTaskDataAttributesPriority | Unset
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = check_update_incident_role_task_data_attributes_priority(_priority)

        update_incident_role_task_data_attributes = cls(
            task=task,
            description=description,
            priority=priority,
        )

        return update_incident_role_task_data_attributes
