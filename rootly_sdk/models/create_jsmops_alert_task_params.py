from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_jsmops_alert_task_params_priority import (
    CreateJsmopsAlertTaskParamsPriority,
    check_create_jsmops_alert_task_params_priority,
)
from ..models.create_jsmops_alert_task_params_task_type import (
    CreateJsmopsAlertTaskParamsTaskType,
    check_create_jsmops_alert_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_jsmops_alert_task_params_escalations_item import CreateJsmopsAlertTaskParamsEscalationsItem
    from ..models.create_jsmops_alert_task_params_schedules_item import CreateJsmopsAlertTaskParamsSchedulesItem
    from ..models.create_jsmops_alert_task_params_teams_item import CreateJsmopsAlertTaskParamsTeamsItem
    from ..models.create_jsmops_alert_task_params_users_item import CreateJsmopsAlertTaskParamsUsersItem


T = TypeVar("T", bound="CreateJsmopsAlertTaskParams")


@_attrs_define
class CreateJsmopsAlertTaskParams:
    """
    Attributes:
        message (str): Message of the alert
        task_type (CreateJsmopsAlertTaskParamsTaskType | Unset):
        description (None | str | Unset): Description field of the alert that is generally used to provide a detailed
            information about the alert
        teams (list[CreateJsmopsAlertTaskParamsTeamsItem] | Unset):
        users (list[CreateJsmopsAlertTaskParamsUsersItem] | Unset):
        schedules (list[CreateJsmopsAlertTaskParamsSchedulesItem] | Unset):
        escalations (list[CreateJsmopsAlertTaskParamsEscalationsItem] | Unset):
        priority (CreateJsmopsAlertTaskParamsPriority | Unset):  Default: 'P3'.
        details (None | str | Unset): Details payload. Can contain liquid markup and need to be valid JSON
    """

    message: str
    task_type: CreateJsmopsAlertTaskParamsTaskType | Unset = UNSET
    description: None | str | Unset = UNSET
    teams: list[CreateJsmopsAlertTaskParamsTeamsItem] | Unset = UNSET
    users: list[CreateJsmopsAlertTaskParamsUsersItem] | Unset = UNSET
    schedules: list[CreateJsmopsAlertTaskParamsSchedulesItem] | Unset = UNSET
    escalations: list[CreateJsmopsAlertTaskParamsEscalationsItem] | Unset = UNSET
    priority: CreateJsmopsAlertTaskParamsPriority | Unset = "P3"
    details: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        task_type: str | Unset = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        teams: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.teams, Unset):
            teams = []
            for teams_item_data in self.teams:
                teams_item = teams_item_data.to_dict()
                teams.append(teams_item)

        users: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()
                users.append(users_item)

        schedules: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.schedules, Unset):
            schedules = []
            for schedules_item_data in self.schedules:
                schedules_item = schedules_item_data.to_dict()
                schedules.append(schedules_item)

        escalations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.escalations, Unset):
            escalations = []
            for escalations_item_data in self.escalations:
                escalations_item = escalations_item_data.to_dict()
                escalations.append(escalations_item)

        priority: str | Unset = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority

        details: None | str | Unset
        if isinstance(self.details, Unset):
            details = UNSET
        else:
            details = self.details

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if description is not UNSET:
            field_dict["description"] = description
        if teams is not UNSET:
            field_dict["teams"] = teams
        if users is not UNSET:
            field_dict["users"] = users
        if schedules is not UNSET:
            field_dict["schedules"] = schedules
        if escalations is not UNSET:
            field_dict["escalations"] = escalations
        if priority is not UNSET:
            field_dict["priority"] = priority
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_jsmops_alert_task_params_escalations_item import CreateJsmopsAlertTaskParamsEscalationsItem
        from ..models.create_jsmops_alert_task_params_schedules_item import CreateJsmopsAlertTaskParamsSchedulesItem
        from ..models.create_jsmops_alert_task_params_teams_item import CreateJsmopsAlertTaskParamsTeamsItem
        from ..models.create_jsmops_alert_task_params_users_item import CreateJsmopsAlertTaskParamsUsersItem

        d = dict(src_dict)
        message = d.pop("message")

        _task_type = d.pop("task_type", UNSET)
        task_type: CreateJsmopsAlertTaskParamsTaskType | Unset
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_create_jsmops_alert_task_params_task_type(_task_type)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _teams = d.pop("teams", UNSET)
        teams: list[CreateJsmopsAlertTaskParamsTeamsItem] | Unset = UNSET
        if _teams is not UNSET:
            teams = []
            for teams_item_data in _teams:
                teams_item = CreateJsmopsAlertTaskParamsTeamsItem.from_dict(teams_item_data)

                teams.append(teams_item)

        _users = d.pop("users", UNSET)
        users: list[CreateJsmopsAlertTaskParamsUsersItem] | Unset = UNSET
        if _users is not UNSET:
            users = []
            for users_item_data in _users:
                users_item = CreateJsmopsAlertTaskParamsUsersItem.from_dict(users_item_data)

                users.append(users_item)

        _schedules = d.pop("schedules", UNSET)
        schedules: list[CreateJsmopsAlertTaskParamsSchedulesItem] | Unset = UNSET
        if _schedules is not UNSET:
            schedules = []
            for schedules_item_data in _schedules:
                schedules_item = CreateJsmopsAlertTaskParamsSchedulesItem.from_dict(schedules_item_data)

                schedules.append(schedules_item)

        _escalations = d.pop("escalations", UNSET)
        escalations: list[CreateJsmopsAlertTaskParamsEscalationsItem] | Unset = UNSET
        if _escalations is not UNSET:
            escalations = []
            for escalations_item_data in _escalations:
                escalations_item = CreateJsmopsAlertTaskParamsEscalationsItem.from_dict(escalations_item_data)

                escalations.append(escalations_item)

        _priority = d.pop("priority", UNSET)
        priority: CreateJsmopsAlertTaskParamsPriority | Unset
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = check_create_jsmops_alert_task_params_priority(_priority)

        def _parse_details(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        details = _parse_details(d.pop("details", UNSET))

        create_jsmops_alert_task_params = cls(
            message=message,
            task_type=task_type,
            description=description,
            teams=teams,
            users=users,
            schedules=schedules,
            escalations=escalations,
            priority=priority,
            details=details,
        )

        create_jsmops_alert_task_params.additional_properties = d
        return create_jsmops_alert_task_params

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
