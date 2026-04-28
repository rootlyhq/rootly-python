from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_motion_task_task_params_task_type import (
    CreateMotionTaskTaskParamsTaskType,
    check_create_motion_task_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_motion_task_task_params_priority import CreateMotionTaskTaskParamsPriority
    from ..models.create_motion_task_task_params_project import CreateMotionTaskTaskParamsProject
    from ..models.create_motion_task_task_params_status import CreateMotionTaskTaskParamsStatus
    from ..models.create_motion_task_task_params_workspace import CreateMotionTaskTaskParamsWorkspace


T = TypeVar("T", bound="CreateMotionTaskTaskParams")


@_attrs_define
class CreateMotionTaskTaskParams:
    """
    Attributes:
        workspace (CreateMotionTaskTaskParamsWorkspace):
        title (str): The task title
        task_type (CreateMotionTaskTaskParamsTaskType | Unset):
        project (CreateMotionTaskTaskParamsProject | Unset):
        status (CreateMotionTaskTaskParamsStatus | Unset):
        description (str | Unset): The task description
        labels (list[str] | Unset):
        priority (CreateMotionTaskTaskParamsPriority | Unset): The priority id and display name
        duration (str | Unset): The duration. Eg.  "NONE", "REMINDER", or a integer greater than 0.
        due_date (str | Unset): The due date
    """

    workspace: CreateMotionTaskTaskParamsWorkspace
    title: str
    task_type: CreateMotionTaskTaskParamsTaskType | Unset = UNSET
    project: CreateMotionTaskTaskParamsProject | Unset = UNSET
    status: CreateMotionTaskTaskParamsStatus | Unset = UNSET
    description: str | Unset = UNSET
    labels: list[str] | Unset = UNSET
    priority: CreateMotionTaskTaskParamsPriority | Unset = UNSET
    duration: str | Unset = UNSET
    due_date: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workspace = self.workspace.to_dict()

        title = self.title

        task_type: str | Unset = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        project: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

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
                "workspace": workspace,
                "title": title,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if project is not UNSET:
            field_dict["project"] = project
        if status is not UNSET:
            field_dict["status"] = status
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
        from ..models.create_motion_task_task_params_priority import CreateMotionTaskTaskParamsPriority
        from ..models.create_motion_task_task_params_project import CreateMotionTaskTaskParamsProject
        from ..models.create_motion_task_task_params_status import CreateMotionTaskTaskParamsStatus
        from ..models.create_motion_task_task_params_workspace import CreateMotionTaskTaskParamsWorkspace

        d = dict(src_dict)
        workspace = CreateMotionTaskTaskParamsWorkspace.from_dict(d.pop("workspace"))

        title = d.pop("title")

        _task_type = d.pop("task_type", UNSET)
        task_type: CreateMotionTaskTaskParamsTaskType | Unset
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_create_motion_task_task_params_task_type(_task_type)

        _project = d.pop("project", UNSET)
        project: CreateMotionTaskTaskParamsProject | Unset
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = CreateMotionTaskTaskParamsProject.from_dict(_project)

        _status = d.pop("status", UNSET)
        status: CreateMotionTaskTaskParamsStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CreateMotionTaskTaskParamsStatus.from_dict(_status)

        description = d.pop("description", UNSET)

        labels = cast(list[str], d.pop("labels", UNSET))

        _priority = d.pop("priority", UNSET)
        priority: CreateMotionTaskTaskParamsPriority | Unset
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = CreateMotionTaskTaskParamsPriority.from_dict(_priority)

        duration = d.pop("duration", UNSET)

        due_date = d.pop("due_date", UNSET)

        create_motion_task_task_params = cls(
            workspace=workspace,
            title=title,
            task_type=task_type,
            project=project,
            status=status,
            description=description,
            labels=labels,
            priority=priority,
            duration=duration,
            due_date=due_date,
        )

        create_motion_task_task_params.additional_properties = d
        return create_motion_task_task_params

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
