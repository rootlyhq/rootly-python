from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.update_communications_stage_data import UpdateCommunicationsStageData


T = TypeVar("T", bound="UpdateCommunicationsStage")


@_attrs_define
class UpdateCommunicationsStage:
    """
    Attributes:
        data (UpdateCommunicationsStageData):
    """

    data: UpdateCommunicationsStageData

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
        from ..models.update_communications_stage_data import UpdateCommunicationsStageData

        d = dict(src_dict)
        data = UpdateCommunicationsStageData.from_dict(d.pop("data"))

        update_communications_stage = cls(
            data=data,
        )

        return update_communications_stage
