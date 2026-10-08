from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="AcknowledgeAlertDataAttributesActorType1")


@_attrs_define
class AcknowledgeAlertDataAttributesActorType1:
    """
    Attributes:
        user_id (str): Rootly ID of the user.
    """

    user_id: str

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "user_id": user_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("user_id")

        acknowledge_alert_data_attributes_actor_type_1 = cls(
            user_id=user_id,
        )

        return acknowledge_alert_data_attributes_actor_type_1
