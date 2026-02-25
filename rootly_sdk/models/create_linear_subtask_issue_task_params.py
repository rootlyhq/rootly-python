from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_linear_subtask_issue_task_params_task_type import (
    CreateLinearSubtaskIssueTaskParamsTaskType,
    check_create_linear_subtask_issue_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_linear_subtask_issue_task_params_labels_item import (
        CreateLinearSubtaskIssueTaskParamsLabelsItem,
    )
    from ..models.create_linear_subtask_issue_task_params_priority import CreateLinearSubtaskIssueTaskParamsPriority
    from ..models.create_linear_subtask_issue_task_params_state import CreateLinearSubtaskIssueTaskParamsState


T = TypeVar("T", bound="CreateLinearSubtaskIssueTaskParams")


@_attrs_define
class CreateLinearSubtaskIssueTaskParams:
    """
    Attributes:
        parent_issue_id (str): The parent issue
        title (str): The issue title
        state (CreateLinearSubtaskIssueTaskParamsState): The state id and display name
        task_type (Union[Unset, CreateLinearSubtaskIssueTaskParamsTaskType]):
        description (Union[Unset, str]): The issue description
        priority (Union[Unset, CreateLinearSubtaskIssueTaskParamsPriority]): The priority id and display name
        labels (Union[Unset, list['CreateLinearSubtaskIssueTaskParamsLabelsItem']]):
        assign_user_email (Union[Unset, str]): The assigned user's email
    """

    parent_issue_id: str
    title: str
    state: "CreateLinearSubtaskIssueTaskParamsState"
    task_type: Unset | CreateLinearSubtaskIssueTaskParamsTaskType = UNSET
    description: Unset | str = UNSET
    priority: Union[Unset, "CreateLinearSubtaskIssueTaskParamsPriority"] = UNSET
    labels: Unset | list["CreateLinearSubtaskIssueTaskParamsLabelsItem"] = UNSET
    assign_user_email: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parent_issue_id = self.parent_issue_id

        title = self.title

        state = self.state.to_dict()

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        description = self.description

        priority: Unset | dict[str, Any] = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.to_dict()

        labels: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()
                labels.append(labels_item)

        assign_user_email = self.assign_user_email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "parent_issue_id": parent_issue_id,
                "title": title,
                "state": state,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if description is not UNSET:
            field_dict["description"] = description
        if priority is not UNSET:
            field_dict["priority"] = priority
        if labels is not UNSET:
            field_dict["labels"] = labels
        if assign_user_email is not UNSET:
            field_dict["assign_user_email"] = assign_user_email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_linear_subtask_issue_task_params_labels_item import (
            CreateLinearSubtaskIssueTaskParamsLabelsItem,
        )
        from ..models.create_linear_subtask_issue_task_params_priority import CreateLinearSubtaskIssueTaskParamsPriority
        from ..models.create_linear_subtask_issue_task_params_state import CreateLinearSubtaskIssueTaskParamsState

        d = dict(src_dict)
        parent_issue_id = d.pop("parent_issue_id")

        title = d.pop("title")

        state = CreateLinearSubtaskIssueTaskParamsState.from_dict(d.pop("state"))

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | CreateLinearSubtaskIssueTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_create_linear_subtask_issue_task_params_task_type(_task_type)

        description = d.pop("description", UNSET)

        _priority = d.pop("priority", UNSET)
        priority: Unset | CreateLinearSubtaskIssueTaskParamsPriority
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = CreateLinearSubtaskIssueTaskParamsPriority.from_dict(_priority)

        labels = []
        _labels = d.pop("labels", UNSET)
        for labels_item_data in _labels or []:
            labels_item = CreateLinearSubtaskIssueTaskParamsLabelsItem.from_dict(labels_item_data)

            labels.append(labels_item)

        assign_user_email = d.pop("assign_user_email", UNSET)

        create_linear_subtask_issue_task_params = cls(
            parent_issue_id=parent_issue_id,
            title=title,
            state=state,
            task_type=task_type,
            description=description,
            priority=priority,
            labels=labels,
            assign_user_email=assign_user_email,
        )

        create_linear_subtask_issue_task_params.additional_properties = d
        return create_linear_subtask_issue_task_params

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
