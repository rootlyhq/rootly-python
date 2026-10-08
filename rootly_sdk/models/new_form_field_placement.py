from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.new_form_field_placement_data import NewFormFieldPlacementData


T = TypeVar("T", bound="NewFormFieldPlacement")


@_attrs_define
class NewFormFieldPlacement:
    """
    Attributes:
        data (NewFormFieldPlacementData):
    """

    data: NewFormFieldPlacementData

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
        from ..models.new_form_field_placement_data import NewFormFieldPlacementData

        d = dict(src_dict)
        data = NewFormFieldPlacementData.from_dict(d.pop("data"))

        new_form_field_placement = cls(
            data=data,
        )

        return new_form_field_placement
