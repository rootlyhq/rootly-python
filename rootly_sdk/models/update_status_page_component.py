from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.update_status_page_component_data import UpdateStatusPageComponentData


T = TypeVar("T", bound="UpdateStatusPageComponent")


@_attrs_define
class UpdateStatusPageComponent:
    """
    Attributes:
        data (UpdateStatusPageComponentData):
    """

    data: UpdateStatusPageComponentData

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
        from ..models.update_status_page_component_data import UpdateStatusPageComponentData

        d = dict(src_dict)
        data = UpdateStatusPageComponentData.from_dict(d.pop("data"))

        update_status_page_component = cls(
            data=data,
        )

        return update_status_page_component
