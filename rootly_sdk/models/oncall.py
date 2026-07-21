from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.oncall_notification_type import check_oncall_notification_type
from ..models.oncall_notification_type import OncallNotificationType
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime


T = TypeVar("T", bound="Oncall")


@_attrs_define
class Oncall:
    """
    Attributes:
        escalation_policy_id (str): ID of the escalation policy
        escalation_policy_name (str): Name of the escalation policy
        user_id (int): ID of the on-call user
        starts_at (datetime.datetime): Start datetime of the on-call shift
        ends_at (datetime.datetime): End datetime of the on-call shift
        escalation_policy_path_id (None | str | Unset): ID of the escalation policy path
        escalation_policy_path_name (None | str | Unset): Name of the escalation policy path
        notification_type (OncallNotificationType | Unset): Notification type of the escalation path (audible or quiet)
        is_default_path (bool | None | Unset): Whether this is the default escalation path
        escalation_level (int | Unset): Level within the escalation policy
        schedule_id (None | str | Unset): ID of the schedule
        schedule_name (None | str | Unset): Name of the schedule
    """

    escalation_policy_id: str
    escalation_policy_name: str
    user_id: int
    starts_at: datetime.datetime
    ends_at: datetime.datetime
    escalation_policy_path_id: None | str | Unset = UNSET
    escalation_policy_path_name: None | str | Unset = UNSET
    notification_type: OncallNotificationType | Unset = UNSET
    is_default_path: bool | None | Unset = UNSET
    escalation_level: int | Unset = UNSET
    schedule_id: None | str | Unset = UNSET
    schedule_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        escalation_policy_id = self.escalation_policy_id

        escalation_policy_name = self.escalation_policy_name

        user_id = self.user_id

        starts_at = self.starts_at.isoformat()

        ends_at = self.ends_at.isoformat()

        escalation_policy_path_id: None | str | Unset
        if isinstance(self.escalation_policy_path_id, Unset):
            escalation_policy_path_id = UNSET
        else:
            escalation_policy_path_id = self.escalation_policy_path_id

        escalation_policy_path_name: None | str | Unset
        if isinstance(self.escalation_policy_path_name, Unset):
            escalation_policy_path_name = UNSET
        else:
            escalation_policy_path_name = self.escalation_policy_path_name

        notification_type: str | Unset = UNSET
        if not isinstance(self.notification_type, Unset):
            notification_type = self.notification_type

        is_default_path: bool | None | Unset
        if isinstance(self.is_default_path, Unset):
            is_default_path = UNSET
        else:
            is_default_path = self.is_default_path

        escalation_level = self.escalation_level

        schedule_id: None | str | Unset
        if isinstance(self.schedule_id, Unset):
            schedule_id = UNSET
        else:
            schedule_id = self.schedule_id

        schedule_name: None | str | Unset
        if isinstance(self.schedule_name, Unset):
            schedule_name = UNSET
        else:
            schedule_name = self.schedule_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "escalation_policy_id": escalation_policy_id,
                "escalation_policy_name": escalation_policy_name,
                "user_id": user_id,
                "starts_at": starts_at,
                "ends_at": ends_at,
            }
        )
        if escalation_policy_path_id is not UNSET:
            field_dict["escalation_policy_path_id"] = escalation_policy_path_id
        if escalation_policy_path_name is not UNSET:
            field_dict["escalation_policy_path_name"] = escalation_policy_path_name
        if notification_type is not UNSET:
            field_dict["notification_type"] = notification_type
        if is_default_path is not UNSET:
            field_dict["is_default_path"] = is_default_path
        if escalation_level is not UNSET:
            field_dict["escalation_level"] = escalation_level
        if schedule_id is not UNSET:
            field_dict["schedule_id"] = schedule_id
        if schedule_name is not UNSET:
            field_dict["schedule_name"] = schedule_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        escalation_policy_id = d.pop("escalation_policy_id")

        escalation_policy_name = d.pop("escalation_policy_name")

        user_id = d.pop("user_id")

        starts_at = isoparse(d.pop("starts_at"))

        ends_at = isoparse(d.pop("ends_at"))

        def _parse_escalation_policy_path_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        escalation_policy_path_id = _parse_escalation_policy_path_id(d.pop("escalation_policy_path_id", UNSET))

        def _parse_escalation_policy_path_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        escalation_policy_path_name = _parse_escalation_policy_path_name(d.pop("escalation_policy_path_name", UNSET))

        _notification_type = d.pop("notification_type", UNSET)
        notification_type: OncallNotificationType | Unset
        if isinstance(_notification_type, Unset):
            notification_type = UNSET
        else:
            notification_type = check_oncall_notification_type(_notification_type)

        def _parse_is_default_path(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_default_path = _parse_is_default_path(d.pop("is_default_path", UNSET))

        escalation_level = d.pop("escalation_level", UNSET)

        def _parse_schedule_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        schedule_id = _parse_schedule_id(d.pop("schedule_id", UNSET))

        def _parse_schedule_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        schedule_name = _parse_schedule_name(d.pop("schedule_name", UNSET))

        oncall = cls(
            escalation_policy_id=escalation_policy_id,
            escalation_policy_name=escalation_policy_name,
            user_id=user_id,
            starts_at=starts_at,
            ends_at=ends_at,
            escalation_policy_path_id=escalation_policy_path_id,
            escalation_policy_path_name=escalation_policy_path_name,
            notification_type=notification_type,
            is_default_path=is_default_path,
            escalation_level=escalation_level,
            schedule_id=schedule_id,
            schedule_name=schedule_name,
        )

        oncall.additional_properties = d
        return oncall

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
