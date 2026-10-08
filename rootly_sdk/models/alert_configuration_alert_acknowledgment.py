from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.alert_configuration_alert_acknowledgment_timeout_minutes import (
    AlertConfigurationAlertAcknowledgmentTimeoutMinutes,
    check_alert_configuration_alert_acknowledgment_timeout_minutes,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertConfigurationAlertAcknowledgment")


@_attrs_define
class AlertConfigurationAlertAcknowledgment:
    """Re-trigger behaviour for acknowledged alerts. Replaces the stored object as a whole.

    Attributes:
        timeout_enabled (bool | Unset): Re-trigger an acknowledged alert after the timeout.
        timeout_minutes (AlertConfigurationAlertAcknowledgmentTimeoutMinutes | Unset): Minutes before an acknowledged
            alert re-triggers.
        retrigger_manual_alerts (bool | Unset): Whether alerts created from a manual page also re-trigger. Changing it
            is rejected with 422 until the manual page re-trigger opt-out is enabled for the team.
    """

    timeout_enabled: bool | Unset = UNSET
    timeout_minutes: AlertConfigurationAlertAcknowledgmentTimeoutMinutes | Unset = UNSET
    retrigger_manual_alerts: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        timeout_enabled = self.timeout_enabled

        timeout_minutes: int | Unset = UNSET
        if not isinstance(self.timeout_minutes, Unset):
            timeout_minutes = self.timeout_minutes

        retrigger_manual_alerts = self.retrigger_manual_alerts

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if timeout_enabled is not UNSET:
            field_dict["timeout_enabled"] = timeout_enabled
        if timeout_minutes is not UNSET:
            field_dict["timeout_minutes"] = timeout_minutes
        if retrigger_manual_alerts is not UNSET:
            field_dict["retrigger_manual_alerts"] = retrigger_manual_alerts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        timeout_enabled = d.pop("timeout_enabled", UNSET)

        _timeout_minutes = d.pop("timeout_minutes", UNSET)
        timeout_minutes: AlertConfigurationAlertAcknowledgmentTimeoutMinutes | Unset
        if isinstance(_timeout_minutes, Unset):
            timeout_minutes = UNSET
        else:
            timeout_minutes = check_alert_configuration_alert_acknowledgment_timeout_minutes(_timeout_minutes)

        retrigger_manual_alerts = d.pop("retrigger_manual_alerts", UNSET)

        alert_configuration_alert_acknowledgment = cls(
            timeout_enabled=timeout_enabled,
            timeout_minutes=timeout_minutes,
            retrigger_manual_alerts=retrigger_manual_alerts,
        )

        return alert_configuration_alert_acknowledgment
