from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.incident_role_task_priority import IncidentRoleTaskPriority, check_incident_role_task_priority
from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentRoleTask")


@_attrs_define
class IncidentRoleTask:
    """
    Attributes:
        task (str): The task of the incident task
        created_at (str): Date of creation
        updated_at (str): Date of last update
        incident_role_id (Union[Unset, str]):
        description (Union[None, Unset, str]): The description of incident task
        priority (Union[Unset, IncidentRoleTaskPriority]): The priority of the incident task
    """

    task: str
    created_at: str
    updated_at: str
    incident_role_id: Unset | str = UNSET
    description: None | Unset | str = UNSET
    priority: Unset | IncidentRoleTaskPriority = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        task = self.task

        created_at = self.created_at

        updated_at = self.updated_at

        incident_role_id = self.incident_role_id

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        priority: Unset | str = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "task": task,
                "created_at": created_at,
                "updated_at": updated_at,
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

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        incident_role_id = d.pop("incident_role_id", UNSET)

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        description = _parse_description(d.pop("description", UNSET))

        _priority = d.pop("priority", UNSET)
        priority: Unset | IncidentRoleTaskPriority
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = check_incident_role_task_priority(_priority)

        incident_role_task = cls(
            task=task,
            created_at=created_at,
            updated_at=updated_at,
            incident_role_id=incident_role_id,
            description=description,
            priority=priority,
        )

        incident_role_task.additional_properties = d
        return incident_role_task

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
