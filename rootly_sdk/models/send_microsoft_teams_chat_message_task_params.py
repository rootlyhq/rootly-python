from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.send_microsoft_teams_chat_message_task_params_task_type import (
    SendMicrosoftTeamsChatMessageTaskParamsTaskType,
    check_send_microsoft_teams_chat_message_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.send_microsoft_teams_chat_message_task_params_chats_item import (
        SendMicrosoftTeamsChatMessageTaskParamsChatsItem,
    )


T = TypeVar("T", bound="SendMicrosoftTeamsChatMessageTaskParams")


@_attrs_define
class SendMicrosoftTeamsChatMessageTaskParams:
    """
    Attributes:
        chats (list['SendMicrosoftTeamsChatMessageTaskParamsChatsItem']):
        text (str): The message text
        task_type (Union[Unset, SendMicrosoftTeamsChatMessageTaskParamsTaskType]):
    """

    chats: list["SendMicrosoftTeamsChatMessageTaskParamsChatsItem"]
    text: str
    task_type: Unset | SendMicrosoftTeamsChatMessageTaskParamsTaskType = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chats = []
        for chats_item_data in self.chats:
            chats_item = chats_item_data.to_dict()
            chats.append(chats_item)

        text = self.text

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chats": chats,
                "text": text,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.send_microsoft_teams_chat_message_task_params_chats_item import (
            SendMicrosoftTeamsChatMessageTaskParamsChatsItem,
        )

        d = dict(src_dict)
        chats = []
        _chats = d.pop("chats")
        for chats_item_data in _chats:
            chats_item = SendMicrosoftTeamsChatMessageTaskParamsChatsItem.from_dict(chats_item_data)

            chats.append(chats_item)

        text = d.pop("text")

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | SendMicrosoftTeamsChatMessageTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_send_microsoft_teams_chat_message_task_params_task_type(_task_type)

        send_microsoft_teams_chat_message_task_params = cls(
            chats=chats,
            text=text,
            task_type=task_type,
        )

        send_microsoft_teams_chat_message_task_params.additional_properties = d
        return send_microsoft_teams_chat_message_task_params

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
