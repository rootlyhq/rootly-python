from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.archive_google_chat_spaces_task_params_task_type import (
    ArchiveGoogleChatSpacesTaskParamsTaskType,
    check_archive_google_chat_spaces_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.archive_google_chat_spaces_task_params_spaces_item import ArchiveGoogleChatSpacesTaskParamsSpacesItem


T = TypeVar("T", bound="ArchiveGoogleChatSpacesTaskParams")


@_attrs_define
class ArchiveGoogleChatSpacesTaskParams:
    """
    Attributes:
        spaces (list[ArchiveGoogleChatSpacesTaskParamsSpacesItem]):
        task_type (ArchiveGoogleChatSpacesTaskParamsTaskType | Unset):
    """

    spaces: list[ArchiveGoogleChatSpacesTaskParamsSpacesItem]
    task_type: ArchiveGoogleChatSpacesTaskParamsTaskType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        spaces = []
        for spaces_item_data in self.spaces:
            spaces_item = spaces_item_data.to_dict()
            spaces.append(spaces_item)

        task_type: str | Unset = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "spaces": spaces,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.archive_google_chat_spaces_task_params_spaces_item import (
            ArchiveGoogleChatSpacesTaskParamsSpacesItem,
        )

        d = dict(src_dict)
        spaces = []
        _spaces = d.pop("spaces")
        for spaces_item_data in _spaces:
            spaces_item = ArchiveGoogleChatSpacesTaskParamsSpacesItem.from_dict(spaces_item_data)

            spaces.append(spaces_item)

        _task_type = d.pop("task_type", UNSET)
        task_type: ArchiveGoogleChatSpacesTaskParamsTaskType | Unset
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_archive_google_chat_spaces_task_params_task_type(_task_type)

        archive_google_chat_spaces_task_params = cls(
            spaces=spaces,
            task_type=task_type,
        )

        archive_google_chat_spaces_task_params.additional_properties = d
        return archive_google_chat_spaces_task_params

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
