from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.private_agent_type import PrivateAgentType, check_private_agent_type

if TYPE_CHECKING:
    from ..models.private_agent_attributes import PrivateAgentAttributes


T = TypeVar("T", bound="PrivateAgent")


@_attrs_define
class PrivateAgent:
    """
    Attributes:
        id (UUID):
        type_ (PrivateAgentType):
        attributes (PrivateAgentAttributes):
    """

    id: UUID
    type_: PrivateAgentType
    attributes: PrivateAgentAttributes

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        type_: str = self.type_

        attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "type": type_,
                "attributes": attributes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.private_agent_attributes import PrivateAgentAttributes

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        type_ = check_private_agent_type(d.pop("type"))

        attributes = PrivateAgentAttributes.from_dict(d.pop("attributes"))

        private_agent = cls(
            id=id,
            type_=type_,
            attributes=attributes,
        )

        return private_agent
