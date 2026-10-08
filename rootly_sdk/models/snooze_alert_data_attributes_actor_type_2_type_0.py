from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SnoozeAlertDataAttributesActorType2Type0")


@_attrs_define
class SnoozeAlertDataAttributesActorType2Type0:
    """
    Attributes:
        email (str): Email of the user, including verified secondary emails.
    """

    email: str

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "email": email,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        snooze_alert_data_attributes_actor_type_2_type_0 = cls(
            email=email,
        )

        return snooze_alert_data_attributes_actor_type_2_type_0
