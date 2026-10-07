from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.update_form_field_placement_condition_data import UpdateFormFieldPlacementConditionData


T = TypeVar("T", bound="UpdateFormFieldPlacementCondition")


@_attrs_define
class UpdateFormFieldPlacementCondition:
    """
    Attributes:
        data (UpdateFormFieldPlacementConditionData):
    """

    data: UpdateFormFieldPlacementConditionData

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
        from ..models.update_form_field_placement_condition_data import UpdateFormFieldPlacementConditionData

        d = dict(src_dict)
        data = UpdateFormFieldPlacementConditionData.from_dict(d.pop("data"))

        update_form_field_placement_condition = cls(
            data=data,
        )

        return update_form_field_placement_condition
