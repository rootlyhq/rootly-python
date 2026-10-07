from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.update_alert_urgency_data_attributes_retrigger_timeout_minutes import (
    UpdateAlertUrgencyDataAttributesRetriggerTimeoutMinutes,
    check_update_alert_urgency_data_attributes_retrigger_timeout_minutes,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAlertUrgencyDataAttributes")


@_attrs_define
class UpdateAlertUrgencyDataAttributes:
    """
    Attributes:
        name (str | Unset): The name of the alert urgency
        description (str | Unset): The description of the alert urgency
        position (int | None | Unset): Position of the alert urgency
        retrigger_timeout_minutes (UpdateAlertUrgencyDataAttributesRetriggerTimeoutMinutes | Unset): Re-trigger
            acknowledged alerts of this urgency after N minutes; null inherits the workspace default, -1 = never.
    """

    name: str | Unset = UNSET
    description: str | Unset = UNSET
    position: int | None | Unset = UNSET
    retrigger_timeout_minutes: UpdateAlertUrgencyDataAttributesRetriggerTimeoutMinutes | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        position: int | None | Unset
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        retrigger_timeout_minutes: int | Unset = UNSET
        if not isinstance(self.retrigger_timeout_minutes, Unset):
            retrigger_timeout_minutes = self.retrigger_timeout_minutes

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if position is not UNSET:
            field_dict["position"] = position
        if retrigger_timeout_minutes is not UNSET:
            field_dict["retrigger_timeout_minutes"] = retrigger_timeout_minutes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        def _parse_position(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        position = _parse_position(d.pop("position", UNSET))

        _retrigger_timeout_minutes = d.pop("retrigger_timeout_minutes", UNSET)
        retrigger_timeout_minutes: UpdateAlertUrgencyDataAttributesRetriggerTimeoutMinutes | Unset
        if isinstance(_retrigger_timeout_minutes, Unset):
            retrigger_timeout_minutes = UNSET
        else:
            retrigger_timeout_minutes = check_update_alert_urgency_data_attributes_retrigger_timeout_minutes(
                _retrigger_timeout_minutes
            )

        update_alert_urgency_data_attributes = cls(
            name=name,
            description=description,
            position=position,
            retrigger_timeout_minutes=retrigger_timeout_minutes,
        )

        return update_alert_urgency_data_attributes
