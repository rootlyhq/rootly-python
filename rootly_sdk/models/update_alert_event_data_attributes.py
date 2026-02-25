from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAlertEventDataAttributes")


@_attrs_define
class UpdateAlertEventDataAttributes:
    """
    Attributes:
        details (str): Note message.
        user_id (Union[Unset, int]): Author of the note.
    """

    details: str
    user_id: Unset | int = UNSET

    def to_dict(self) -> dict[str, Any]:
        details = self.details

        user_id = self.user_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "details": details,
            }
        )
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        details = d.pop("details")

        user_id = d.pop("user_id", UNSET)

        update_alert_event_data_attributes = cls(
            details=details,
            user_id=user_id,
        )

        return update_alert_event_data_attributes
