from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_linear_issue_task_params_task_type import (
    UpdateLinearIssueTaskParamsTaskType,
    check_update_linear_issue_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_linear_issue_task_params_labels_item import UpdateLinearIssueTaskParamsLabelsItem
    from ..models.update_linear_issue_task_params_priority import UpdateLinearIssueTaskParamsPriority
    from ..models.update_linear_issue_task_params_project import UpdateLinearIssueTaskParamsProject
    from ..models.update_linear_issue_task_params_state_type_0 import UpdateLinearIssueTaskParamsStateType0


T = TypeVar("T", bound="UpdateLinearIssueTaskParams")


@_attrs_define
class UpdateLinearIssueTaskParams:
    """
    Attributes:
        issue_id (str): The issue id
        task_type (UpdateLinearIssueTaskParamsTaskType | Unset):
        title (str | Unset): The issue title
        description (str | Unset): The issue description
        state (None | Unset | UpdateLinearIssueTaskParamsStateType0): The state id and display name
        project (UpdateLinearIssueTaskParamsProject | Unset): The project id and display name
        labels (list[UpdateLinearIssueTaskParamsLabelsItem] | Unset):
        priority (UpdateLinearIssueTaskParamsPriority | Unset): The priority id and display name
        assign_user_email (str | Unset): The assigned user's email
    """

    issue_id: str
    task_type: UpdateLinearIssueTaskParamsTaskType | Unset = UNSET
    title: str | Unset = UNSET
    description: str | Unset = UNSET
    state: None | Unset | UpdateLinearIssueTaskParamsStateType0 = UNSET
    project: UpdateLinearIssueTaskParamsProject | Unset = UNSET
    labels: list[UpdateLinearIssueTaskParamsLabelsItem] | Unset = UNSET
    priority: UpdateLinearIssueTaskParamsPriority | Unset = UNSET
    assign_user_email: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_linear_issue_task_params_state_type_0 import UpdateLinearIssueTaskParamsStateType0

        issue_id = self.issue_id

        task_type: str | Unset = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        title = self.title

        description = self.description

        state: dict[str, Any] | None | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        elif isinstance(self.state, UpdateLinearIssueTaskParamsStateType0):
            state = self.state.to_dict()
        else:
            state = self.state

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
                "issue_id": issue_id,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if state is not UNSET:
            field_dict["state"] = state
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
        from ..models.update_linear_issue_task_params_labels_item import UpdateLinearIssueTaskParamsLabelsItem
        from ..models.update_linear_issue_task_params_priority import UpdateLinearIssueTaskParamsPriority
        from ..models.update_linear_issue_task_params_project import UpdateLinearIssueTaskParamsProject
        from ..models.update_linear_issue_task_params_state_type_0 import UpdateLinearIssueTaskParamsStateType0

        d = dict(src_dict)
        issue_id = d.pop("issue_id")

        _task_type = d.pop("task_type", UNSET)
        task_type: UpdateLinearIssueTaskParamsTaskType | Unset
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_update_linear_issue_task_params_task_type(_task_type)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        def _parse_state(data: object) -> None | Unset | UpdateLinearIssueTaskParamsStateType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                state_type_0 = UpdateLinearIssueTaskParamsStateType0.from_dict(data)

                return state_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateLinearIssueTaskParamsStateType0, data)

        state = _parse_state(d.pop("state", UNSET))

        _project = d.pop("project", UNSET)
        project: UpdateLinearIssueTaskParamsProject | Unset
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = UpdateLinearIssueTaskParamsProject.from_dict(_project)

        _labels = d.pop("labels", UNSET)
        labels: list[UpdateLinearIssueTaskParamsLabelsItem] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for labels_item_data in _labels:
                labels_item = UpdateLinearIssueTaskParamsLabelsItem.from_dict(labels_item_data)

                labels.append(labels_item)

        _priority = d.pop("priority", UNSET)
        priority: UpdateLinearIssueTaskParamsPriority | Unset
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = UpdateLinearIssueTaskParamsPriority.from_dict(_priority)

        assign_user_email = d.pop("assign_user_email", UNSET)

        update_linear_issue_task_params = cls(
            issue_id=issue_id,
            task_type=task_type,
            title=title,
            description=description,
            state=state,
            project=project,
            labels=labels,
            priority=priority,
            assign_user_email=assign_user_email,
        )

        update_linear_issue_task_params.additional_properties = d
        return update_linear_issue_task_params

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
