from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewAlertUrgencyDataAttributes")


@_attrs_define
class NewAlertUrgencyDataAttributes:
    """
    Attributes:
        name (str): The name of the alert urgency
        description (str): The description of the alert urgency
        position (Union[None, Unset, int]): Position of the alert urgency
    """

    name: str
    description: str
    position: None | Unset | int = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        position: None | Unset | int
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "description": description,
            }
        )
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description")

        def _parse_position(data: object) -> None | Unset | int:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | int, data)

        position = _parse_position(d.pop("position", UNSET))

        new_alert_urgency_data_attributes = cls(
            name=name,
            description=description,
            position=position,
        )

        return new_alert_urgency_data_attributes
