from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAlertUrgencyDataAttributes")


@_attrs_define
class UpdateAlertUrgencyDataAttributes:
    """
    Attributes:
        name (Union[Unset, str]): The name of the alert urgency
        description (Union[Unset, str]): The description of the alert urgency
        position (Union[None, Unset, int]): Position of the alert urgency
        retrigger_timeout_minutes (Union[None, Unset, int]): Re-trigger acknowledged alerts of this urgency after N
            minutes; null inherits the workspace default, negative = never.
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    position: Union[None, Unset, int] = UNSET
    retrigger_timeout_minutes: Union[None, Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        position: Union[None, Unset, int]
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        retrigger_timeout_minutes: Union[None, Unset, int]
        if isinstance(self.retrigger_timeout_minutes, Unset):
            retrigger_timeout_minutes = UNSET
        else:
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

        def _parse_position(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        position = _parse_position(d.pop("position", UNSET))

        def _parse_retrigger_timeout_minutes(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        retrigger_timeout_minutes = _parse_retrigger_timeout_minutes(d.pop("retrigger_timeout_minutes", UNSET))

        update_alert_urgency_data_attributes = cls(
            name=name,
            description=description,
            position=position,
            retrigger_timeout_minutes=retrigger_timeout_minutes,
        )

        return update_alert_urgency_data_attributes
