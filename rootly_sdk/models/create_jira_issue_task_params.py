from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_jira_issue_task_params_task_type import (
    CreateJiraIssueTaskParamsTaskType,
    check_create_jira_issue_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_jira_issue_task_params_integration import CreateJiraIssueTaskParamsIntegration
    from ..models.create_jira_issue_task_params_issue_type import CreateJiraIssueTaskParamsIssueType
    from ..models.create_jira_issue_task_params_priority import CreateJiraIssueTaskParamsPriority
    from ..models.create_jira_issue_task_params_status import CreateJiraIssueTaskParamsStatus


T = TypeVar("T", bound="CreateJiraIssueTaskParams")


@_attrs_define
class CreateJiraIssueTaskParams:
    """
    Attributes:
        title (str): The issue title
        project_key (str): The project key
        issue_type (CreateJiraIssueTaskParamsIssueType): The issue type id and display name
        task_type (CreateJiraIssueTaskParamsTaskType | Unset):
        integration (CreateJiraIssueTaskParamsIntegration | Unset): Specify integration id if you have more than one
            Jira instance
        description (str | Unset): The issue description
        labels (str | Unset): The issue labels
        assign_user_email (str | Unset): The assigned user's email
        reporter_user_email (str | Unset): The reporter user's email
        due_date (str | Unset): The due date
        priority (CreateJiraIssueTaskParamsPriority | Unset): The priority id and display name
        status (CreateJiraIssueTaskParamsStatus | Unset): The status id and display name
        custom_fields_mapping (None | str | Unset): Custom field mappings. Can contain liquid markup and need to be
            valid JSON
        update_payload (None | str | Unset): Update payload. Can contain liquid markup and need to be valid JSON
    """

    title: str
    project_key: str
    issue_type: CreateJiraIssueTaskParamsIssueType
    task_type: CreateJiraIssueTaskParamsTaskType | Unset = UNSET
    integration: CreateJiraIssueTaskParamsIntegration | Unset = UNSET
    description: str | Unset = UNSET
    labels: str | Unset = UNSET
    assign_user_email: str | Unset = UNSET
    reporter_user_email: str | Unset = UNSET
    due_date: str | Unset = UNSET
    priority: CreateJiraIssueTaskParamsPriority | Unset = UNSET
    status: CreateJiraIssueTaskParamsStatus | Unset = UNSET
    custom_fields_mapping: None | str | Unset = UNSET
    update_payload: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        project_key = self.project_key

        issue_type = self.issue_type.to_dict()

        task_type: str | Unset = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        integration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.integration, Unset):
            integration = self.integration.to_dict()

        description = self.description

        labels = self.labels

        assign_user_email = self.assign_user_email

        reporter_user_email = self.reporter_user_email

        due_date = self.due_date

        priority: dict[str, Any] | Unset = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.to_dict()

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        custom_fields_mapping: None | str | Unset
        if isinstance(self.custom_fields_mapping, Unset):
            custom_fields_mapping = UNSET
        else:
            custom_fields_mapping = self.custom_fields_mapping

        update_payload: None | str | Unset
        if isinstance(self.update_payload, Unset):
            update_payload = UNSET
        else:
            update_payload = self.update_payload

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "project_key": project_key,
                "issue_type": issue_type,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if integration is not UNSET:
            field_dict["integration"] = integration
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
        from ..models.create_jira_issue_task_params_integration import CreateJiraIssueTaskParamsIntegration
        from ..models.create_jira_issue_task_params_issue_type import CreateJiraIssueTaskParamsIssueType
        from ..models.create_jira_issue_task_params_priority import CreateJiraIssueTaskParamsPriority
        from ..models.create_jira_issue_task_params_status import CreateJiraIssueTaskParamsStatus

        d = dict(src_dict)
        title = d.pop("title")

        project_key = d.pop("project_key")

        issue_type = CreateJiraIssueTaskParamsIssueType.from_dict(d.pop("issue_type"))

        _task_type = d.pop("task_type", UNSET)
        task_type: CreateJiraIssueTaskParamsTaskType | Unset
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_create_jira_issue_task_params_task_type(_task_type)

        _integration = d.pop("integration", UNSET)
        integration: CreateJiraIssueTaskParamsIntegration | Unset
        if isinstance(_integration, Unset):
            integration = UNSET
        else:
            integration = CreateJiraIssueTaskParamsIntegration.from_dict(_integration)

        description = d.pop("description", UNSET)

        labels = d.pop("labels", UNSET)

        assign_user_email = d.pop("assign_user_email", UNSET)

        reporter_user_email = d.pop("reporter_user_email", UNSET)

        due_date = d.pop("due_date", UNSET)

        _priority = d.pop("priority", UNSET)
        priority: CreateJiraIssueTaskParamsPriority | Unset
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = CreateJiraIssueTaskParamsPriority.from_dict(_priority)

        _status = d.pop("status", UNSET)
        status: CreateJiraIssueTaskParamsStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CreateJiraIssueTaskParamsStatus.from_dict(_status)

        def _parse_custom_fields_mapping(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom_fields_mapping = _parse_custom_fields_mapping(d.pop("custom_fields_mapping", UNSET))

        def _parse_update_payload(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        update_payload = _parse_update_payload(d.pop("update_payload", UNSET))

        create_jira_issue_task_params = cls(
            title=title,
            project_key=project_key,
            issue_type=issue_type,
            task_type=task_type,
            integration=integration,
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

        create_jira_issue_task_params.additional_properties = d
        return create_jira_issue_task_params

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
