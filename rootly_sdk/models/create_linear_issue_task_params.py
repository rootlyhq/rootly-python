from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_linear_issue_task_params_task_type import (
    CreateLinearIssueTaskParamsTaskType,
    check_create_linear_issue_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_linear_issue_task_params_labels_item import CreateLinearIssueTaskParamsLabelsItem
    from ..models.create_linear_issue_task_params_priority import CreateLinearIssueTaskParamsPriority
    from ..models.create_linear_issue_task_params_project import CreateLinearIssueTaskParamsProject
    from ..models.create_linear_issue_task_params_state import CreateLinearIssueTaskParamsState
    from ..models.create_linear_issue_task_params_team import CreateLinearIssueTaskParamsTeam


T = TypeVar("T", bound="CreateLinearIssueTaskParams")


@_attrs_define
class CreateLinearIssueTaskParams:
    """
    Attributes:
        title (str): The issue title
        team (CreateLinearIssueTaskParamsTeam): The team id and display name
        state (CreateLinearIssueTaskParamsState): The state id and display name
        task_type (CreateLinearIssueTaskParamsTaskType | Unset):
        description (str | Unset): The issue description
        project (CreateLinearIssueTaskParamsProject | Unset): The project id and display name
        labels (list[CreateLinearIssueTaskParamsLabelsItem] | Unset):
        priority (CreateLinearIssueTaskParamsPriority | Unset): The priority id and display name
        assign_user_email (str | Unset): The assigned user's email
    """

    title: str
    team: CreateLinearIssueTaskParamsTeam
    state: CreateLinearIssueTaskParamsState
    task_type: CreateLinearIssueTaskParamsTaskType | Unset = UNSET
    description: str | Unset = UNSET
    project: CreateLinearIssueTaskParamsProject | Unset = UNSET
    labels: list[CreateLinearIssueTaskParamsLabelsItem] | Unset = UNSET
    priority: CreateLinearIssueTaskParamsPriority | Unset = UNSET
    assign_user_email: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        team = self.team.to_dict()

        state = self.state.to_dict()

        task_type: str | Unset = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        description = self.description

        project: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        labels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()
                labels.append(labels_item)

        priority: dict[str, Any] | Unset = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.to_dict()

        assign_user_email = self.assign_user_email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "team": team,
                "state": state,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if description is not UNSET:
            field_dict["description"] = description
        if project is not UNSET:
            field_dict["project"] = project
        if labels is not UNSET:
            field_dict["labels"] = labels
        if priority is not UNSET:
            field_dict["priority"] = priority
        if assign_user_email is not UNSET:
            field_dict["assign_user_email"] = assign_user_email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_linear_issue_task_params_labels_item import CreateLinearIssueTaskParamsLabelsItem
        from ..models.create_linear_issue_task_params_priority import CreateLinearIssueTaskParamsPriority
        from ..models.create_linear_issue_task_params_project import CreateLinearIssueTaskParamsProject
        from ..models.create_linear_issue_task_params_state import CreateLinearIssueTaskParamsState
        from ..models.create_linear_issue_task_params_team import CreateLinearIssueTaskParamsTeam

        d = dict(src_dict)
        title = d.pop("title")

        team = CreateLinearIssueTaskParamsTeam.from_dict(d.pop("team"))

        state = CreateLinearIssueTaskParamsState.from_dict(d.pop("state"))

        _task_type = d.pop("task_type", UNSET)
        task_type: CreateLinearIssueTaskParamsTaskType | Unset
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_create_linear_issue_task_params_task_type(_task_type)

        description = d.pop("description", UNSET)

        _project = d.pop("project", UNSET)
        project: CreateLinearIssueTaskParamsProject | Unset
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = CreateLinearIssueTaskParamsProject.from_dict(_project)

        _labels = d.pop("labels", UNSET)
        labels: list[CreateLinearIssueTaskParamsLabelsItem] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for labels_item_data in _labels:
                labels_item = CreateLinearIssueTaskParamsLabelsItem.from_dict(labels_item_data)

                labels.append(labels_item)

        _priority = d.pop("priority", UNSET)
        priority: CreateLinearIssueTaskParamsPriority | Unset
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = CreateLinearIssueTaskParamsPriority.from_dict(_priority)

        assign_user_email = d.pop("assign_user_email", UNSET)

        create_linear_issue_task_params = cls(
            title=title,
            team=team,
            state=state,
            task_type=task_type,
            description=description,
            project=project,
            labels=labels,
            priority=priority,
            assign_user_email=assign_user_email,
        )

        create_linear_issue_task_params.additional_properties = d
        return create_linear_issue_task_params

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
