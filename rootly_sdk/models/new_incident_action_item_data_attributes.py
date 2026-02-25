from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.new_incident_action_item_data_attributes_kind import (
    NewIncidentActionItemDataAttributesKind,
    check_new_incident_action_item_data_attributes_kind,
)
from ..models.new_incident_action_item_data_attributes_priority import (
    NewIncidentActionItemDataAttributesPriority,
    check_new_incident_action_item_data_attributes_priority,
)
from ..models.new_incident_action_item_data_attributes_status import (
    NewIncidentActionItemDataAttributesStatus,
    check_new_incident_action_item_data_attributes_status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="NewIncidentActionItemDataAttributes")


@_attrs_define
class NewIncidentActionItemDataAttributes:
    """
    Attributes:
        summary (str): The summary of the action item
        description (Union[None, Unset, str]): The description of the action item
        kind (Union[Unset, NewIncidentActionItemDataAttributesKind]): The kind of the action item
        assigned_to_user_id (Union[None, Unset, int]): ID of user you wish to assign this action item
        assigned_to_group_ids (Union[Unset, list[str]]): IDs of groups you wish to assign this action item
        priority (Union[Unset, NewIncidentActionItemDataAttributesPriority]): The priority of the action item
        status (Union[Unset, NewIncidentActionItemDataAttributesStatus]): The status of the action item
        due_date (Union[None, Unset, str]): The due date of the action item
        jira_issue_id (Union[None, Unset, str]): The Jira issue ID.
        jira_issue_key (Union[None, Unset, str]): The Jira issue key.
        jira_issue_url (Union[None, Unset, str]): The Jira issue URL.
    """

    summary: str
    description: None | Unset | str = UNSET
    kind: Unset | NewIncidentActionItemDataAttributesKind = UNSET
    assigned_to_user_id: None | Unset | int = UNSET
    assigned_to_group_ids: Unset | list[str] = UNSET
    priority: Unset | NewIncidentActionItemDataAttributesPriority = UNSET
    status: Unset | NewIncidentActionItemDataAttributesStatus = UNSET
    due_date: None | Unset | str = UNSET
    jira_issue_id: None | Unset | str = UNSET
    jira_issue_key: None | Unset | str = UNSET
    jira_issue_url: None | Unset | str = UNSET

    def to_dict(self) -> dict[str, Any]:
        summary = self.summary

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        kind: Unset | str = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        assigned_to_user_id: None | Unset | int
        if isinstance(self.assigned_to_user_id, Unset):
            assigned_to_user_id = UNSET
        else:
            assigned_to_user_id = self.assigned_to_user_id

        assigned_to_group_ids: Unset | list[str] = UNSET
        if not isinstance(self.assigned_to_group_ids, Unset):
            assigned_to_group_ids = self.assigned_to_group_ids

        priority: Unset | str = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority

        status: Unset | str = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        due_date: None | Unset | str
        if isinstance(self.due_date, Unset):
            due_date = UNSET
        else:
            due_date = self.due_date

        jira_issue_id: None | Unset | str
        if isinstance(self.jira_issue_id, Unset):
            jira_issue_id = UNSET
        else:
            jira_issue_id = self.jira_issue_id

        jira_issue_key: None | Unset | str
        if isinstance(self.jira_issue_key, Unset):
            jira_issue_key = UNSET
        else:
            jira_issue_key = self.jira_issue_key

        jira_issue_url: None | Unset | str
        if isinstance(self.jira_issue_url, Unset):
            jira_issue_url = UNSET
        else:
            jira_issue_url = self.jira_issue_url

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "summary": summary,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if kind is not UNSET:
            field_dict["kind"] = kind
        if assigned_to_user_id is not UNSET:
            field_dict["assigned_to_user_id"] = assigned_to_user_id
        if assigned_to_group_ids is not UNSET:
            field_dict["assigned_to_group_ids"] = assigned_to_group_ids
        if priority is not UNSET:
            field_dict["priority"] = priority
        if status is not UNSET:
            field_dict["status"] = status
        if due_date is not UNSET:
            field_dict["due_date"] = due_date
        if jira_issue_id is not UNSET:
            field_dict["jira_issue_id"] = jira_issue_id
        if jira_issue_key is not UNSET:
            field_dict["jira_issue_key"] = jira_issue_key
        if jira_issue_url is not UNSET:
            field_dict["jira_issue_url"] = jira_issue_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        summary = d.pop("summary")

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        description = _parse_description(d.pop("description", UNSET))

        _kind = d.pop("kind", UNSET)
        kind: Unset | NewIncidentActionItemDataAttributesKind
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_new_incident_action_item_data_attributes_kind(_kind)

        def _parse_assigned_to_user_id(data: object) -> None | Unset | int:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | int, data)

        assigned_to_user_id = _parse_assigned_to_user_id(d.pop("assigned_to_user_id", UNSET))

        assigned_to_group_ids = cast(list[str], d.pop("assigned_to_group_ids", UNSET))

        _priority = d.pop("priority", UNSET)
        priority: Unset | NewIncidentActionItemDataAttributesPriority
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = check_new_incident_action_item_data_attributes_priority(_priority)

        _status = d.pop("status", UNSET)
        status: Unset | NewIncidentActionItemDataAttributesStatus
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_new_incident_action_item_data_attributes_status(_status)

        def _parse_due_date(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        due_date = _parse_due_date(d.pop("due_date", UNSET))

        def _parse_jira_issue_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        jira_issue_id = _parse_jira_issue_id(d.pop("jira_issue_id", UNSET))

        def _parse_jira_issue_key(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        jira_issue_key = _parse_jira_issue_key(d.pop("jira_issue_key", UNSET))

        def _parse_jira_issue_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        jira_issue_url = _parse_jira_issue_url(d.pop("jira_issue_url", UNSET))

        new_incident_action_item_data_attributes = cls(
            summary=summary,
            description=description,
            kind=kind,
            assigned_to_user_id=assigned_to_user_id,
            assigned_to_group_ids=assigned_to_group_ids,
            priority=priority,
            status=status,
            due_date=due_date,
            jira_issue_id=jira_issue_id,
            jira_issue_key=jira_issue_key,
            jira_issue_url=jira_issue_url,
        )

        return new_incident_action_item_data_attributes
