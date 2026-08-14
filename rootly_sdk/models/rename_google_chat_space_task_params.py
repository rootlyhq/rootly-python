from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rename_google_chat_space_task_params_task_type import (
    RenameGoogleChatSpaceTaskParamsTaskType,
    check_rename_google_chat_space_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rename_google_chat_space_task_params_space import RenameGoogleChatSpaceTaskParamsSpace


T = TypeVar("T", bound="RenameGoogleChatSpaceTaskParams")


@_attrs_define
class RenameGoogleChatSpaceTaskParams:
    """
    Attributes:
        space (RenameGoogleChatSpaceTaskParamsSpace):
        title (str):
        task_type (Union[Unset, RenameGoogleChatSpaceTaskParamsTaskType]):
    """

    space: "RenameGoogleChatSpaceTaskParamsSpace"
    title: str
    task_type: Union[Unset, RenameGoogleChatSpaceTaskParamsTaskType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        space = self.space.to_dict()

        title = self.title

        task_type: Union[Unset, str] = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "space": space,
                "title": title,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rename_google_chat_space_task_params_space import RenameGoogleChatSpaceTaskParamsSpace

        d = dict(src_dict)
        space = RenameGoogleChatSpaceTaskParamsSpace.from_dict(d.pop("space"))

        title = d.pop("title")

        _task_type = d.pop("task_type", UNSET)
        task_type: Union[Unset, RenameGoogleChatSpaceTaskParamsTaskType]
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_rename_google_chat_space_task_params_task_type(_task_type)

        rename_google_chat_space_task_params = cls(
            space=space,
            title=title,
            task_type=task_type,
        )

        rename_google_chat_space_task_params.additional_properties = d
        return rename_google_chat_space_task_params

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
