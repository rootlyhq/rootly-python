from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_microsoft_teams_chat_task_params_chat_type import (
    CreateMicrosoftTeamsChatTaskParamsChatType,
    check_create_microsoft_teams_chat_task_params_chat_type,
)
from ..models.create_microsoft_teams_chat_task_params_task_type import (
    CreateMicrosoftTeamsChatTaskParamsTaskType,
    check_create_microsoft_teams_chat_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_microsoft_teams_chat_task_params_members_item import (
        CreateMicrosoftTeamsChatTaskParamsMembersItem,
    )


T = TypeVar("T", bound="CreateMicrosoftTeamsChatTaskParams")


@_attrs_define
class CreateMicrosoftTeamsChatTaskParams:
    """
    Attributes:
        members (list['CreateMicrosoftTeamsChatTaskParamsMembersItem']): Array of members to include in the chat
        task_type (Union[Unset, CreateMicrosoftTeamsChatTaskParamsTaskType]):
        topic (Union[None, Unset, str]): Chat topic (only for group chats)
        chat_type (Union[Unset, CreateMicrosoftTeamsChatTaskParamsChatType]): Type of chat to create Default: 'group'.
    """

    members: list["CreateMicrosoftTeamsChatTaskParamsMembersItem"]
    task_type: Unset | CreateMicrosoftTeamsChatTaskParamsTaskType = UNSET
    topic: None | Unset | str = UNSET
    chat_type: Unset | CreateMicrosoftTeamsChatTaskParamsChatType = "group"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        members = []
        for members_item_data in self.members:
            members_item = members_item_data.to_dict()
            members.append(members_item)

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        topic: None | Unset | str
        if isinstance(self.topic, Unset):
            topic = UNSET
        else:
            topic = self.topic

        chat_type: Unset | str = UNSET
        if not isinstance(self.chat_type, Unset):
            chat_type = self.chat_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "members": members,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if topic is not UNSET:
            field_dict["topic"] = topic
        if chat_type is not UNSET:
            field_dict["chat_type"] = chat_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_microsoft_teams_chat_task_params_members_item import (
            CreateMicrosoftTeamsChatTaskParamsMembersItem,
        )

        d = dict(src_dict)
        members = []
        _members = d.pop("members")
        for members_item_data in _members:
            members_item = CreateMicrosoftTeamsChatTaskParamsMembersItem.from_dict(members_item_data)

            members.append(members_item)

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | CreateMicrosoftTeamsChatTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_create_microsoft_teams_chat_task_params_task_type(_task_type)

        def _parse_topic(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        topic = _parse_topic(d.pop("topic", UNSET))

        _chat_type = d.pop("chat_type", UNSET)
        chat_type: Unset | CreateMicrosoftTeamsChatTaskParamsChatType
        if isinstance(_chat_type, Unset):
            chat_type = UNSET
        else:
            chat_type = check_create_microsoft_teams_chat_task_params_chat_type(_chat_type)

        create_microsoft_teams_chat_task_params = cls(
            members=members,
            task_type=task_type,
            topic=topic,
            chat_type=chat_type,
        )

        create_microsoft_teams_chat_task_params.additional_properties = d
        return create_microsoft_teams_chat_task_params

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
