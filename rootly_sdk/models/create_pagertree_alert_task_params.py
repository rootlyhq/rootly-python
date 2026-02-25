from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_pagertree_alert_task_params_severity import (
    CreatePagertreeAlertTaskParamsSeverity,
    check_create_pagertree_alert_task_params_severity,
)
from ..models.create_pagertree_alert_task_params_task_type import (
    CreatePagertreeAlertTaskParamsTaskType,
    check_create_pagertree_alert_task_params_task_type,
)
from ..models.create_pagertree_alert_task_params_urgency import (
    CreatePagertreeAlertTaskParamsUrgency,
    check_create_pagertree_alert_task_params_urgency,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_pagertree_alert_task_params_teams_item import CreatePagertreeAlertTaskParamsTeamsItem
    from ..models.create_pagertree_alert_task_params_users_item import CreatePagertreeAlertTaskParamsUsersItem


T = TypeVar("T", bound="CreatePagertreeAlertTaskParams")


@_attrs_define
class CreatePagertreeAlertTaskParams:
    """
    Attributes:
        task_type (Union[Unset, CreatePagertreeAlertTaskParamsTaskType]):
        title (Union[Unset, str]): Title of alert as text
        description (Union[Unset, str]): Description of alert as text
        urgency (Union[Unset, CreatePagertreeAlertTaskParamsUrgency]):
        severity (Union[Unset, CreatePagertreeAlertTaskParamsSeverity]):
        teams (Union[Unset, list['CreatePagertreeAlertTaskParamsTeamsItem']]):
        users (Union[Unset, list['CreatePagertreeAlertTaskParamsUsersItem']]):
        incident (Union[Unset, bool]): Setting to true makes an alert a Pagertree incident
    """

    task_type: Unset | CreatePagertreeAlertTaskParamsTaskType = UNSET
    title: Unset | str = UNSET
    description: Unset | str = UNSET
    urgency: Unset | CreatePagertreeAlertTaskParamsUrgency = UNSET
    severity: Unset | CreatePagertreeAlertTaskParamsSeverity = UNSET
    teams: Unset | list["CreatePagertreeAlertTaskParamsTeamsItem"] = UNSET
    users: Unset | list["CreatePagertreeAlertTaskParamsUsersItem"] = UNSET
    incident: Unset | bool = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        title = self.title

        description = self.description

        urgency: Unset | str = UNSET
        if not isinstance(self.urgency, Unset):
            urgency = self.urgency

        severity: Unset | str = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity

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

        incident = self.incident

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if urgency is not UNSET:
            field_dict["urgency"] = urgency
        if severity is not UNSET:
            field_dict["severity"] = severity
        if teams is not UNSET:
            field_dict["teams"] = teams
        if users is not UNSET:
            field_dict["users"] = users
        if incident is not UNSET:
            field_dict["incident"] = incident

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_pagertree_alert_task_params_teams_item import CreatePagertreeAlertTaskParamsTeamsItem
        from ..models.create_pagertree_alert_task_params_users_item import CreatePagertreeAlertTaskParamsUsersItem

        d = dict(src_dict)
        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | CreatePagertreeAlertTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_create_pagertree_alert_task_params_task_type(_task_type)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        _urgency = d.pop("urgency", UNSET)
        urgency: Unset | CreatePagertreeAlertTaskParamsUrgency
        if isinstance(_urgency, Unset):
            urgency = UNSET
        else:
            urgency = check_create_pagertree_alert_task_params_urgency(_urgency)

        _severity = d.pop("severity", UNSET)
        severity: Unset | CreatePagertreeAlertTaskParamsSeverity
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = check_create_pagertree_alert_task_params_severity(_severity)

        teams = []
        _teams = d.pop("teams", UNSET)
        for teams_item_data in _teams or []:
            teams_item = CreatePagertreeAlertTaskParamsTeamsItem.from_dict(teams_item_data)

            teams.append(teams_item)

        users = []
        _users = d.pop("users", UNSET)
        for users_item_data in _users or []:
            users_item = CreatePagertreeAlertTaskParamsUsersItem.from_dict(users_item_data)

            users.append(users_item)

        incident = d.pop("incident", UNSET)

        create_pagertree_alert_task_params = cls(
            task_type=task_type,
            title=title,
            description=description,
            urgency=urgency,
            severity=severity,
            teams=teams,
            users=users,
            incident=incident,
        )

        create_pagertree_alert_task_params.additional_properties = d
        return create_pagertree_alert_task_params

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
