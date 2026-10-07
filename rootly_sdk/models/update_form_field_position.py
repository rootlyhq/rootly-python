from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.update_form_field_position_data import UpdateFormFieldPositionData


T = TypeVar("T", bound="UpdateFormFieldPosition")


@_attrs_define
class UpdateFormFieldPosition:
    """
    Attributes:
        data (UpdateFormFieldPositionData):
    """

    data: UpdateFormFieldPositionData

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
        from ..models.update_form_field_position_data import UpdateFormFieldPositionData

        d = dict(src_dict)
        data = UpdateFormFieldPositionData.from_dict(d.pop("data"))

        update_form_field_position = cls(
            data=data,
        )

        return update_form_field_position
