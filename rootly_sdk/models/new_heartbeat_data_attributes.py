from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.new_heartbeat_data_attributes_interval_unit import (
    NewHeartbeatDataAttributesIntervalUnit,
    check_new_heartbeat_data_attributes_interval_unit,
)
from ..models.new_heartbeat_data_attributes_notification_target_type import (
    NewHeartbeatDataAttributesNotificationTargetType,
    check_new_heartbeat_data_attributes_notification_target_type,
)
from ..types import UNSET, Unset

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
        notification_target_type (NewHeartbeatDataAttributesNotificationTargetType):
        description (Union[None, Unset, str]): The description of the heartbeat
        alert_description (Union[None, Unset, str]): Description of alerts triggered when heartbeat expires.
        alert_urgency_id (Union[None, Unset, str]): Urgency of alerts triggered when heartbeat expires.
        enabled (Union[Unset, bool]): Whether to trigger alerts when heartbeat is expired.
    """

    name: str
    alert_summary: str
    interval: int
    interval_unit: NewHeartbeatDataAttributesIntervalUnit
    notification_target_id: str
    notification_target_type: NewHeartbeatDataAttributesNotificationTargetType
    description: None | Unset | str = UNSET
    alert_description: None | Unset | str = UNSET
    alert_urgency_id: None | Unset | str = UNSET
    enabled: Unset | bool = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        alert_summary = self.alert_summary

        interval = self.interval

        interval_unit: str = self.interval_unit

        notification_target_id = self.notification_target_id

        notification_target_type: str = self.notification_target_type

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

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

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        description = _parse_description(d.pop("description", UNSET))

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
            enabled=enabled,
        )

        return new_heartbeat_data_attributes
