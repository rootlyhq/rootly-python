from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.update_heartbeat_data_attributes_interval_unit import (
    UpdateHeartbeatDataAttributesIntervalUnit,
    check_update_heartbeat_data_attributes_interval_unit,
)
from ..models.update_heartbeat_data_attributes_notification_target_type import (
    UpdateHeartbeatDataAttributesNotificationTargetType,
    check_update_heartbeat_data_attributes_notification_target_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateHeartbeatDataAttributes")


@_attrs_define
class UpdateHeartbeatDataAttributes:
    """
    Attributes:
        name (Union[Unset, str]): The name of the heartbeat
        description (Union[None, Unset, str]): The description of the heartbeat
        alert_summary (Union[Unset, str]): Summary of alerts triggered when heartbeat expires.
        alert_description (Union[None, Unset, str]): Description of alerts triggered when heartbeat expires.
        alert_urgency_id (Union[None, Unset, str]): Urgency of alerts triggered when heartbeat expires.
        interval (Union[Unset, int]):
        interval_unit (Union[Unset, UpdateHeartbeatDataAttributesIntervalUnit]):
        notification_target_id (Union[Unset, str]):
        notification_target_type (Union[Unset, UpdateHeartbeatDataAttributesNotificationTargetType]):
        enabled (Union[Unset, bool]): Whether to trigger alerts when heartbeat is expired.
    """

    name: Unset | str = UNSET
    description: None | Unset | str = UNSET
    alert_summary: Unset | str = UNSET
    alert_description: None | Unset | str = UNSET
    alert_urgency_id: None | Unset | str = UNSET
    interval: Unset | int = UNSET
    interval_unit: Unset | UpdateHeartbeatDataAttributesIntervalUnit = UNSET
    notification_target_id: Unset | str = UNSET
    notification_target_type: Unset | UpdateHeartbeatDataAttributesNotificationTargetType = UNSET
    enabled: Unset | bool = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        alert_summary = self.alert_summary

        alert_description: None | Unset | str
        if isinstance(self.alert_description, Unset):
            alert_description = UNSET
        else:
            alert_description = self.alert_description

        alert_urgency_id: None | Unset | str
        if isinstance(self.alert_urgency_id, Unset):
            alert_urgency_id = UNSET
        else:
            alert_urgency_id = self.alert_urgency_id

        interval = self.interval

        interval_unit: Unset | str = UNSET
        if not isinstance(self.interval_unit, Unset):
            interval_unit = self.interval_unit

        notification_target_id = self.notification_target_id

        notification_target_type: Unset | str = UNSET
        if not isinstance(self.notification_target_type, Unset):
            notification_target_type = self.notification_target_type

        enabled = self.enabled

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if alert_summary is not UNSET:
            field_dict["alert_summary"] = alert_summary
        if alert_description is not UNSET:
            field_dict["alert_description"] = alert_description
        if alert_urgency_id is not UNSET:
            field_dict["alert_urgency_id"] = alert_urgency_id
        if interval is not UNSET:
            field_dict["interval"] = interval
        if interval_unit is not UNSET:
            field_dict["interval_unit"] = interval_unit
        if notification_target_id is not UNSET:
            field_dict["notification_target_id"] = notification_target_id
        if notification_target_type is not UNSET:
            field_dict["notification_target_type"] = notification_target_type
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        description = _parse_description(d.pop("description", UNSET))

        alert_summary = d.pop("alert_summary", UNSET)

        def _parse_alert_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        alert_description = _parse_alert_description(d.pop("alert_description", UNSET))

        def _parse_alert_urgency_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        alert_urgency_id = _parse_alert_urgency_id(d.pop("alert_urgency_id", UNSET))

        interval = d.pop("interval", UNSET)

        _interval_unit = d.pop("interval_unit", UNSET)
        interval_unit: Unset | UpdateHeartbeatDataAttributesIntervalUnit
        if isinstance(_interval_unit, Unset):
            interval_unit = UNSET
        else:
            interval_unit = check_update_heartbeat_data_attributes_interval_unit(_interval_unit)

        notification_target_id = d.pop("notification_target_id", UNSET)

        _notification_target_type = d.pop("notification_target_type", UNSET)
        notification_target_type: Unset | UpdateHeartbeatDataAttributesNotificationTargetType
        if isinstance(_notification_target_type, Unset):
            notification_target_type = UNSET
        else:
            notification_target_type = check_update_heartbeat_data_attributes_notification_target_type(
                _notification_target_type
            )

        enabled = d.pop("enabled", UNSET)

        update_heartbeat_data_attributes = cls(
            name=name,
            description=description,
            alert_summary=alert_summary,
            alert_description=alert_description,
            alert_urgency_id=alert_urgency_id,
            interval=interval,
            interval_unit=interval_unit,
            notification_target_id=notification_target_id,
            notification_target_type=notification_target_type,
            enabled=enabled,
        )

        return update_heartbeat_data_attributes
