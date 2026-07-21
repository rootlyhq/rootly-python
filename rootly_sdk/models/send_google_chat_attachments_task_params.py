from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.send_google_chat_attachments_task_params_task_type import (
    check_send_google_chat_attachments_task_params_task_type,
)
from ..models.send_google_chat_attachments_task_params_task_type import SendGoogleChatAttachmentsTaskParamsTaskType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.send_google_chat_attachments_task_params_spaces_item import (
        SendGoogleChatAttachmentsTaskParamsSpacesItem,
    )


T = TypeVar("T", bound="SendGoogleChatAttachmentsTaskParams")


@_attrs_define
class SendGoogleChatAttachmentsTaskParams:
    """
    Attributes:
        spaces (list[SendGoogleChatAttachmentsTaskParamsSpacesItem]):
        attachments (str):
        task_type (SendGoogleChatAttachmentsTaskParamsTaskType | Unset):
    """

    spaces: list[SendGoogleChatAttachmentsTaskParamsSpacesItem]
    attachments: str
    task_type: SendGoogleChatAttachmentsTaskParamsTaskType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.send_google_chat_attachments_task_params_spaces_item import (
            SendGoogleChatAttachmentsTaskParamsSpacesItem,
        )

        spaces = []
        for spaces_item_data in self.spaces:
            spaces_item = spaces_item_data.to_dict()
            spaces.append(spaces_item)

        attachments = self.attachments

        task_type: str | Unset = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "spaces": spaces,
                "attachments": attachments,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.send_google_chat_attachments_task_params_spaces_item import (
            SendGoogleChatAttachmentsTaskParamsSpacesItem,
        )

        d = dict(src_dict)
        spaces = []
        _spaces = d.pop("spaces")
        for spaces_item_data in _spaces:
            spaces_item = SendGoogleChatAttachmentsTaskParamsSpacesItem.from_dict(spaces_item_data)

            spaces.append(spaces_item)

        attachments = d.pop("attachments")

        _task_type = d.pop("task_type", UNSET)
        task_type: SendGoogleChatAttachmentsTaskParamsTaskType | Unset
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_send_google_chat_attachments_task_params_task_type(_task_type)

        send_google_chat_attachments_task_params = cls(
            spaces=spaces,
            attachments=attachments,
            task_type=task_type,
        )

        send_google_chat_attachments_task_params.additional_properties = d
        return send_google_chat_attachments_task_params

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
