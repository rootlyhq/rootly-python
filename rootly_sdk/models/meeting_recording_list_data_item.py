from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.meeting_recording_list_data_item_type import (
    MeetingRecordingListDataItemType,
    check_meeting_recording_list_data_item_type,
)

if TYPE_CHECKING:
    from ..models.meeting_recording import MeetingRecording


T = TypeVar("T", bound="MeetingRecordingListDataItem")


@_attrs_define
class MeetingRecordingListDataItem:
    """
    Attributes:
        id (str): Unique UUID of the meeting recording
        type_ (MeetingRecordingListDataItemType):
        attributes (MeetingRecording):
    """

    id: str
    type_: MeetingRecordingListDataItemType
    attributes: MeetingRecording
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_: str = self.type_

        attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "attributes": attributes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.meeting_recording import MeetingRecording

        d = dict(src_dict)
        id = d.pop("id")

        type_ = check_meeting_recording_list_data_item_type(d.pop("type"))

        attributes = MeetingRecording.from_dict(d.pop("attributes"))

        meeting_recording_list_data_item = cls(
            id=id,
            type_=type_,
            attributes=attributes,
        )

        meeting_recording_list_data_item.additional_properties = d
        return meeting_recording_list_data_item

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
