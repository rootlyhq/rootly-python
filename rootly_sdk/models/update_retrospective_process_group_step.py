from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.update_retrospective_process_group_step_data import UpdateRetrospectiveProcessGroupStepData


T = TypeVar("T", bound="UpdateRetrospectiveProcessGroupStep")


@_attrs_define
class UpdateRetrospectiveProcessGroupStep:
    """
    Attributes:
        data (UpdateRetrospectiveProcessGroupStepData):
    """

    data: UpdateRetrospectiveProcessGroupStepData

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
        from ..models.update_retrospective_process_group_step_data import UpdateRetrospectiveProcessGroupStepData

        d = dict(src_dict)
        data = UpdateRetrospectiveProcessGroupStepData.from_dict(d.pop("data"))

        update_retrospective_process_group_step = cls(
            data=data,
        )

        return update_retrospective_process_group_step
