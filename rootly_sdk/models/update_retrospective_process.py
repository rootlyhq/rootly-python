from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.update_retrospective_process_data import UpdateRetrospectiveProcessData


T = TypeVar("T", bound="UpdateRetrospectiveProcess")


@_attrs_define
class UpdateRetrospectiveProcess:
    """
    Attributes:
        data (UpdateRetrospectiveProcessData):
    """

    data: UpdateRetrospectiveProcessData

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
        from ..models.update_retrospective_process_data import UpdateRetrospectiveProcessData

        d = dict(src_dict)
        data = UpdateRetrospectiveProcessData.from_dict(d.pop("data"))

        update_retrospective_process = cls(
            data=data,
        )

        return update_retrospective_process
