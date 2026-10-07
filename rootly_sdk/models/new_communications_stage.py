from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.new_communications_stage_data import NewCommunicationsStageData


T = TypeVar("T", bound="NewCommunicationsStage")


@_attrs_define
class NewCommunicationsStage:
    """
    Attributes:
        data (NewCommunicationsStageData):
    """

    data: NewCommunicationsStageData

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
        from ..models.new_communications_stage_data import NewCommunicationsStageData

        d = dict(src_dict)
        data = NewCommunicationsStageData.from_dict(d.pop("data"))

        new_communications_stage = cls(
            data=data,
        )

        return new_communications_stage
