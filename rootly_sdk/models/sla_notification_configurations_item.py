from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sla_notification_configurations_item_offset_type import (
    SlaNotificationConfigurationsItemOffsetType,
    check_sla_notification_configurations_item_offset_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SlaNotificationConfigurationsItem")


@_attrs_define
class SlaNotificationConfigurationsItem:
    """
    Attributes:
        id (UUID | Unset): Unique ID of the notification configuration
        offset_type (SlaNotificationConfigurationsItemOffsetType | Unset): When to send the notification relative to the
            deadline
        offset_days (int | Unset): Number of days offset from the deadline
        created_at (str | Unset): Date of creation
        updated_at (str | Unset): Date of last update
    """

    id: UUID | Unset = UNSET
    offset_type: SlaNotificationConfigurationsItemOffsetType | Unset = UNSET
    offset_days: int | Unset = UNSET
    created_at: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        offset_type: str | Unset = UNSET
        if not isinstance(self.offset_type, Unset):
            offset_type = self.offset_type

        offset_days = self.offset_days

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if offset_type is not UNSET:
            field_dict["offset_type"] = offset_type
        if offset_days is not UNSET:
            field_dict["offset_days"] = offset_days
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _offset_type = d.pop("offset_type", UNSET)
        offset_type: SlaNotificationConfigurationsItemOffsetType | Unset
        if isinstance(_offset_type, Unset):
            offset_type = UNSET
        else:
            offset_type = check_sla_notification_configurations_item_offset_type(_offset_type)

        offset_days = d.pop("offset_days", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        sla_notification_configurations_item = cls(
            id=id,
            offset_type=offset_type,
            offset_days=offset_days,
            created_at=created_at,
            updated_at=updated_at,
        )

        sla_notification_configurations_item.additional_properties = d
        return sla_notification_configurations_item

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
