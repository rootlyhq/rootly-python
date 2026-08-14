from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

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
        task_type (Union[Unset, UpdateMotionTaskTaskParamsTaskType]):
        title (Union[Unset, str]): The task title
        description (Union[Unset, str]): The task description
        labels (Union[Unset, list[str]]):
        priority (Union[Unset, UpdateMotionTaskTaskParamsPriority]): The priority id and display name
        duration (Union[Unset, str]): The duration. Eg.  "NONE", "REMINDER", or a integer greater than 0.
        due_date (Union[Unset, str]): The due date
    """

    task_id: str
    task_type: Unset | UpdateMotionTaskTaskParamsTaskType = UNSET
    title: Unset | str = UNSET
    description: Unset | str = UNSET
    labels: Unset | list[str] = UNSET
    priority: Union[Unset, "UpdateMotionTaskTaskParamsPriority"] = UNSET
    duration: Unset | str = UNSET
    due_date: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        task_id = self.task_id

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        title = self.title

        description = self.description

        labels: Unset | list[str] = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels

        priority: Unset | dict[str, Any] = UNSET
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
        task_type: Unset | UpdateMotionTaskTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_update_motion_task_task_params_task_type(_task_type)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        labels = cast(list[str], d.pop("labels", UNSET))

        _priority = d.pop("priority", UNSET)
        priority: Unset | UpdateMotionTaskTaskParamsPriority
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
