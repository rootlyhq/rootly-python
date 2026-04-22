from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_github_issue_task_params_task_type import (
    UpdateGithubIssueTaskParamsTaskType,
    check_update_github_issue_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_github_issue_task_params_completion import UpdateGithubIssueTaskParamsCompletion
    from ..models.update_github_issue_task_params_issue_type import UpdateGithubIssueTaskParamsIssueType
    from ..models.update_github_issue_task_params_labels_item import UpdateGithubIssueTaskParamsLabelsItem
    from ..models.update_github_issue_task_params_repository import UpdateGithubIssueTaskParamsRepository


T = TypeVar("T", bound="UpdateGithubIssueTaskParams")


@_attrs_define
class UpdateGithubIssueTaskParams:
    """
    Attributes:
        issue_id (str): The issue id
        completion (UpdateGithubIssueTaskParamsCompletion):
        task_type (UpdateGithubIssueTaskParamsTaskType | Unset):
        repository (UpdateGithubIssueTaskParamsRepository | Unset): The repository (used for loading labels and issue
            types)
        title (str | Unset): The issue title
        body (str | Unset): The issue body
        labels (list[UpdateGithubIssueTaskParamsLabelsItem] | Unset): The issue labels
        issue_type (UpdateGithubIssueTaskParamsIssueType | Unset): The issue type
    """

    issue_id: str
    completion: UpdateGithubIssueTaskParamsCompletion
    task_type: UpdateGithubIssueTaskParamsTaskType | Unset = UNSET
    repository: UpdateGithubIssueTaskParamsRepository | Unset = UNSET
    title: str | Unset = UNSET
    body: str | Unset = UNSET
    labels: list[UpdateGithubIssueTaskParamsLabelsItem] | Unset = UNSET
    issue_type: UpdateGithubIssueTaskParamsIssueType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        issue_id = self.issue_id

        completion = self.completion.to_dict()

        task_type: str | Unset = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        repository: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repository, Unset):
            repository = self.repository.to_dict()

        title = self.title

        body = self.body

        labels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()
                labels.append(labels_item)

        issue_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.issue_type, Unset):
            issue_type = self.issue_type.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "issue_id": issue_id,
                "completion": completion,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if repository is not UNSET:
            field_dict["repository"] = repository
        if title is not UNSET:
            field_dict["title"] = title
        if body is not UNSET:
            field_dict["body"] = body
        if labels is not UNSET:
            field_dict["labels"] = labels
        if issue_type is not UNSET:
            field_dict["issue_type"] = issue_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_github_issue_task_params_completion import UpdateGithubIssueTaskParamsCompletion
        from ..models.update_github_issue_task_params_issue_type import UpdateGithubIssueTaskParamsIssueType
        from ..models.update_github_issue_task_params_labels_item import UpdateGithubIssueTaskParamsLabelsItem
        from ..models.update_github_issue_task_params_repository import UpdateGithubIssueTaskParamsRepository

        d = dict(src_dict)
        issue_id = d.pop("issue_id")

        completion = UpdateGithubIssueTaskParamsCompletion.from_dict(d.pop("completion"))

        _task_type = d.pop("task_type", UNSET)
        task_type: UpdateGithubIssueTaskParamsTaskType | Unset
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_update_github_issue_task_params_task_type(_task_type)

        _repository = d.pop("repository", UNSET)
        repository: UpdateGithubIssueTaskParamsRepository | Unset
        if isinstance(_repository, Unset):
            repository = UNSET
        else:
            repository = UpdateGithubIssueTaskParamsRepository.from_dict(_repository)

        title = d.pop("title", UNSET)

        body = d.pop("body", UNSET)

        _labels = d.pop("labels", UNSET)
        labels: list[UpdateGithubIssueTaskParamsLabelsItem] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for labels_item_data in _labels:
                labels_item = UpdateGithubIssueTaskParamsLabelsItem.from_dict(labels_item_data)

                labels.append(labels_item)

        _issue_type = d.pop("issue_type", UNSET)
        issue_type: UpdateGithubIssueTaskParamsIssueType | Unset
        if isinstance(_issue_type, Unset):
            issue_type = UNSET
        else:
            issue_type = UpdateGithubIssueTaskParamsIssueType.from_dict(_issue_type)

        update_github_issue_task_params = cls(
            issue_id=issue_id,
            completion=completion,
            task_type=task_type,
            repository=repository,
            title=title,
            body=body,
            labels=labels,
            issue_type=issue_type,
        )

        update_github_issue_task_params.additional_properties = d
        return update_github_issue_task_params

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
