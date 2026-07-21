from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.ai_chat_session_message import AiChatSessionMessage
    from ..models.ai_chat_session_message_list_meta import AiChatSessionMessageListMeta


T = TypeVar("T", bound="AiChatSessionMessageList")


@_attrs_define
class AiChatSessionMessageList:
    """
    Attributes:
        messages (list[AiChatSessionMessage]):
        meta (AiChatSessionMessageListMeta | Unset):
    """

    messages: list[AiChatSessionMessage]
    meta: AiChatSessionMessageListMeta | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.ai_chat_session_message_list_meta import AiChatSessionMessageListMeta
        from ..models.ai_chat_session_message import AiChatSessionMessage

        messages = []
        for messages_item_data in self.messages:
            messages_item = messages_item_data.to_dict()
            messages.append(messages_item)

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "messages": messages,
            }
        )
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ai_chat_session_message import AiChatSessionMessage
        from ..models.ai_chat_session_message_list_meta import AiChatSessionMessageListMeta

        d = dict(src_dict)
        messages = []
        _messages = d.pop("messages")
        for messages_item_data in _messages:
            messages_item = AiChatSessionMessage.from_dict(messages_item_data)

            messages.append(messages_item)

        _meta = d.pop("meta", UNSET)
        meta: AiChatSessionMessageListMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = AiChatSessionMessageListMeta.from_dict(_meta)

        ai_chat_session_message_list = cls(
            messages=messages,
            meta=meta,
        )

        ai_chat_session_message_list.additional_properties = d
        return ai_chat_session_message_list

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
