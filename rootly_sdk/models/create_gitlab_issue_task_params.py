from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_gitlab_issue_task_params_issue_type import (
    CreateGitlabIssueTaskParamsIssueType,
    check_create_gitlab_issue_task_params_issue_type,
)
from ..models.create_gitlab_issue_task_params_task_type import (
    CreateGitlabIssueTaskParamsTaskType,
    check_create_gitlab_issue_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_gitlab_issue_task_params_repository import CreateGitlabIssueTaskParamsRepository


T = TypeVar("T", bound="CreateGitlabIssueTaskParams")


@_attrs_define
class CreateGitlabIssueTaskParams:
    """
    Attributes:
        issue_type (CreateGitlabIssueTaskParamsIssueType): The issue type
        title (str): The issue title
        repository (CreateGitlabIssueTaskParamsRepository):
        task_type (CreateGitlabIssueTaskParamsTaskType | Unset):
        description (str | Unset): The issue description
        labels (str | Unset): The issue labels
        due_date (str | Unset): The due date
    """

    issue_type: CreateGitlabIssueTaskParamsIssueType
    title: str
    repository: CreateGitlabIssueTaskParamsRepository
    task_type: CreateGitlabIssueTaskParamsTaskType | Unset = UNSET
    description: str | Unset = UNSET
    labels: str | Unset = UNSET
    due_date: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        issue_type: str = self.issue_type

        title = self.title

        repository = self.repository.to_dict()

        task_type: str | Unset = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        description = self.description

        labels = self.labels

        due_date = self.due_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "issue_type": issue_type,
                "title": title,
                "repository": repository,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if description is not UNSET:
            field_dict["description"] = description
        if labels is not UNSET:
            field_dict["labels"] = labels
        if due_date is not UNSET:
            field_dict["due_date"] = due_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_gitlab_issue_task_params_repository import CreateGitlabIssueTaskParamsRepository

        d = dict(src_dict)
        issue_type = check_create_gitlab_issue_task_params_issue_type(d.pop("issue_type"))

        title = d.pop("title")

        repository = CreateGitlabIssueTaskParamsRepository.from_dict(d.pop("repository"))

        _task_type = d.pop("task_type", UNSET)
        task_type: CreateGitlabIssueTaskParamsTaskType | Unset
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_create_gitlab_issue_task_params_task_type(_task_type)

        description = d.pop("description", UNSET)

        labels = d.pop("labels", UNSET)

        due_date = d.pop("due_date", UNSET)

        create_gitlab_issue_task_params = cls(
            issue_type=issue_type,
            title=title,
            repository=repository,
            task_type=task_type,
            description=description,
            labels=labels,
            due_date=due_date,
        )

        create_gitlab_issue_task_params.additional_properties = d
        return create_gitlab_issue_task_params

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
