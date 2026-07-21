from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.new_alert_event_data_attributes_kind import check_new_alert_event_data_attributes_kind
from ..models.new_alert_event_data_attributes_kind import NewAlertEventDataAttributesKind
from ..types import UNSET, Unset
from typing import cast


T = TypeVar("T", bound="NewAlertEventDataAttributes")


@_attrs_define
class NewAlertEventDataAttributes:
    """
    Attributes:
        kind (NewAlertEventDataAttributesKind):
        details (str): Note message.
        user_id (int | Unset): Author of the note.
    """

    kind: NewAlertEventDataAttributesKind
    details: str
    user_id: int | Unset = UNSET

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
