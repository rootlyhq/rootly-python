from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

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
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        offset_type: str = self.offset_type

        offset_days = self.offset_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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

        new_sla_data_attributes_notification_configurations_item.additional_properties = d
        return new_sla_data_attributes_notification_configurations_item

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
