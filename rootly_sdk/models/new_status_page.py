from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.new_status_page_data import NewStatusPageData


T = TypeVar("T", bound="NewStatusPage")


@_attrs_define
class NewStatusPage:
    """
    Attributes:
        data (NewStatusPageData):
    """

    data: NewStatusPageData

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
        from ..models.new_status_page_data import NewStatusPageData

        d = dict(src_dict)
        data = NewStatusPageData.from_dict(d.pop("data"))

        new_status_page = cls(
            data=data,
        )

        return new_status_page
