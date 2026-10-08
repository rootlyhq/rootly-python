from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.private_agent_enrollment_token_response_data_type import (
    PrivateAgentEnrollmentTokenResponseDataType,
    check_private_agent_enrollment_token_response_data_type,
)

if TYPE_CHECKING:
    from ..models.private_agent_enrollment_token_response_data_attributes import (
        PrivateAgentEnrollmentTokenResponseDataAttributes,
    )


T = TypeVar("T", bound="PrivateAgentEnrollmentTokenResponseData")


@_attrs_define
class PrivateAgentEnrollmentTokenResponseData:
    """
    Attributes:
        id (UUID):
        type_ (PrivateAgentEnrollmentTokenResponseDataType):
        attributes (PrivateAgentEnrollmentTokenResponseDataAttributes):
    """

    id: UUID
    type_: PrivateAgentEnrollmentTokenResponseDataType
    attributes: PrivateAgentEnrollmentTokenResponseDataAttributes

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
        from ..models.private_agent_enrollment_token_response_data_attributes import (
            PrivateAgentEnrollmentTokenResponseDataAttributes,
        )

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        type_ = check_private_agent_enrollment_token_response_data_type(d.pop("type"))

        attributes = PrivateAgentEnrollmentTokenResponseDataAttributes.from_dict(d.pop("attributes"))

        private_agent_enrollment_token_response_data = cls(
            id=id,
            type_=type_,
            attributes=attributes,
        )

        return private_agent_enrollment_token_response_data
