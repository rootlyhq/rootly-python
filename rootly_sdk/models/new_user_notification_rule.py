from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.new_user_notification_rule_data import NewUserNotificationRuleData


T = TypeVar("T", bound="NewUserNotificationRule")


@_attrs_define
class NewUserNotificationRule:
    """
    Attributes:
        data (NewUserNotificationRuleData):
    """

    data: NewUserNotificationRuleData

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_user_notification_rule_data import NewUserNotificationRuleData

        d = dict(src_dict)
        data = NewUserNotificationRuleData.from_dict(d.pop("data"))

        new_user_notification_rule = cls(
            data=data,
        )

        return new_user_notification_rule
