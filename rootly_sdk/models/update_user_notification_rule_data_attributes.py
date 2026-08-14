from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.update_user_notification_rule_data_attributes_enabled_contact_types_item import (
    UpdateUserNotificationRuleDataAttributesEnabledContactTypesItem,
    check_update_user_notification_rule_data_attributes_enabled_contact_types_item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateUserNotificationRuleDataAttributes")


@_attrs_define
class UpdateUserNotificationRuleDataAttributes:
    """
    Attributes:
        delay (Union[None, Unset, int]): Delay after which rule gets triggered
        position (Union[None, Unset, int]): Position of the rule
        user_email_address_id (Union[None, Unset, str]): User email address to which notification to be sent
        user_call_number_id (Union[None, Unset, str]): User phone number to which notification to be sent
        user_sms_number_id (Union[None, Unset, str]): User sms number to which notification to be sent
        user_device_id (Union[None, Unset, str]): User device to which notification to be sent
        enabled_contact_types (Union[Unset, list[UpdateUserNotificationRuleDataAttributesEnabledContactTypesItem]]):
            Contact types for which notification needs to be enabled
    """

    delay: None | Unset | int = UNSET
    position: None | Unset | int = UNSET
    user_email_address_id: None | Unset | str = UNSET
    user_call_number_id: None | Unset | str = UNSET
    user_sms_number_id: None | Unset | str = UNSET
    user_device_id: None | Unset | str = UNSET
    enabled_contact_types: Unset | list[UpdateUserNotificationRuleDataAttributesEnabledContactTypesItem] = UNSET

    def to_dict(self) -> dict[str, Any]:
        delay: None | Unset | int
        if isinstance(self.delay, Unset):
            delay = UNSET
        else:
            delay = self.delay

        position: None | Unset | int
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        user_email_address_id: None | Unset | str
        if isinstance(self.user_email_address_id, Unset):
            user_email_address_id = UNSET
        else:
            user_email_address_id = self.user_email_address_id

        user_call_number_id: None | Unset | str
        if isinstance(self.user_call_number_id, Unset):
            user_call_number_id = UNSET
        else:
            user_call_number_id = self.user_call_number_id

        user_sms_number_id: None | Unset | str
        if isinstance(self.user_sms_number_id, Unset):
            user_sms_number_id = UNSET
        else:
            user_sms_number_id = self.user_sms_number_id

        user_device_id: None | Unset | str
        if isinstance(self.user_device_id, Unset):
            user_device_id = UNSET
        else:
            user_device_id = self.user_device_id

        enabled_contact_types: Unset | list[str] = UNSET
        if not isinstance(self.enabled_contact_types, Unset):
            enabled_contact_types = []
            for enabled_contact_types_item_data in self.enabled_contact_types:
                enabled_contact_types_item: str = enabled_contact_types_item_data
                enabled_contact_types.append(enabled_contact_types_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if delay is not UNSET:
            field_dict["delay"] = delay
        if position is not UNSET:
            field_dict["position"] = position
        if user_email_address_id is not UNSET:
            field_dict["user_email_address_id"] = user_email_address_id
        if user_call_number_id is not UNSET:
            field_dict["user_call_number_id"] = user_call_number_id
        if user_sms_number_id is not UNSET:
            field_dict["user_sms_number_id"] = user_sms_number_id
        if user_device_id is not UNSET:
            field_dict["user_device_id"] = user_device_id
        if enabled_contact_types is not UNSET:
            field_dict["enabled_contact_types"] = enabled_contact_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_delay(data: object) -> None | Unset | int:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | int, data)

        delay = _parse_delay(d.pop("delay", UNSET))

        def _parse_position(data: object) -> None | Unset | int:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | int, data)

        position = _parse_position(d.pop("position", UNSET))

        def _parse_user_email_address_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        user_email_address_id = _parse_user_email_address_id(d.pop("user_email_address_id", UNSET))

        def _parse_user_call_number_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        user_call_number_id = _parse_user_call_number_id(d.pop("user_call_number_id", UNSET))

        def _parse_user_sms_number_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        user_sms_number_id = _parse_user_sms_number_id(d.pop("user_sms_number_id", UNSET))

        def _parse_user_device_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        user_device_id = _parse_user_device_id(d.pop("user_device_id", UNSET))

        enabled_contact_types = []
        _enabled_contact_types = d.pop("enabled_contact_types", UNSET)
        for enabled_contact_types_item_data in _enabled_contact_types or []:
            enabled_contact_types_item = check_update_user_notification_rule_data_attributes_enabled_contact_types_item(
                enabled_contact_types_item_data
            )

            enabled_contact_types.append(enabled_contact_types_item)

        update_user_notification_rule_data_attributes = cls(
            delay=delay,
            position=position,
            user_email_address_id=user_email_address_id,
            user_call_number_id=user_call_number_id,
            user_sms_number_id=user_sms_number_id,
            user_device_id=user_device_id,
            enabled_contact_types=enabled_contact_types,
        )

        return update_user_notification_rule_data_attributes
