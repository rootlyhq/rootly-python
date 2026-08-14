from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.page_opsgenie_on_call_responders_task_params_priority import (
    PageOpsgenieOnCallRespondersTaskParamsPriority,
    check_page_opsgenie_on_call_responders_task_params_priority,
)
from ..models.page_opsgenie_on_call_responders_task_params_task_type import (
    PageOpsgenieOnCallRespondersTaskParamsTaskType,
    check_page_opsgenie_on_call_responders_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.page_opsgenie_on_call_responders_task_params_teams_item import (
        PageOpsgenieOnCallRespondersTaskParamsTeamsItem,
    )
    from ..models.page_opsgenie_on_call_responders_task_params_users_item import (
        PageOpsgenieOnCallRespondersTaskParamsUsersItem,
    )


T = TypeVar("T", bound="PageOpsgenieOnCallRespondersTaskParams")


@_attrs_define
class PageOpsgenieOnCallRespondersTaskParams:
    """
    Attributes:
        task_type (Union[Unset, PageOpsgenieOnCallRespondersTaskParamsTaskType]):
        title (Union[None, Unset, str]): Incident title.
        message (Union[Unset, str]): Message of the incident
        description (Union[Unset, str]): Description field of the incident that is generally used to provide a detailed
            information about the incident
        teams (Union[Unset, list['PageOpsgenieOnCallRespondersTaskParamsTeamsItem']]):
        users (Union[Unset, list['PageOpsgenieOnCallRespondersTaskParamsUsersItem']]):
        priority (Union[Unset, PageOpsgenieOnCallRespondersTaskParamsPriority]):  Default: 'P1'.
    """

    task_type: Unset | PageOpsgenieOnCallRespondersTaskParamsTaskType = UNSET
    title: None | Unset | str = UNSET
    message: Unset | str = UNSET
    description: Unset | str = UNSET
    teams: Unset | list["PageOpsgenieOnCallRespondersTaskParamsTeamsItem"] = UNSET
    users: Unset | list["PageOpsgenieOnCallRespondersTaskParamsUsersItem"] = UNSET
    priority: Unset | PageOpsgenieOnCallRespondersTaskParamsPriority = "P1"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        title: None | Unset | str
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        message = self.message

        description = self.description

        teams: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.teams, Unset):
            teams = []
            for teams_item_data in self.teams:
                teams_item = teams_item_data.to_dict()
                teams.append(teams_item)

        users: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()
                users.append(users_item)

        priority: Unset | str = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if title is not UNSET:
            field_dict["title"] = title
        if message is not UNSET:
            field_dict["message"] = message
        if description is not UNSET:
            field_dict["description"] = description
        if teams is not UNSET:
            field_dict["teams"] = teams
        if users is not UNSET:
            field_dict["users"] = users
        if priority is not UNSET:
            field_dict["priority"] = priority

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.page_opsgenie_on_call_responders_task_params_teams_item import (
            PageOpsgenieOnCallRespondersTaskParamsTeamsItem,
        )
        from ..models.page_opsgenie_on_call_responders_task_params_users_item import (
            PageOpsgenieOnCallRespondersTaskParamsUsersItem,
        )

        d = dict(src_dict)
        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | PageOpsgenieOnCallRespondersTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_page_opsgenie_on_call_responders_task_params_task_type(_task_type)

        def _parse_title(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        title = _parse_title(d.pop("title", UNSET))

        message = d.pop("message", UNSET)

        description = d.pop("description", UNSET)

        teams = []
        _teams = d.pop("teams", UNSET)
        for teams_item_data in _teams or []:
            teams_item = PageOpsgenieOnCallRespondersTaskParamsTeamsItem.from_dict(teams_item_data)

            teams.append(teams_item)

        users = []
        _users = d.pop("users", UNSET)
        for users_item_data in _users or []:
            users_item = PageOpsgenieOnCallRespondersTaskParamsUsersItem.from_dict(users_item_data)

            users.append(users_item)

        _priority = d.pop("priority", UNSET)
        priority: Unset | PageOpsgenieOnCallRespondersTaskParamsPriority
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = check_page_opsgenie_on_call_responders_task_params_priority(_priority)

        page_opsgenie_on_call_responders_task_params = cls(
            task_type=task_type,
            title=title,
            message=message,
            description=description,
            teams=teams,
            users=users,
            priority=priority,
        )

        page_opsgenie_on_call_responders_task_params.additional_properties = d
        return page_opsgenie_on_call_responders_task_params

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
