from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ai_chat_response_data_attributes_status import (
    AiChatResponseDataAttributesStatus,
    check_ai_chat_response_data_attributes_status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AiChatResponseDataAttributes")


@_attrs_define
class AiChatResponseDataAttributes:
    """
    Attributes:
        session_id (UUID): AI chat session UUID
        reply (None | str | Unset): Assistant reply text
        status (AiChatResponseDataAttributesStatus | Unset): Response status (present when user input is required)
    """

    session_id: UUID
    reply: None | str | Unset = UNSET
    status: AiChatResponseDataAttributesStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        session_id = str(self.session_id)

        reply: None | str | Unset
        if isinstance(self.reply, Unset):
            reply = UNSET
        else:
            reply = self.reply

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "session_id": session_id,
            }
        )
        if reply is not UNSET:
            field_dict["reply"] = reply
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        session_id = UUID(d.pop("session_id"))

        def _parse_reply(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reply = _parse_reply(d.pop("reply", UNSET))

        _status = d.pop("status", UNSET)
        status: AiChatResponseDataAttributesStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_ai_chat_response_data_attributes_status(_status)

        ai_chat_response_data_attributes = cls(
            session_id=session_id,
            reply=reply,
            status=status,
        )

        ai_chat_response_data_attributes.additional_properties = d
        return ai_chat_response_data_attributes

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
