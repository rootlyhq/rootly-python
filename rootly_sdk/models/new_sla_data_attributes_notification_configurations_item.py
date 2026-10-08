from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.new_sla_data_attributes_notification_configurations_item_offset_type import (
    NewSlaDataAttributesNotificationConfigurationsItemOffsetType,
    check_new_sla_data_attributes_notification_configurations_item_offset_type,
)

T = TypeVar("T", bound="NewSlaDataAttributesNotificationConfigurationsItem")


@_attrs_define
class NewSlaDataAttributesNotificationConfigurationsItem:
    """
    Attributes:
        offset_type (NewSlaDataAttributesNotificationConfigurationsItemOffsetType): When to send the notification
            relative to the deadline
        offset_days (int): Number of days before or after the deadline. Must be 0 for when_due.
    """

    offset_type: NewSlaDataAttributesNotificationConfigurationsItemOffsetType
    offset_days: int

    def to_dict(self) -> dict[str, Any]:
        offset_type: str = self.offset_type

        offset_days = self.offset_days

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "offset_type": offset_type,
                "offset_days": offset_days,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        offset_type = check_new_sla_data_attributes_notification_configurations_item_offset_type(d.pop("offset_type"))

        offset_days = d.pop("offset_days")

        new_sla_data_attributes_notification_configurations_item = cls(
            offset_type=offset_type,
            offset_days=offset_days,
        )

        return new_sla_data_attributes_notification_configurations_item
