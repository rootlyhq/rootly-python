from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="NewAlertDataAttributesActorType3Type0")


@_attrs_define
class NewAlertDataAttributesActorType3Type0:
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

        new_alert_data_attributes_actor_type_3_type_0 = cls(
            email=email,
        )

        return new_alert_data_attributes_actor_type_3_type_0
