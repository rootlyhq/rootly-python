from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.remove_from_slack_channel_task_params_target_kind import (
    RemoveFromSlackChannelTaskParamsTargetKind,
    check_remove_from_slack_channel_task_params_target_kind,
)
from ..models.remove_from_slack_channel_task_params_task_type import (
    RemoveFromSlackChannelTaskParamsTaskType,
    check_remove_from_slack_channel_task_params_task_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RemoveFromSlackChannelTaskParams")


@_attrs_define
class RemoveFromSlackChannelTaskParams:
    """
    Attributes:
        task_type (RemoveFromSlackChannelTaskParamsTaskType | Unset):
        target_kind (RemoveFromSlackChannelTaskParamsTargetKind | Unset):
        dry_run (bool | Unset):
    """

    task_type: RemoveFromSlackChannelTaskParamsTaskType | Unset = UNSET
    target_kind: RemoveFromSlackChannelTaskParamsTargetKind | Unset = UNSET
    dry_run: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        task_type: str | Unset = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        target_kind: str | Unset = UNSET
        if not isinstance(self.target_kind, Unset):
            target_kind = self.target_kind

        dry_run = self.dry_run

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if target_kind is not UNSET:
            field_dict["target_kind"] = target_kind
        if dry_run is not UNSET:
            field_dict["dry_run"] = dry_run

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _task_type = d.pop("task_type", UNSET)
        task_type: RemoveFromSlackChannelTaskParamsTaskType | Unset
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_remove_from_slack_channel_task_params_task_type(_task_type)

        _target_kind = d.pop("target_kind", UNSET)
        target_kind: RemoveFromSlackChannelTaskParamsTargetKind | Unset
        if isinstance(_target_kind, Unset):
            target_kind = UNSET
        else:
            target_kind = check_remove_from_slack_channel_task_params_target_kind(_target_kind)

        dry_run = d.pop("dry_run", UNSET)

        remove_from_slack_channel_task_params = cls(
            task_type=task_type,
            target_kind=target_kind,
            dry_run=dry_run,
        )

        remove_from_slack_channel_task_params.additional_properties = d
        return remove_from_slack_channel_task_params

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
