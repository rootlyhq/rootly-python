from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_zendesk_jira_link_task_params_task_type import (
    CreateZendeskJiraLinkTaskParamsTaskType,
    check_create_zendesk_jira_link_task_params_task_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateZendeskJiraLinkTaskParams")


@_attrs_define
class CreateZendeskJiraLinkTaskParams:
    """
    Attributes:
        jira_issue_id (str): Jira Issue Id.
        jira_issue_key (str): Jira Issue Key.
        zendesk_ticket_id (str): Zendesk Ticket Id.
        task_type (Union[Unset, CreateZendeskJiraLinkTaskParamsTaskType]):
    """

    jira_issue_id: str
    jira_issue_key: str
    zendesk_ticket_id: str
    task_type: Unset | CreateZendeskJiraLinkTaskParamsTaskType = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        jira_issue_id = self.jira_issue_id

        jira_issue_key = self.jira_issue_key

        zendesk_ticket_id = self.zendesk_ticket_id

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "jira_issue_id": jira_issue_id,
                "jira_issue_key": jira_issue_key,
                "zendesk_ticket_id": zendesk_ticket_id,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        jira_issue_id = d.pop("jira_issue_id")

        jira_issue_key = d.pop("jira_issue_key")

        zendesk_ticket_id = d.pop("zendesk_ticket_id")

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | CreateZendeskJiraLinkTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_create_zendesk_jira_link_task_params_task_type(_task_type)

        create_zendesk_jira_link_task_params = cls(
            jira_issue_id=jira_issue_id,
            jira_issue_key=jira_issue_key,
            zendesk_ticket_id=zendesk_ticket_id,
            task_type=task_type,
        )

        create_zendesk_jira_link_task_params.additional_properties = d
        return create_zendesk_jira_link_task_params

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
