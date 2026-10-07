from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.new_alert_urgency_data_attributes_retrigger_timeout_minutes import (
    NewAlertUrgencyDataAttributesRetriggerTimeoutMinutes,
    check_new_alert_urgency_data_attributes_retrigger_timeout_minutes,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="NewAlertUrgencyDataAttributes")


@_attrs_define
class NewAlertUrgencyDataAttributes:
    """
    Attributes:
        name (str): The name of the alert urgency
        description (str): The description of the alert urgency
        position (int | None | Unset): Position of the alert urgency
        retrigger_timeout_minutes (NewAlertUrgencyDataAttributesRetriggerTimeoutMinutes | Unset): Re-trigger
            acknowledged alerts of this urgency after N minutes; null inherits the workspace default, -1 = never.
    """

    name: str
    description: str
    position: int | None | Unset = UNSET
    retrigger_timeout_minutes: NewAlertUrgencyDataAttributesRetriggerTimeoutMinutes | Unset = UNSET

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

        field_dict.update(
            {
                "name": name,
                "description": description,
            }
        )
        if position is not UNSET:
            field_dict["position"] = position
        if retrigger_timeout_minutes is not UNSET:
            field_dict["retrigger_timeout_minutes"] = retrigger_timeout_minutes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description")

        def _parse_position(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        position = _parse_position(d.pop("position", UNSET))

        _retrigger_timeout_minutes = d.pop("retrigger_timeout_minutes", UNSET)
        retrigger_timeout_minutes: NewAlertUrgencyDataAttributesRetriggerTimeoutMinutes | Unset
        if isinstance(_retrigger_timeout_minutes, Unset):
            retrigger_timeout_minutes = UNSET
        else:
            retrigger_timeout_minutes = check_new_alert_urgency_data_attributes_retrigger_timeout_minutes(
                _retrigger_timeout_minutes
            )

        new_alert_urgency_data_attributes = cls(
            name=name,
            description=description,
            position=position,
            retrigger_timeout_minutes=retrigger_timeout_minutes,
        )

        return new_alert_urgency_data_attributes
