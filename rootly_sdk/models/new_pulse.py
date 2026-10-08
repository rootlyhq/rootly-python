from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.new_pulse_data import NewPulseData


T = TypeVar("T", bound="NewPulse")


@_attrs_define
class NewPulse:
    """
    Attributes:
        data (NewPulseData):
    """

    data: NewPulseData

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_pulse_data import NewPulseData

        d = dict(src_dict)
        data = NewPulseData.from_dict(d.pop("data"))

        new_pulse = cls(
            data=data,
        )

        return new_pulse
