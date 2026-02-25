from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.incident_action_item_kind import IncidentActionItemKind, check_incident_action_item_kind
from ..models.incident_action_item_priority import IncidentActionItemPriority, check_incident_action_item_priority
from ..models.incident_action_item_status import IncidentActionItemStatus, check_incident_action_item_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_flat_response import UserFlatResponse


T = TypeVar("T", bound="IncidentActionItem")


@_attrs_define
class IncidentActionItem:
    """
    Attributes:
        summary (str): The summary of the action item
        created_at (str): Date of creation
        updated_at (str): Date of last update
        description (Union[None, Unset, str]): The description of incident action item
        kind (Union[Unset, IncidentActionItemKind]): The kind of the action item
        assigned_to (Union[Unset, UserFlatResponse]): Flat user object as returned by serializer
        assigned_to_group_ids (Union[None, Unset, list[str]]): IDs of groups you wish to assign this action item
        priority (Union[Unset, IncidentActionItemPriority]): The priority of the action item
        status (Union[Unset, IncidentActionItemStatus]): The status of the action item
        due_date (Union[None, Unset, str]): The due date of the action item
        jira_issue_id (Union[None, Unset, str]): The Jira issue ID.
        jira_issue_key (Union[None, Unset, str]): The Jira issue key.
        jira_issue_url (Union[None, Unset, str]): The Jira issue URL.
    """

    summary: str
    created_at: str
    updated_at: str
    description: None | Unset | str = UNSET
    kind: Unset | IncidentActionItemKind = UNSET
    assigned_to: Union[Unset, "UserFlatResponse"] = UNSET
    assigned_to_group_ids: None | Unset | list[str] = UNSET
    priority: Unset | IncidentActionItemPriority = UNSET
    status: Unset | IncidentActionItemStatus = UNSET
    due_date: None | Unset | str = UNSET
    jira_issue_id: None | Unset | str = UNSET
    jira_issue_key: None | Unset | str = UNSET
    jira_issue_url: None | Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        summary = self.summary

        created_at = self.created_at

        updated_at = self.updated_at

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        kind: Unset | str = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        assigned_to: Unset | dict[str, Any] = UNSET
        if not isinstance(self.assigned_to, Unset):
            assigned_to = self.assigned_to.to_dict()

        assigned_to_group_ids: None | Unset | list[str]
        if isinstance(self.assigned_to_group_ids, Unset):
            assigned_to_group_ids = UNSET
        elif isinstance(self.assigned_to_group_ids, list):
            assigned_to_group_ids = self.assigned_to_group_ids

        else:
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
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "summary": summary,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if kind is not UNSET:
            field_dict["kind"] = kind
        if assigned_to is not UNSET:
            field_dict["assigned_to"] = assigned_to
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
        from ..models.user_flat_response import UserFlatResponse

        d = dict(src_dict)
        summary = d.pop("summary")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        description = _parse_description(d.pop("description", UNSET))

        _kind = d.pop("kind", UNSET)
        kind: Unset | IncidentActionItemKind
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_incident_action_item_kind(_kind)

        _assigned_to = d.pop("assigned_to", UNSET)
        assigned_to: Unset | UserFlatResponse
        if isinstance(_assigned_to, Unset):
            assigned_to = UNSET
        else:
            assigned_to = UserFlatResponse.from_dict(_assigned_to)

        def _parse_assigned_to_group_ids(data: object) -> None | Unset | list[str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                assigned_to_group_ids_type_0 = cast(list[str], data)

                return assigned_to_group_ids_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | list[str], data)

        assigned_to_group_ids = _parse_assigned_to_group_ids(d.pop("assigned_to_group_ids", UNSET))

        _priority = d.pop("priority", UNSET)
        priority: Unset | IncidentActionItemPriority
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = check_incident_action_item_priority(_priority)

        _status = d.pop("status", UNSET)
        status: Unset | IncidentActionItemStatus
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_incident_action_item_status(_status)

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

        incident_action_item = cls(
            summary=summary,
            created_at=created_at,
            updated_at=updated_at,
            description=description,
            kind=kind,
            assigned_to=assigned_to,
            assigned_to_group_ids=assigned_to_group_ids,
            priority=priority,
            status=status,
            due_date=due_date,
            jira_issue_id=jira_issue_id,
            jira_issue_key=jira_issue_key,
            jira_issue_url=jira_issue_url,
        )

        incident_action_item.additional_properties = d
        return incident_action_item

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
