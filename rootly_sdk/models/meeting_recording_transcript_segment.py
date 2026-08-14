from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.meeting_recording_transcript_word import MeetingRecordingTranscriptWord


T = TypeVar("T", bound="MeetingRecordingTranscriptSegment")


@_attrs_define
class MeetingRecordingTranscriptSegment:
    """
    Attributes:
        speaker (str): Speaker label (e.g. Speaker 1)
        words (list['MeetingRecordingTranscriptWord']): Timestamped words spoken by this speaker
    """

    speaker: str
    words: list["MeetingRecordingTranscriptWord"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        speaker = self.speaker

        words = []
        for words_item_data in self.words:
            words_item = words_item_data.to_dict()
            words.append(words_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "speaker": speaker,
                "words": words,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.meeting_recording_transcript_word import MeetingRecordingTranscriptWord

        d = dict(src_dict)
        speaker = d.pop("speaker")

        words = []
        _words = d.pop("words")
        for words_item_data in _words:
            words_item = MeetingRecordingTranscriptWord.from_dict(words_item_data)

            words.append(words_item)

        meeting_recording_transcript_segment = cls(
            speaker=speaker,
            words=words,
        )

        meeting_recording_transcript_segment.additional_properties = d
        return meeting_recording_transcript_segment

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
