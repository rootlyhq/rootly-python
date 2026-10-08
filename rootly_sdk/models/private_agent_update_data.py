from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.private_agent_update_data_type import PrivateAgentUpdateDataType, check_private_agent_update_data_type

if TYPE_CHECKING:
    from ..models.private_agent_update_data_attributes import PrivateAgentUpdateDataAttributes


T = TypeVar("T", bound="PrivateAgentUpdateData")


@_attrs_define
class PrivateAgentUpdateData:
    """
    Attributes:
        type_ (PrivateAgentUpdateDataType):
        attributes (PrivateAgentUpdateDataAttributes):
    """

    type_: PrivateAgentUpdateDataType
    attributes: PrivateAgentUpdateDataAttributes

    def to_dict(self) -> dict[str, Any]:
        type_: str = self.type_

        attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "attributes": attributes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.private_agent_update_data_attributes import PrivateAgentUpdateDataAttributes

        d = dict(src_dict)
        type_ = check_private_agent_update_data_type(d.pop("type"))

        attributes = PrivateAgentUpdateDataAttributes.from_dict(d.pop("attributes"))

        private_agent_update_data = cls(
            type_=type_,
            attributes=attributes,
        )

        return private_agent_update_data
