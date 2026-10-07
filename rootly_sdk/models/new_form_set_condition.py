from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.new_form_set_condition_data import NewFormSetConditionData


T = TypeVar("T", bound="NewFormSetCondition")


@_attrs_define
class NewFormSetCondition:
    """
    Attributes:
        data (NewFormSetConditionData):
    """

    data: NewFormSetConditionData

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
        from ..models.new_form_set_condition_data import NewFormSetConditionData

        d = dict(src_dict)
        data = NewFormSetConditionData.from_dict(d.pop("data"))

        new_form_set_condition = cls(
            data=data,
        )

        return new_form_set_condition
