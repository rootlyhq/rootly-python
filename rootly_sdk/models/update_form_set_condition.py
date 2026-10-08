from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.update_form_set_condition_data import UpdateFormSetConditionData


T = TypeVar("T", bound="UpdateFormSetCondition")


@_attrs_define
class UpdateFormSetCondition:
    """
    Attributes:
        data (UpdateFormSetConditionData):
    """

    data: UpdateFormSetConditionData

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
        from ..models.update_form_set_condition_data import UpdateFormSetConditionData

        d = dict(src_dict)
        data = UpdateFormSetConditionData.from_dict(d.pop("data"))

        update_form_set_condition = cls(
            data=data,
        )

        return update_form_set_condition
