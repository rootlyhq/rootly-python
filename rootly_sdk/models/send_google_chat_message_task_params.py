from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.send_google_chat_message_task_params_task_type import (
    SendGoogleChatMessageTaskParamsTaskType,
    check_send_google_chat_message_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.send_google_chat_message_task_params_spaces_item import SendGoogleChatMessageTaskParamsSpacesItem


T = TypeVar("T", bound="SendGoogleChatMessageTaskParams")


@_attrs_define
class SendGoogleChatMessageTaskParams:
    """
    Attributes:
        spaces (list['SendGoogleChatMessageTaskParamsSpacesItem']):
        text (str):
        task_type (Union[Unset, SendGoogleChatMessageTaskParamsTaskType]):
        thread_key (Union[None, Unset, str]): Thread key to reply within a thread. Messages with the same thread key are
            grouped together
    """

    spaces: list["SendGoogleChatMessageTaskParamsSpacesItem"]
    text: str
    task_type: Union[Unset, SendGoogleChatMessageTaskParamsTaskType] = UNSET
    thread_key: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        spaces = []
        for spaces_item_data in self.spaces:
            spaces_item = spaces_item_data.to_dict()
            spaces.append(spaces_item)

        text = self.text

        task_type: Union[Unset, str] = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        thread_key: Union[None, Unset, str]
        if isinstance(self.thread_key, Unset):
            thread_key = UNSET
        else:
            thread_key = self.thread_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "spaces": spaces,
                "text": text,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if thread_key is not UNSET:
            field_dict["thread_key"] = thread_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.send_google_chat_message_task_params_spaces_item import SendGoogleChatMessageTaskParamsSpacesItem

        d = dict(src_dict)
        spaces = []
        _spaces = d.pop("spaces")
        for spaces_item_data in _spaces:
            spaces_item = SendGoogleChatMessageTaskParamsSpacesItem.from_dict(spaces_item_data)

            spaces.append(spaces_item)

        text = d.pop("text")

        _task_type = d.pop("task_type", UNSET)
        task_type: Union[Unset, SendGoogleChatMessageTaskParamsTaskType]
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_send_google_chat_message_task_params_task_type(_task_type)

        def _parse_thread_key(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        thread_key = _parse_thread_key(d.pop("thread_key", UNSET))

        send_google_chat_message_task_params = cls(
            spaces=spaces,
            text=text,
            task_type=task_type,
            thread_key=thread_key,
        )

        send_google_chat_message_task_params.additional_properties = d
        return send_google_chat_message_task_params

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
