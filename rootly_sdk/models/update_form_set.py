from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.update_form_set_data import UpdateFormSetData


T = TypeVar("T", bound="UpdateFormSet")


@_attrs_define
class UpdateFormSet:
    """
    Attributes:
        data (UpdateFormSetData):
    """

    data: UpdateFormSetData

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
        from ..models.update_form_set_data import UpdateFormSetData

        d = dict(src_dict)
        data = UpdateFormSetData.from_dict(d.pop("data"))

        update_form_set = cls(
            data=data,
        )

        return update_form_set
