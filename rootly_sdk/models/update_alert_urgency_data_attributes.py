from collections.abc import Mapping
from typing import Any, TypeVar, cast

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
    """

    name: Unset | str = UNSET
    description: Unset | str = UNSET
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

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        def _parse_position(data: object) -> None | Unset | int:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | int, data)

        position = _parse_position(d.pop("position", UNSET))

        update_alert_urgency_data_attributes = cls(
            name=name,
            description=description,
            position=position,
        )

        return update_alert_urgency_data_attributes
