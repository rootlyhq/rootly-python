from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_motion_task_task_params_task_type import (
    UpdateMotionTaskTaskParamsTaskType,
    check_update_motion_task_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_motion_task_task_params_priority import UpdateMotionTaskTaskParamsPriority


T = TypeVar("T", bound="UpdateMotionTaskTaskParams")


@_attrs_define
class UpdateMotionTaskTaskParams:
    """
    Attributes:
        task_id (str): The task id
        task_type (UpdateMotionTaskTaskParamsTaskType | Unset):
        title (str | Unset): The task title
        description (str | Unset): The task description
        labels (list[str] | Unset):
        priority (UpdateMotionTaskTaskParamsPriority | Unset): The priority id and display name
        duration (str | Unset): The duration. Eg.  "NONE", "REMINDER", or a integer greater than 0.
        due_date (str | Unset): The due date
    """

    task_id: str
    task_type: UpdateMotionTaskTaskParamsTaskType | Unset = UNSET
    title: str | Unset = UNSET
    description: str | Unset = UNSET
    labels: list[str] | Unset = UNSET
    priority: UpdateMotionTaskTaskParamsPriority | Unset = UNSET
    duration: str | Unset = UNSET
    due_date: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        task_id = self.task_id

        task_type: str | Unset = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        title = self.title

        description = self.description

        labels: list[str] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels

        priority: dict[str, Any] | Unset = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.to_dict()

        duration = self.duration

        due_date = self.due_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "task_id": task_id,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if labels is not UNSET:
            field_dict["labels"] = labels
        if priority is not UNSET:
            field_dict["priority"] = priority
        if duration is not UNSET:
            field_dict["duration"] = duration
        if due_date is not UNSET:
            field_dict["due_date"] = due_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_motion_task_task_params_priority import UpdateMotionTaskTaskParamsPriority

        d = dict(src_dict)
        task_id = d.pop("task_id")

        _task_type = d.pop("task_type", UNSET)
        task_type: UpdateMotionTaskTaskParamsTaskType | Unset
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_update_motion_task_task_params_task_type(_task_type)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        labels = cast(list[str], d.pop("labels", UNSET))

        _priority = d.pop("priority", UNSET)
        priority: UpdateMotionTaskTaskParamsPriority | Unset
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = UpdateMotionTaskTaskParamsPriority.from_dict(_priority)

        duration = d.pop("duration", UNSET)

        due_date = d.pop("due_date", UNSET)

        update_motion_task_task_params = cls(
            task_id=task_id,
            task_type=task_type,
            title=title,
            description=description,
            labels=labels,
            priority=priority,
            duration=duration,
            due_date=due_date,
        )

        update_motion_task_task_params.additional_properties = d
        return update_motion_task_task_params

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
