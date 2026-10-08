from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alert_configuration_manual_paging_form_settings_item import (
    AlertConfigurationManualPagingFormSettingsItem,
    check_alert_configuration_manual_paging_form_settings_item,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_configuration_alert_acknowledgment import AlertConfigurationAlertAcknowledgment
    from ..models.alert_configuration_default_user_notification_settings import (
        AlertConfigurationDefaultUserNotificationSettings,
    )


T = TypeVar("T", bound="AlertConfiguration")


@_attrs_define
class AlertConfiguration:
    """
    Attributes:
        alert_acknowledgment (AlertConfigurationAlertAcknowledgment | Unset): Re-trigger behaviour for acknowledged
            alerts. Replaces the stored object as a whole.
        manual_paging_form_settings (list[AlertConfigurationManualPagingFormSettingsItem] | Unset): Stored entity types
            for the manual paging form, as configured; at least one is required. The form itself may hide a type the team
            cannot use yet, such as functionality.
        manual_paging_urgency_ids (list[UUID] | Unset): Alert urgency ids allowed when manually paging. Empty means all;
            deleted urgencies are left out. Present and accepted only while the manual-page-urgency-allowlist feature is on
            for the team.
        default_user_notification_settings (AlertConfigurationDefaultUserNotificationSettings | Unset): Channel defaults
            for new users, per urgency level. Omitted levels keep the built-in defaults; existing users are never changed.
            Present and accepted only while org-default-notification-settings is on for the team.
        created_at (datetime.datetime | Unset):
        updated_at (datetime.datetime | Unset):
    """

    alert_acknowledgment: AlertConfigurationAlertAcknowledgment | Unset = UNSET
    manual_paging_form_settings: list[AlertConfigurationManualPagingFormSettingsItem] | Unset = UNSET
    manual_paging_urgency_ids: list[UUID] | Unset = UNSET
    default_user_notification_settings: AlertConfigurationDefaultUserNotificationSettings | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert_acknowledgment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.alert_acknowledgment, Unset):
            alert_acknowledgment = self.alert_acknowledgment.to_dict()

        manual_paging_form_settings: list[str] | Unset = UNSET
        if not isinstance(self.manual_paging_form_settings, Unset):
            manual_paging_form_settings = []
            for manual_paging_form_settings_item_data in self.manual_paging_form_settings:
                manual_paging_form_settings_item: str = manual_paging_form_settings_item_data
                manual_paging_form_settings.append(manual_paging_form_settings_item)

        manual_paging_urgency_ids: list[str] | Unset = UNSET
        if not isinstance(self.manual_paging_urgency_ids, Unset):
            manual_paging_urgency_ids = []
            for manual_paging_urgency_ids_item_data in self.manual_paging_urgency_ids:
                manual_paging_urgency_ids_item = str(manual_paging_urgency_ids_item_data)
                manual_paging_urgency_ids.append(manual_paging_urgency_ids_item)

        default_user_notification_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_user_notification_settings, Unset):
            default_user_notification_settings = self.default_user_notification_settings.to_dict()

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alert_acknowledgment is not UNSET:
            field_dict["alert_acknowledgment"] = alert_acknowledgment
        if manual_paging_form_settings is not UNSET:
            field_dict["manual_paging_form_settings"] = manual_paging_form_settings
        if manual_paging_urgency_ids is not UNSET:
            field_dict["manual_paging_urgency_ids"] = manual_paging_urgency_ids
        if default_user_notification_settings is not UNSET:
            field_dict["default_user_notification_settings"] = default_user_notification_settings
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alert_configuration_alert_acknowledgment import AlertConfigurationAlertAcknowledgment
        from ..models.alert_configuration_default_user_notification_settings import (
            AlertConfigurationDefaultUserNotificationSettings,
        )

        d = dict(src_dict)
        _alert_acknowledgment = d.pop("alert_acknowledgment", UNSET)
        alert_acknowledgment: AlertConfigurationAlertAcknowledgment | Unset
        if isinstance(_alert_acknowledgment, Unset):
            alert_acknowledgment = UNSET
        else:
            alert_acknowledgment = AlertConfigurationAlertAcknowledgment.from_dict(_alert_acknowledgment)

        _manual_paging_form_settings = d.pop("manual_paging_form_settings", UNSET)
        manual_paging_form_settings: list[AlertConfigurationManualPagingFormSettingsItem] | Unset = UNSET
        if _manual_paging_form_settings is not UNSET:
            manual_paging_form_settings = []
            for manual_paging_form_settings_item_data in _manual_paging_form_settings:
                manual_paging_form_settings_item = check_alert_configuration_manual_paging_form_settings_item(
                    manual_paging_form_settings_item_data
                )

                manual_paging_form_settings.append(manual_paging_form_settings_item)

        _manual_paging_urgency_ids = d.pop("manual_paging_urgency_ids", UNSET)
        manual_paging_urgency_ids: list[UUID] | Unset = UNSET
        if _manual_paging_urgency_ids is not UNSET:
            manual_paging_urgency_ids = []
            for manual_paging_urgency_ids_item_data in _manual_paging_urgency_ids:
                manual_paging_urgency_ids_item = UUID(manual_paging_urgency_ids_item_data)

                manual_paging_urgency_ids.append(manual_paging_urgency_ids_item)

        _default_user_notification_settings = d.pop("default_user_notification_settings", UNSET)
        default_user_notification_settings: AlertConfigurationDefaultUserNotificationSettings | Unset
        if isinstance(_default_user_notification_settings, Unset):
            default_user_notification_settings = UNSET
        else:
            default_user_notification_settings = AlertConfigurationDefaultUserNotificationSettings.from_dict(
                _default_user_notification_settings
            )

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)

        alert_configuration = cls(
            alert_acknowledgment=alert_acknowledgment,
            manual_paging_form_settings=manual_paging_form_settings,
            manual_paging_urgency_ids=manual_paging_urgency_ids,
            default_user_notification_settings=default_user_notification_settings,
            created_at=created_at,
            updated_at=updated_at,
        )

        alert_configuration.additional_properties = d
        return alert_configuration

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
