from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ai_chat_response_data_type import AiChatResponseDataType, check_ai_chat_response_data_type

if TYPE_CHECKING:
    from ..models.ai_chat_response_data_attributes import AiChatResponseDataAttributes


T = TypeVar("T", bound="AiChatResponseData")


@_attrs_define
class AiChatResponseData:
    """
    Attributes:
        id (UUID): Session UUID
        type_ (AiChatResponseDataType):
        attributes (AiChatResponseDataAttributes):
    """

    id: UUID
    type_: AiChatResponseDataType
    attributes: "AiChatResponseDataAttributes"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        type_: str = self.type_

        attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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
        from ..models.ai_chat_response_data_attributes import AiChatResponseDataAttributes

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        type_ = check_ai_chat_response_data_type(d.pop("type"))

        attributes = AiChatResponseDataAttributes.from_dict(d.pop("attributes"))

        ai_chat_response_data = cls(
            id=id,
            type_=type_,
            attributes=attributes,
        )

        ai_chat_response_data.additional_properties = d
        return ai_chat_response_data

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
