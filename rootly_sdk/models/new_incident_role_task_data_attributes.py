from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.new_incident_role_task_data_attributes_priority import (
    NewIncidentRoleTaskDataAttributesPriority,
    check_new_incident_role_task_data_attributes_priority,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="NewIncidentRoleTaskDataAttributes")


@_attrs_define
class NewIncidentRoleTaskDataAttributes:
    """
    Attributes:
        task (str): The task of the incident task
        incident_role_id (str | Unset):
        description (None | str | Unset): The description of the incident task
        priority (NewIncidentRoleTaskDataAttributesPriority | Unset): The priority of the incident task
    """

    task: str
    incident_role_id: str | Unset = UNSET
    description: None | str | Unset = UNSET
    priority: NewIncidentRoleTaskDataAttributesPriority | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        task = self.task

        incident_role_id = self.incident_role_id

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        priority: str | Unset = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "task": task,
            }
        )
        if incident_role_id is not UNSET:
            field_dict["incident_role_id"] = incident_role_id
        if description is not UNSET:
            field_dict["description"] = description
        if priority is not UNSET:
            field_dict["priority"] = priority

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        task = d.pop("task")

        incident_role_id = d.pop("incident_role_id", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _priority = d.pop("priority", UNSET)
        priority: NewIncidentRoleTaskDataAttributesPriority | Unset
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = check_new_incident_role_task_data_attributes_priority(_priority)

        new_incident_role_task_data_attributes = cls(
            task=task,
            incident_role_id=incident_role_id,
            description=description,
            priority=priority,
        )

        return new_incident_role_task_data_attributes
