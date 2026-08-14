from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MeetingRecordingTranscriptWord")


@_attrs_define
class MeetingRecordingTranscriptWord:
    """
    Attributes:
        text (str): Transcribed word
        start_timestamp (Union[Unset, float]): Start time in seconds from recording start
        end_timestamp (Union[Unset, float]): End time in seconds from recording start
    """

    text: str
    start_timestamp: Union[Unset, float] = UNSET
    end_timestamp: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        start_timestamp = self.start_timestamp

        end_timestamp = self.end_timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
            }
        )
        if start_timestamp is not UNSET:
            field_dict["start_timestamp"] = start_timestamp
        if end_timestamp is not UNSET:
            field_dict["end_timestamp"] = end_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        text = d.pop("text")

        start_timestamp = d.pop("start_timestamp", UNSET)

        end_timestamp = d.pop("end_timestamp", UNSET)

        meeting_recording_transcript_word = cls(
            text=text,
            start_timestamp=start_timestamp,
            end_timestamp=end_timestamp,
        )

        meeting_recording_transcript_word.additional_properties = d
        return meeting_recording_transcript_word

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
