from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_github_issue_task_params_labels_mode import (
    UpdateGithubIssueTaskParamsLabelsMode,
    check_update_github_issue_task_params_labels_mode,
)
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
        labels_mode (UpdateGithubIssueTaskParamsLabelsMode | Unset): How to apply labels. 'replace' (default) overwrites
            all existing labels. 'append' adds to existing labels without removing them. Default: 'replace'.
        issue_type (UpdateGithubIssueTaskParamsIssueType | Unset): The issue type
        custom_fields_mapping (None | str | Unset): Custom field mappings. Can contain liquid markup and need to be
            valid JSON
    """

    issue_id: str
    completion: UpdateGithubIssueTaskParamsCompletion
    task_type: UpdateGithubIssueTaskParamsTaskType | Unset = UNSET
    repository: UpdateGithubIssueTaskParamsRepository | Unset = UNSET
    title: str | Unset = UNSET
    body: str | Unset = UNSET
    labels: list[UpdateGithubIssueTaskParamsLabelsItem] | Unset = UNSET
    labels_mode: UpdateGithubIssueTaskParamsLabelsMode | Unset = "replace"
    issue_type: UpdateGithubIssueTaskParamsIssueType | Unset = UNSET
    custom_fields_mapping: None | str | Unset = UNSET
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

        labels_mode: str | Unset = UNSET
        if not isinstance(self.labels_mode, Unset):
            labels_mode = self.labels_mode

        issue_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.issue_type, Unset):
            issue_type = self.issue_type.to_dict()

        custom_fields_mapping: None | str | Unset
        if isinstance(self.custom_fields_mapping, Unset):
            custom_fields_mapping = UNSET
        else:
            custom_fields_mapping = self.custom_fields_mapping

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
        if labels_mode is not UNSET:
            field_dict["labels_mode"] = labels_mode
        if issue_type is not UNSET:
            field_dict["issue_type"] = issue_type
        if custom_fields_mapping is not UNSET:
            field_dict["custom_fields_mapping"] = custom_fields_mapping

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

        _labels_mode = d.pop("labels_mode", UNSET)
        labels_mode: UpdateGithubIssueTaskParamsLabelsMode | Unset
        if isinstance(_labels_mode, Unset):
            labels_mode = UNSET
        else:
            labels_mode = check_update_github_issue_task_params_labels_mode(_labels_mode)

        _issue_type = d.pop("issue_type", UNSET)
        issue_type: UpdateGithubIssueTaskParamsIssueType | Unset
        if isinstance(_issue_type, Unset):
            issue_type = UNSET
        else:
            issue_type = UpdateGithubIssueTaskParamsIssueType.from_dict(_issue_type)

        def _parse_custom_fields_mapping(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom_fields_mapping = _parse_custom_fields_mapping(d.pop("custom_fields_mapping", UNSET))

        update_github_issue_task_params = cls(
            issue_id=issue_id,
            completion=completion,
            task_type=task_type,
            repository=repository,
            title=title,
            body=body,
            labels=labels,
            labels_mode=labels_mode,
            issue_type=issue_type,
            custom_fields_mapping=custom_fields_mapping,
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
