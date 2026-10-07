from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.update_alert_configuration_data_attributes_manual_paging_form_settings_item import (
    UpdateAlertConfigurationDataAttributesManualPagingFormSettingsItem,
    check_update_alert_configuration_data_attributes_manual_paging_form_settings_item,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_alert_configuration_data_attributes_alert_acknowledgment import (
        UpdateAlertConfigurationDataAttributesAlertAcknowledgment,
    )
    from ..models.update_alert_configuration_data_attributes_default_user_notification_settings import (
        UpdateAlertConfigurationDataAttributesDefaultUserNotificationSettings,
    )


T = TypeVar("T", bound="UpdateAlertConfigurationDataAttributes")


@_attrs_define
class UpdateAlertConfigurationDataAttributes:
    """Every attribute is optional and replaces its stored value. An attribute whose feature is not enabled for the team is
    refused with 403.

        Attributes:
            alert_acknowledgment (UpdateAlertConfigurationDataAttributesAlertAcknowledgment | Unset): Re-trigger behaviour
                for acknowledged alerts. Replaces the stored object as a whole.
            manual_paging_form_settings (list[UpdateAlertConfigurationDataAttributesManualPagingFormSettingsItem] | Unset):
                Stored entity types for the manual paging form, as configured; at least one is required. The form itself may
                hide a type the team cannot use yet, such as functionality.
            manual_paging_urgency_ids (list[UUID] | Unset): Alert urgency ids allowed when manually paging. Empty means all;
                deleted urgencies are left out. Present and accepted only while the manual-page-urgency-allowlist feature is on
                for the team.
            default_user_notification_settings (UpdateAlertConfigurationDataAttributesDefaultUserNotificationSettings |
                Unset): Channel defaults for new users, per urgency level. Omitted levels keep the built-in defaults; existing
                users are never changed. Present and accepted only while org-default-notification-settings is on for the team.
    """

    alert_acknowledgment: UpdateAlertConfigurationDataAttributesAlertAcknowledgment | Unset = UNSET
    manual_paging_form_settings: list[UpdateAlertConfigurationDataAttributesManualPagingFormSettingsItem] | Unset = (
        UNSET
    )
    manual_paging_urgency_ids: list[UUID] | Unset = UNSET
    default_user_notification_settings: (
        UpdateAlertConfigurationDataAttributesDefaultUserNotificationSettings | Unset
    ) = UNSET

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

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if alert_acknowledgment is not UNSET:
            field_dict["alert_acknowledgment"] = alert_acknowledgment
        if manual_paging_form_settings is not UNSET:
            field_dict["manual_paging_form_settings"] = manual_paging_form_settings
        if manual_paging_urgency_ids is not UNSET:
            field_dict["manual_paging_urgency_ids"] = manual_paging_urgency_ids
        if default_user_notification_settings is not UNSET:
            field_dict["default_user_notification_settings"] = default_user_notification_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_alert_configuration_data_attributes_alert_acknowledgment import (
            UpdateAlertConfigurationDataAttributesAlertAcknowledgment,
        )
        from ..models.update_alert_configuration_data_attributes_default_user_notification_settings import (
            UpdateAlertConfigurationDataAttributesDefaultUserNotificationSettings,
        )

        d = dict(src_dict)
        _alert_acknowledgment = d.pop("alert_acknowledgment", UNSET)
        alert_acknowledgment: UpdateAlertConfigurationDataAttributesAlertAcknowledgment | Unset
        if isinstance(_alert_acknowledgment, Unset):
            alert_acknowledgment = UNSET
        else:
            alert_acknowledgment = UpdateAlertConfigurationDataAttributesAlertAcknowledgment.from_dict(
                _alert_acknowledgment
            )

        _manual_paging_form_settings = d.pop("manual_paging_form_settings", UNSET)
        manual_paging_form_settings: (
            list[UpdateAlertConfigurationDataAttributesManualPagingFormSettingsItem] | Unset
        ) = UNSET
        if _manual_paging_form_settings is not UNSET:
            manual_paging_form_settings = []
            for manual_paging_form_settings_item_data in _manual_paging_form_settings:
                manual_paging_form_settings_item = (
                    check_update_alert_configuration_data_attributes_manual_paging_form_settings_item(
                        manual_paging_form_settings_item_data
                    )
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
        default_user_notification_settings: (
            UpdateAlertConfigurationDataAttributesDefaultUserNotificationSettings | Unset
        )
        if isinstance(_default_user_notification_settings, Unset):
            default_user_notification_settings = UNSET
        else:
            default_user_notification_settings = (
                UpdateAlertConfigurationDataAttributesDefaultUserNotificationSettings.from_dict(
                    _default_user_notification_settings
                )
            )

        update_alert_configuration_data_attributes = cls(
            alert_acknowledgment=alert_acknowledgment,
            manual_paging_form_settings=manual_paging_form_settings,
            manual_paging_urgency_ids=manual_paging_urgency_ids,
            default_user_notification_settings=default_user_notification_settings,
        )

        return update_alert_configuration_data_attributes
