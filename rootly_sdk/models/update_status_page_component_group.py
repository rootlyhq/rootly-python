from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.update_status_page_component_group_data import UpdateStatusPageComponentGroupData


T = TypeVar("T", bound="UpdateStatusPageComponentGroup")


@_attrs_define
class UpdateStatusPageComponentGroup:
    """
    Attributes:
        data (UpdateStatusPageComponentGroupData):
    """

    data: UpdateStatusPageComponentGroupData

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
        from ..models.update_status_page_component_group_data import UpdateStatusPageComponentGroupData

        d = dict(src_dict)
        data = UpdateStatusPageComponentGroupData.from_dict(d.pop("data"))

        update_status_page_component_group = cls(
            data=data,
        )

        return update_status_page_component_group
