from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invite_to_google_chat_space_task_params_task_type import (
    InviteToGoogleChatSpaceTaskParamsTaskType,
    check_invite_to_google_chat_space_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invite_to_google_chat_space_task_params_space import InviteToGoogleChatSpaceTaskParamsSpace


T = TypeVar("T", bound="InviteToGoogleChatSpaceTaskParams")


@_attrs_define
class InviteToGoogleChatSpaceTaskParams:
    """
    Attributes:
        space (InviteToGoogleChatSpaceTaskParamsSpace):
        emails (str): Comma separated list of emails to invite
        task_type (Union[Unset, InviteToGoogleChatSpaceTaskParamsTaskType]):
    """

    space: "InviteToGoogleChatSpaceTaskParamsSpace"
    emails: str
    task_type: Unset | InviteToGoogleChatSpaceTaskParamsTaskType = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        space = self.space.to_dict()

        emails = self.emails

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "space": space,
                "emails": emails,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.invite_to_google_chat_space_task_params_space import InviteToGoogleChatSpaceTaskParamsSpace

        d = dict(src_dict)
        space = InviteToGoogleChatSpaceTaskParamsSpace.from_dict(d.pop("space"))

        emails = d.pop("emails")

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | InviteToGoogleChatSpaceTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_invite_to_google_chat_space_task_params_task_type(_task_type)

        invite_to_google_chat_space_task_params = cls(
            space=space,
            emails=emails,
            task_type=task_type,
        )

        invite_to_google_chat_space_task_params.additional_properties = d
        return invite_to_google_chat_space_task_params

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
