from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.add_microsoft_teams_chat_tab_task_params_task_type import (
    AddMicrosoftTeamsChatTabTaskParamsTaskType,
    check_add_microsoft_teams_chat_tab_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.add_microsoft_teams_chat_tab_task_params_chat import AddMicrosoftTeamsChatTabTaskParamsChat


T = TypeVar("T", bound="AddMicrosoftTeamsChatTabTaskParams")


@_attrs_define
class AddMicrosoftTeamsChatTabTaskParams:
    """
    Attributes:
        chat (AddMicrosoftTeamsChatTabTaskParamsChat):
        title (str): The tab title
        link (str): The tab link
        task_type (Union[Unset, AddMicrosoftTeamsChatTabTaskParamsTaskType]):
    """

    chat: "AddMicrosoftTeamsChatTabTaskParamsChat"
    title: str
    link: str
    task_type: Union[Unset, AddMicrosoftTeamsChatTabTaskParamsTaskType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chat = self.chat.to_dict()

        title = self.title

        link = self.link

        task_type: Union[Unset, str] = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chat": chat,
                "title": title,
                "link": link,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_microsoft_teams_chat_tab_task_params_chat import AddMicrosoftTeamsChatTabTaskParamsChat

        d = dict(src_dict)
        chat = AddMicrosoftTeamsChatTabTaskParamsChat.from_dict(d.pop("chat"))

        title = d.pop("title")

        link = d.pop("link")

        _task_type = d.pop("task_type", UNSET)
        task_type: Union[Unset, AddMicrosoftTeamsChatTabTaskParamsTaskType]
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_add_microsoft_teams_chat_tab_task_params_task_type(_task_type)

        add_microsoft_teams_chat_tab_task_params = cls(
            chat=chat,
            title=title,
            link=link,
            task_type=task_type,
        )

        add_microsoft_teams_chat_tab_task_params.additional_properties = d
        return add_microsoft_teams_chat_tab_task_params

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
