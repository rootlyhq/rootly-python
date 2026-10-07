from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.update_alert_configuration_data_attributes_default_user_notification_settings_audible_contact_types_item import (
    UpdateAlertConfigurationDataAttributesDefaultUserNotificationSettingsAudibleContactTypesItem,
    check_update_alert_configuration_data_attributes_default_user_notification_settings_audible_contact_types_item,
)
from ..models.update_alert_configuration_data_attributes_default_user_notification_settings_quiet_contact_types_item import (
    UpdateAlertConfigurationDataAttributesDefaultUserNotificationSettingsQuietContactTypesItem,
    check_update_alert_configuration_data_attributes_default_user_notification_settings_quiet_contact_types_item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAlertConfigurationDataAttributesDefaultUserNotificationSettings")


@_attrs_define
class UpdateAlertConfigurationDataAttributesDefaultUserNotificationSettings:
    """Channel defaults for new users, per urgency level. Omitted levels keep the built-in defaults; existing users are
    never changed. Present and accepted only while org-default-notification-settings is on for the team.

        Attributes:
            audible_contact_types
                (list[UpdateAlertConfigurationDataAttributesDefaultUserNotificationSettingsAudibleContactTypesItem] | Unset):
                Channels enabled on a newly created user's audible notification rule. At least one channel is required.
            quiet_contact_types
                (list[UpdateAlertConfigurationDataAttributesDefaultUserNotificationSettingsQuietContactTypesItem] | Unset):
                Channels enabled on a newly created user's quiet notification rule. At least one channel is required.
    """

    audible_contact_types: (
        list[UpdateAlertConfigurationDataAttributesDefaultUserNotificationSettingsAudibleContactTypesItem] | Unset
    ) = UNSET
    quiet_contact_types: (
        list[UpdateAlertConfigurationDataAttributesDefaultUserNotificationSettingsQuietContactTypesItem] | Unset
    ) = UNSET

    def to_dict(self) -> dict[str, Any]:
        audible_contact_types: list[str] | Unset = UNSET
        if not isinstance(self.audible_contact_types, Unset):
            audible_contact_types = []
            for audible_contact_types_item_data in self.audible_contact_types:
                audible_contact_types_item: str = audible_contact_types_item_data
                audible_contact_types.append(audible_contact_types_item)

        quiet_contact_types: list[str] | Unset = UNSET
        if not isinstance(self.quiet_contact_types, Unset):
            quiet_contact_types = []
            for quiet_contact_types_item_data in self.quiet_contact_types:
                quiet_contact_types_item: str = quiet_contact_types_item_data
                quiet_contact_types.append(quiet_contact_types_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if audible_contact_types is not UNSET:
            field_dict["audible_contact_types"] = audible_contact_types
        if quiet_contact_types is not UNSET:
            field_dict["quiet_contact_types"] = quiet_contact_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _audible_contact_types = d.pop("audible_contact_types", UNSET)
        audible_contact_types: (
            list[UpdateAlertConfigurationDataAttributesDefaultUserNotificationSettingsAudibleContactTypesItem] | Unset
        ) = UNSET
        if _audible_contact_types is not UNSET:
            audible_contact_types = []
            for audible_contact_types_item_data in _audible_contact_types:
                audible_contact_types_item = check_update_alert_configuration_data_attributes_default_user_notification_settings_audible_contact_types_item(
                    audible_contact_types_item_data
                )

                audible_contact_types.append(audible_contact_types_item)

        _quiet_contact_types = d.pop("quiet_contact_types", UNSET)
        quiet_contact_types: (
            list[UpdateAlertConfigurationDataAttributesDefaultUserNotificationSettingsQuietContactTypesItem] | Unset
        ) = UNSET
        if _quiet_contact_types is not UNSET:
            quiet_contact_types = []
            for quiet_contact_types_item_data in _quiet_contact_types:
                quiet_contact_types_item = check_update_alert_configuration_data_attributes_default_user_notification_settings_quiet_contact_types_item(
                    quiet_contact_types_item_data
                )

                quiet_contact_types.append(quiet_contact_types_item)

        update_alert_configuration_data_attributes_default_user_notification_settings = cls(
            audible_contact_types=audible_contact_types,
            quiet_contact_types=quiet_contact_types,
        )

        return update_alert_configuration_data_attributes_default_user_notification_settings
