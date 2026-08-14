from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="InviteToSlackChannelTaskParamsType2")


@_attrs_define
class InviteToSlackChannelTaskParamsType2:
    """
    Attributes:
        slack_emails (str):
    """

    slack_emails: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        slack_emails = self.slack_emails

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "slack_emails": slack_emails,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        slack_emails = d.pop("slack_emails")

        invite_to_slack_channel_task_params_type_2 = cls(
            slack_emails=slack_emails,
        )

        invite_to_slack_channel_task_params_type_2.additional_properties = d
        return invite_to_slack_channel_task_params_type_2

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
