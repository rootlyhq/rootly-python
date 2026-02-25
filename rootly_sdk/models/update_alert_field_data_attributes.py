from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAlertFieldDataAttributes")


@_attrs_define
class UpdateAlertFieldDataAttributes:
    """
    Attributes:
        name (Union[Unset, str]): The name of the alert field
    """

    name: Unset | str = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        update_alert_field_data_attributes = cls(
            name=name,
        )

        return update_alert_field_data_attributes
