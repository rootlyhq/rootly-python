from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.new_alert_event_data_attributes_kind import (
    NewAlertEventDataAttributesKind,
    check_new_alert_event_data_attributes_kind,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="NewAlertEventDataAttributes")


@_attrs_define
class NewAlertEventDataAttributes:
    """
    Attributes:
        kind (NewAlertEventDataAttributesKind):
        details (str): Note message.
        user_id (Union[Unset, int]): Author of the note.
    """

    kind: NewAlertEventDataAttributesKind
    details: str
    user_id: Unset | int = UNSET

    def to_dict(self) -> dict[str, Any]:
        kind: str = self.kind

        details = self.details

        user_id = self.user_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "kind": kind,
                "details": details,
            }
        )
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = check_new_alert_event_data_attributes_kind(d.pop("kind"))

        details = d.pop("details")

        user_id = d.pop("user_id", UNSET)

        new_alert_event_data_attributes = cls(
            kind=kind,
            details=details,
            user_id=user_id,
        )

        return new_alert_event_data_attributes
