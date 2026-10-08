from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.private_agent_update_data import PrivateAgentUpdateData


T = TypeVar("T", bound="PrivateAgentUpdate")


@_attrs_define
class PrivateAgentUpdate:
    """
    Attributes:
        data (PrivateAgentUpdateData):
    """

    data: PrivateAgentUpdateData

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
        from ..models.private_agent_update_data import PrivateAgentUpdateData

        d = dict(src_dict)
        data = PrivateAgentUpdateData.from_dict(d.pop("data"))

        private_agent_update = cls(
            data=data,
        )

        return private_agent_update
