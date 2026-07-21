from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.new_alert_data_attributes_notification_targets_type_0_item_type import (
    check_new_alert_data_attributes_notification_targets_type_0_item_type,
)
from ..models.new_alert_data_attributes_notification_targets_type_0_item_type import (
    NewAlertDataAttributesNotificationTargetsType0ItemType,
)
from typing import cast


T = TypeVar("T", bound="NewAlertDataAttributesNotificationTargetsType0Item")


@_attrs_define
class NewAlertDataAttributesNotificationTargetsType0Item:
    """
    Attributes:
        type_ (NewAlertDataAttributesNotificationTargetsType0ItemType): The type of the notification target. Can be one
            of Group, Service, EscalationPolicy, Functionality, User.
        id (str): The identifier of the notification target object.
    """

    type_: NewAlertDataAttributesNotificationTargetsType0ItemType
    id: str

    def to_dict(self) -> dict[str, Any]:
        type_: str = self.type_

        id = self.id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = check_new_alert_data_attributes_notification_targets_type_0_item_type(d.pop("type"))

        id = d.pop("id")

        new_alert_data_attributes_notification_targets_type_0_item = cls(
            type_=type_,
            id=id,
        )

        return new_alert_data_attributes_notification_targets_type_0_item
