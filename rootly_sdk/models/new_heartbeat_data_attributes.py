from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.new_heartbeat_data_attributes_interval_unit import check_new_heartbeat_data_attributes_interval_unit
from ..models.new_heartbeat_data_attributes_interval_unit import NewHeartbeatDataAttributesIntervalUnit
from ..models.new_heartbeat_data_attributes_notification_target_type import (
    check_new_heartbeat_data_attributes_notification_target_type,
)
from ..models.new_heartbeat_data_attributes_notification_target_type import (
    NewHeartbeatDataAttributesNotificationTargetType,
)
from ..types import UNSET, Unset
from typing import cast


T = TypeVar("T", bound="NewHeartbeatDataAttributes")


@_attrs_define
class NewHeartbeatDataAttributes:
    """
    Attributes:
        name (str): The name of the heartbeat
        alert_summary (str): Summary of alerts triggered when heartbeat expires.
        interval (int):
        interval_unit (NewHeartbeatDataAttributesIntervalUnit):
        notification_target_id (str):
        notification_target_type (NewHeartbeatDataAttributesNotificationTargetType): The type of the notification
            target. Please contact support if you encounter issues using `Functionality` as a target type.
        description (None | str | Unset): The description of the heartbeat
        alert_description (None | str | Unset): Description of alerts triggered when heartbeat expires.
        alert_urgency_id (None | str | Unset): Urgency of alerts triggered when heartbeat expires.
        owner_group_ids (list[str] | Unset): List of team IDs that own this heartbeat
        enabled (bool | Unset): Whether to trigger alerts when heartbeat is expired.
    """

    name: str
    alert_summary: str
    interval: int
    interval_unit: NewHeartbeatDataAttributesIntervalUnit
    notification_target_id: str
    notification_target_type: NewHeartbeatDataAttributesNotificationTargetType
    description: None | str | Unset = UNSET
    alert_description: None | str | Unset = UNSET
    alert_urgency_id: None | str | Unset = UNSET
    owner_group_ids: list[str] | Unset = UNSET
    enabled: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        alert_summary = self.alert_summary

        interval = self.interval

        interval_unit: str = self.interval_unit

        notification_target_id = self.notification_target_id

        notification_target_type: str = self.notification_target_type

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        alert_description: None | str | Unset
        if isinstance(self.alert_description, Unset):
            alert_description = UNSET
        else:
            alert_description = self.alert_description

        alert_urgency_id: None | str | Unset
        if isinstance(self.alert_urgency_id, Unset):
            alert_urgency_id = UNSET
        else:
            alert_urgency_id = self.alert_urgency_id

        owner_group_ids: list[str] | Unset = UNSET
        if not isinstance(self.owner_group_ids, Unset):
            owner_group_ids = self.owner_group_ids

        enabled = self.enabled

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "alert_summary": alert_summary,
                "interval": interval,
                "interval_unit": interval_unit,
                "notification_target_id": notification_target_id,
                "notification_target_type": notification_target_type,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if alert_description is not UNSET:
            field_dict["alert_description"] = alert_description
        if alert_urgency_id is not UNSET:
            field_dict["alert_urgency_id"] = alert_urgency_id
        if owner_group_ids is not UNSET:
            field_dict["owner_group_ids"] = owner_group_ids
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        alert_summary = d.pop("alert_summary")

        interval = d.pop("interval")

        interval_unit = check_new_heartbeat_data_attributes_interval_unit(d.pop("interval_unit"))

        notification_target_id = d.pop("notification_target_id")

        notification_target_type = check_new_heartbeat_data_attributes_notification_target_type(
            d.pop("notification_target_type")
        )

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_alert_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alert_description = _parse_alert_description(d.pop("alert_description", UNSET))

        def _parse_alert_urgency_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alert_urgency_id = _parse_alert_urgency_id(d.pop("alert_urgency_id", UNSET))

        owner_group_ids = cast(list[str], d.pop("owner_group_ids", UNSET))

        enabled = d.pop("enabled", UNSET)

        new_heartbeat_data_attributes = cls(
            name=name,
            alert_summary=alert_summary,
            interval=interval,
            interval_unit=interval_unit,
            notification_target_id=notification_target_id,
            notification_target_type=notification_target_type,
            description=description,
            alert_description=alert_description,
            alert_urgency_id=alert_urgency_id,
            owner_group_ids=owner_group_ids,
            enabled=enabled,
        )

        return new_heartbeat_data_attributes
