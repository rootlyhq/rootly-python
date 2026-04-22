from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_opsgenie_alert_task_params_priority import (
    CreateOpsgenieAlertTaskParamsPriority,
    check_create_opsgenie_alert_task_params_priority,
)
from ..models.create_opsgenie_alert_task_params_task_type import (
    CreateOpsgenieAlertTaskParamsTaskType,
    check_create_opsgenie_alert_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_opsgenie_alert_task_params_escalations_item import CreateOpsgenieAlertTaskParamsEscalationsItem
    from ..models.create_opsgenie_alert_task_params_schedules_item import CreateOpsgenieAlertTaskParamsSchedulesItem
    from ..models.create_opsgenie_alert_task_params_teams_item import CreateOpsgenieAlertTaskParamsTeamsItem
    from ..models.create_opsgenie_alert_task_params_users_item import CreateOpsgenieAlertTaskParamsUsersItem


T = TypeVar("T", bound="CreateOpsgenieAlertTaskParams")


@_attrs_define
class CreateOpsgenieAlertTaskParams:
    """
    Attributes:
        message (str): Message of the alert
        task_type (CreateOpsgenieAlertTaskParamsTaskType | Unset):
        description (str | Unset): Description field of the alert that is generally used to provide a detailed
            information about the alert
        teams (list[CreateOpsgenieAlertTaskParamsTeamsItem] | Unset):
        users (list[CreateOpsgenieAlertTaskParamsUsersItem] | Unset):
        schedules (list[CreateOpsgenieAlertTaskParamsSchedulesItem] | Unset):
        escalations (list[CreateOpsgenieAlertTaskParamsEscalationsItem] | Unset):
        priority (CreateOpsgenieAlertTaskParamsPriority | Unset):  Default: 'P1'.
        details (None | str | Unset): Details payload. Can contain liquid markup and need to be valid JSON
    """

    message: str
    task_type: CreateOpsgenieAlertTaskParamsTaskType | Unset = UNSET
    description: str | Unset = UNSET
    teams: list[CreateOpsgenieAlertTaskParamsTeamsItem] | Unset = UNSET
    users: list[CreateOpsgenieAlertTaskParamsUsersItem] | Unset = UNSET
    schedules: list[CreateOpsgenieAlertTaskParamsSchedulesItem] | Unset = UNSET
    escalations: list[CreateOpsgenieAlertTaskParamsEscalationsItem] | Unset = UNSET
    priority: CreateOpsgenieAlertTaskParamsPriority | Unset = "P1"
    details: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        task_type: str | Unset = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

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
        from ..models.create_opsgenie_alert_task_params_escalations_item import (
            CreateOpsgenieAlertTaskParamsEscalationsItem,
        )
        from ..models.create_opsgenie_alert_task_params_schedules_item import CreateOpsgenieAlertTaskParamsSchedulesItem
        from ..models.create_opsgenie_alert_task_params_teams_item import CreateOpsgenieAlertTaskParamsTeamsItem
        from ..models.create_opsgenie_alert_task_params_users_item import CreateOpsgenieAlertTaskParamsUsersItem

        d = dict(src_dict)
        message = d.pop("message")

        _task_type = d.pop("task_type", UNSET)
        task_type: CreateOpsgenieAlertTaskParamsTaskType | Unset
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_create_opsgenie_alert_task_params_task_type(_task_type)

        description = d.pop("description", UNSET)

        _teams = d.pop("teams", UNSET)
        teams: list[CreateOpsgenieAlertTaskParamsTeamsItem] | Unset = UNSET
        if _teams is not UNSET:
            teams = []
            for teams_item_data in _teams:
                teams_item = CreateOpsgenieAlertTaskParamsTeamsItem.from_dict(teams_item_data)

                teams.append(teams_item)

        _users = d.pop("users", UNSET)
        users: list[CreateOpsgenieAlertTaskParamsUsersItem] | Unset = UNSET
        if _users is not UNSET:
            users = []
            for users_item_data in _users:
                users_item = CreateOpsgenieAlertTaskParamsUsersItem.from_dict(users_item_data)

                users.append(users_item)

        _schedules = d.pop("schedules", UNSET)
        schedules: list[CreateOpsgenieAlertTaskParamsSchedulesItem] | Unset = UNSET
        if _schedules is not UNSET:
            schedules = []
            for schedules_item_data in _schedules:
                schedules_item = CreateOpsgenieAlertTaskParamsSchedulesItem.from_dict(schedules_item_data)

                schedules.append(schedules_item)

        _escalations = d.pop("escalations", UNSET)
        escalations: list[CreateOpsgenieAlertTaskParamsEscalationsItem] | Unset = UNSET
        if _escalations is not UNSET:
            escalations = []
            for escalations_item_data in _escalations:
                escalations_item = CreateOpsgenieAlertTaskParamsEscalationsItem.from_dict(escalations_item_data)

                escalations.append(escalations_item)

        _priority = d.pop("priority", UNSET)
        priority: CreateOpsgenieAlertTaskParamsPriority | Unset
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = check_create_opsgenie_alert_task_params_priority(_priority)

        def _parse_details(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        details = _parse_details(d.pop("details", UNSET))

        create_opsgenie_alert_task_params = cls(
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

        create_opsgenie_alert_task_params.additional_properties = d
        return create_opsgenie_alert_task_params

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
