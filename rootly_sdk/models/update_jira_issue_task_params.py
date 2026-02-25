from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_jira_issue_task_params_task_type import (
    UpdateJiraIssueTaskParamsTaskType,
    check_update_jira_issue_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_jira_issue_task_params_priority import UpdateJiraIssueTaskParamsPriority
    from ..models.update_jira_issue_task_params_status import UpdateJiraIssueTaskParamsStatus


T = TypeVar("T", bound="UpdateJiraIssueTaskParams")


@_attrs_define
class UpdateJiraIssueTaskParams:
    """
    Attributes:
        issue_id (str): The issue id
        project_key (str): The project key
        task_type (Union[Unset, UpdateJiraIssueTaskParamsTaskType]):
        title (Union[Unset, str]): The issue title
        description (Union[Unset, str]): The issue description
        labels (Union[Unset, str]): The issue labels
        assign_user_email (Union[Unset, str]): The assigned user's email
        reporter_user_email (Union[Unset, str]): The reporter user's email
        due_date (Union[Unset, str]): The due date
        priority (Union[Unset, UpdateJiraIssueTaskParamsPriority]): The priority id and display name
        status (Union[Unset, UpdateJiraIssueTaskParamsStatus]): The status id and display name
        custom_fields_mapping (Union[None, Unset, str]): Custom field mappings. Can contain liquid markup and need to be
            valid JSON
        update_payload (Union[None, Unset, str]): Update payload. Can contain liquid markup and need to be valid JSON
    """

    issue_id: str
    project_key: str
    task_type: Unset | UpdateJiraIssueTaskParamsTaskType = UNSET
    title: Unset | str = UNSET
    description: Unset | str = UNSET
    labels: Unset | str = UNSET
    assign_user_email: Unset | str = UNSET
    reporter_user_email: Unset | str = UNSET
    due_date: Unset | str = UNSET
    priority: Union[Unset, "UpdateJiraIssueTaskParamsPriority"] = UNSET
    status: Union[Unset, "UpdateJiraIssueTaskParamsStatus"] = UNSET
    custom_fields_mapping: None | Unset | str = UNSET
    update_payload: None | Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        issue_id = self.issue_id

        project_key = self.project_key

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        title = self.title

        description = self.description

        labels = self.labels

        assign_user_email = self.assign_user_email

        reporter_user_email = self.reporter_user_email

        due_date = self.due_date

        priority: Unset | dict[str, Any] = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.to_dict()

        status: Unset | dict[str, Any] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        custom_fields_mapping: None | Unset | str
        if isinstance(self.custom_fields_mapping, Unset):
            custom_fields_mapping = UNSET
        else:
            custom_fields_mapping = self.custom_fields_mapping

        update_payload: None | Unset | str
        if isinstance(self.update_payload, Unset):
            update_payload = UNSET
        else:
            update_payload = self.update_payload

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "issue_id": issue_id,
                "project_key": project_key,
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
        if assign_user_email is not UNSET:
            field_dict["assign_user_email"] = assign_user_email
        if reporter_user_email is not UNSET:
            field_dict["reporter_user_email"] = reporter_user_email
        if due_date is not UNSET:
            field_dict["due_date"] = due_date
        if priority is not UNSET:
            field_dict["priority"] = priority
        if status is not UNSET:
            field_dict["status"] = status
        if custom_fields_mapping is not UNSET:
            field_dict["custom_fields_mapping"] = custom_fields_mapping
        if update_payload is not UNSET:
            field_dict["update_payload"] = update_payload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_jira_issue_task_params_priority import UpdateJiraIssueTaskParamsPriority
        from ..models.update_jira_issue_task_params_status import UpdateJiraIssueTaskParamsStatus

        d = dict(src_dict)
        issue_id = d.pop("issue_id")

        project_key = d.pop("project_key")

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | UpdateJiraIssueTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_update_jira_issue_task_params_task_type(_task_type)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        labels = d.pop("labels", UNSET)

        assign_user_email = d.pop("assign_user_email", UNSET)

        reporter_user_email = d.pop("reporter_user_email", UNSET)

        due_date = d.pop("due_date", UNSET)

        _priority = d.pop("priority", UNSET)
        priority: Unset | UpdateJiraIssueTaskParamsPriority
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = UpdateJiraIssueTaskParamsPriority.from_dict(_priority)

        _status = d.pop("status", UNSET)
        status: Unset | UpdateJiraIssueTaskParamsStatus
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = UpdateJiraIssueTaskParamsStatus.from_dict(_status)

        def _parse_custom_fields_mapping(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        custom_fields_mapping = _parse_custom_fields_mapping(d.pop("custom_fields_mapping", UNSET))

        def _parse_update_payload(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        update_payload = _parse_update_payload(d.pop("update_payload", UNSET))

        update_jira_issue_task_params = cls(
            issue_id=issue_id,
            project_key=project_key,
            task_type=task_type,
            title=title,
            description=description,
            labels=labels,
            assign_user_email=assign_user_email,
            reporter_user_email=reporter_user_email,
            due_date=due_date,
            priority=priority,
            status=status,
            custom_fields_mapping=custom_fields_mapping,
            update_payload=update_payload,
        )

        update_jira_issue_task_params.additional_properties = d
        return update_jira_issue_task_params

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
