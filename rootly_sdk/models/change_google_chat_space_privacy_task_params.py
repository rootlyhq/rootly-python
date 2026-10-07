from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.change_google_chat_space_privacy_task_params_task_type import (
    ChangeGoogleChatSpacePrivacyTaskParamsTaskType,
    check_change_google_chat_space_privacy_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.change_google_chat_space_privacy_task_params_space import ChangeGoogleChatSpacePrivacyTaskParamsSpace


T = TypeVar("T", bound="ChangeGoogleChatSpacePrivacyTaskParams")


@_attrs_define
class ChangeGoogleChatSpacePrivacyTaskParams:
    """
    Attributes:
        space (ChangeGoogleChatSpacePrivacyTaskParamsSpace):
        task_type (ChangeGoogleChatSpacePrivacyTaskParamsTaskType | Unset):
        audience (None | str | Unset): Target audience resource name (e.g. audiences/default). Leave blank to make
            private.
    """

    space: ChangeGoogleChatSpacePrivacyTaskParamsSpace
    task_type: ChangeGoogleChatSpacePrivacyTaskParamsTaskType | Unset = UNSET
    audience: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        space = self.space.to_dict()

        task_type: str | Unset = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        audience: None | str | Unset
        if isinstance(self.audience, Unset):
            audience = UNSET
        else:
            audience = self.audience

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "space": space,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if audience is not UNSET:
            field_dict["audience"] = audience

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.change_google_chat_space_privacy_task_params_space import (
            ChangeGoogleChatSpacePrivacyTaskParamsSpace,
        )

        d = dict(src_dict)
        space = ChangeGoogleChatSpacePrivacyTaskParamsSpace.from_dict(d.pop("space"))

        _task_type = d.pop("task_type", UNSET)
        task_type: ChangeGoogleChatSpacePrivacyTaskParamsTaskType | Unset
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_change_google_chat_space_privacy_task_params_task_type(_task_type)

        def _parse_audience(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        audience = _parse_audience(d.pop("audience", UNSET))

        change_google_chat_space_privacy_task_params = cls(
            space=space,
            task_type=task_type,
            audience=audience,
        )

        change_google_chat_space_privacy_task_params.additional_properties = d
        return change_google_chat_space_privacy_task_params

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
