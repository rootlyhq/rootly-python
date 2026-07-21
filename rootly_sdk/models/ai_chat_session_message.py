from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.ai_chat_session_message_role import AiChatSessionMessageRole, check_ai_chat_session_message_role

T = TypeVar("T", bound="AiChatSessionMessage")


@_attrs_define
class AiChatSessionMessage:
    """
    Attributes:
        id (UUID): Message UUID
        role (AiChatSessionMessageRole): Message author role
        content (str): Message content
        created_at (datetime.datetime): When the message was created
    """

    id: UUID
    role: AiChatSessionMessageRole
    content: str
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        role: str = self.role

        content = self.content

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "role": role,
                "content": content,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        role = check_ai_chat_session_message_role(d.pop("role"))

        content = d.pop("content")

        created_at = isoparse(d.pop("created_at"))

        ai_chat_session_message = cls(
            id=id,
            role=role,
            content=content,
            created_at=created_at,
        )

        ai_chat_session_message.additional_properties = d
        return ai_chat_session_message

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
