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
        task (Union[Unset, str]): The task of the incident task
        description (Union[None, Unset, str]): The description of the incident task
        priority (Union[Unset, UpdateIncidentRoleTaskDataAttributesPriority]): The priority of the incident task
    """

    task: Unset | str = UNSET
    description: None | Unset | str = UNSET
    priority: Unset | UpdateIncidentRoleTaskDataAttributesPriority = UNSET

    def to_dict(self) -> dict[str, Any]:
        task = self.task

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        priority: Unset | str = UNSET
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

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        description = _parse_description(d.pop("description", UNSET))

        _priority = d.pop("priority", UNSET)
        priority: Unset | UpdateIncidentRoleTaskDataAttributesPriority
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
