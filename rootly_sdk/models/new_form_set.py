from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.new_form_set_data import NewFormSetData


T = TypeVar("T", bound="NewFormSet")


@_attrs_define
class NewFormSet:
    """
    Attributes:
        data (NewFormSetData):
    """

    data: NewFormSetData

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
        from ..models.new_form_set_data import NewFormSetData

        d = dict(src_dict)
        data = NewFormSetData.from_dict(d.pop("data"))

        new_form_set = cls(
            data=data,
        )

        return new_form_set
