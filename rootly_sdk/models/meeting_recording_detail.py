from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.meeting_recording_platform import check_meeting_recording_platform
from ..models.meeting_recording_platform import MeetingRecordingPlatform
from ..models.meeting_recording_status import check_meeting_recording_status
from ..models.meeting_recording_status import MeetingRecordingStatus
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
    from ..models.meeting_recording_detail_transcript_type_1 import MeetingRecordingDetailTranscriptType1
    from ..models.meeting_recording_transcript_segment import MeetingRecordingTranscriptSegment


T = TypeVar("T", bound="MeetingRecordingDetail")


@_attrs_define
class MeetingRecordingDetail:
    """
    Attributes:
        platform (MeetingRecordingPlatform): Meeting platform
        session_number (int): Session number within the incident for this platform (starts at 1, increments on re-
            invite)
        status (MeetingRecordingStatus): Current recording lifecycle status
        created_at (datetime.datetime): When the recording session was created
        updated_at (datetime.datetime): When the recording session was last updated
        started_at (datetime.datetime | None | Unset): When the bot started recording (null if bot never joined)
        ended_at (datetime.datetime | None | Unset): When the recording ended
        duration_minutes (float | None | Unset): Recording duration in minutes (null if not started)
        speaker_count (int | Unset): Number of unique speakers detected in the transcript
        word_count (int | Unset): Total word count across all transcript segments
        transcript_summary (None | str | Unset): AI-generated summary of the meeting transcript (null if no transcript
            or not yet analyzed)
        title (None | str | Unset): Human-readable label for the recording session
        meeting_url (None | str | Unset): Original meeting URL
        video_url (None | str | Unset): Signed URL to stream/download the video recording
        created_by (None | str | Unset): Source that created the recording (e.g. desktop_sdk, recall_bot)
        transcript (list[MeetingRecordingTranscriptSegment] | MeetingRecordingDetailTranscriptType1 | Unset): Array of
            speaker segments when populated, empty object when no transcript exists.
        recall_upload_id (None | str | Unset): Recall upload identifier
        recordable_id (None | str | Unset): UUID of the associated recordable (e.g. incident)
        recordable_type (None | str | Unset): Type of the associated recordable (e.g. Incident)
    """

    platform: MeetingRecordingPlatform
    session_number: int
    status: MeetingRecordingStatus
    created_at: datetime.datetime
    updated_at: datetime.datetime
    started_at: datetime.datetime | None | Unset = UNSET
    ended_at: datetime.datetime | None | Unset = UNSET
    duration_minutes: float | None | Unset = UNSET
    speaker_count: int | Unset = UNSET
    word_count: int | Unset = UNSET
    transcript_summary: None | str | Unset = UNSET
    title: None | str | Unset = UNSET
    meeting_url: None | str | Unset = UNSET
    video_url: None | str | Unset = UNSET
    created_by: None | str | Unset = UNSET
    transcript: list[MeetingRecordingTranscriptSegment] | MeetingRecordingDetailTranscriptType1 | Unset = UNSET
    recall_upload_id: None | str | Unset = UNSET
    recordable_id: None | str | Unset = UNSET
    recordable_type: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.meeting_recording_transcript_segment import MeetingRecordingTranscriptSegment
        from ..models.meeting_recording_detail_transcript_type_1 import MeetingRecordingDetailTranscriptType1

        platform: str = self.platform

        session_number = self.session_number

        status: str = self.status

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        started_at: None | str | Unset
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        elif isinstance(self.started_at, datetime.datetime):
            started_at = self.started_at.isoformat()
        else:
            started_at = self.started_at

        ended_at: None | str | Unset
        if isinstance(self.ended_at, Unset):
            ended_at = UNSET
        elif isinstance(self.ended_at, datetime.datetime):
            ended_at = self.ended_at.isoformat()
        else:
            ended_at = self.ended_at

        duration_minutes: float | None | Unset
        if isinstance(self.duration_minutes, Unset):
            duration_minutes = UNSET
        else:
            duration_minutes = self.duration_minutes

        speaker_count = self.speaker_count

        word_count = self.word_count

        transcript_summary: None | str | Unset
        if isinstance(self.transcript_summary, Unset):
            transcript_summary = UNSET
        else:
            transcript_summary = self.transcript_summary

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        meeting_url: None | str | Unset
        if isinstance(self.meeting_url, Unset):
            meeting_url = UNSET
        else:
            meeting_url = self.meeting_url

        video_url: None | str | Unset
        if isinstance(self.video_url, Unset):
            video_url = UNSET
        else:
            video_url = self.video_url

        created_by: None | str | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        transcript: dict[str, Any] | list[dict[str, Any]] | Unset
        if isinstance(self.transcript, Unset):
            transcript = UNSET
        elif isinstance(self.transcript, list):
            transcript = []
            for transcript_type_0_item_data in self.transcript:
                transcript_type_0_item = transcript_type_0_item_data.to_dict()
                transcript.append(transcript_type_0_item)

        else:
            transcript = self.transcript.to_dict()

        recall_upload_id: None | str | Unset
        if isinstance(self.recall_upload_id, Unset):
            recall_upload_id = UNSET
        else:
            recall_upload_id = self.recall_upload_id

        recordable_id: None | str | Unset
        if isinstance(self.recordable_id, Unset):
            recordable_id = UNSET
        else:
            recordable_id = self.recordable_id

        recordable_type: None | str | Unset
        if isinstance(self.recordable_type, Unset):
            recordable_type = UNSET
        else:
            recordable_type = self.recordable_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "platform": platform,
                "session_number": session_number,
                "status": status,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if ended_at is not UNSET:
            field_dict["ended_at"] = ended_at
        if duration_minutes is not UNSET:
            field_dict["duration_minutes"] = duration_minutes
        if speaker_count is not UNSET:
            field_dict["speaker_count"] = speaker_count
        if word_count is not UNSET:
            field_dict["word_count"] = word_count
        if transcript_summary is not UNSET:
            field_dict["transcript_summary"] = transcript_summary
        if title is not UNSET:
            field_dict["title"] = title
        if meeting_url is not UNSET:
            field_dict["meeting_url"] = meeting_url
        if video_url is not UNSET:
            field_dict["video_url"] = video_url
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if transcript is not UNSET:
            field_dict["transcript"] = transcript
        if recall_upload_id is not UNSET:
            field_dict["recall_upload_id"] = recall_upload_id
        if recordable_id is not UNSET:
            field_dict["recordable_id"] = recordable_id
        if recordable_type is not UNSET:
            field_dict["recordable_type"] = recordable_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.meeting_recording_detail_transcript_type_1 import MeetingRecordingDetailTranscriptType1
        from ..models.meeting_recording_transcript_segment import MeetingRecordingTranscriptSegment

        d = dict(src_dict)
        platform = check_meeting_recording_platform(d.pop("platform"))

        session_number = d.pop("session_number")

        status = check_meeting_recording_status(d.pop("status"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        def _parse_started_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                started_at_type_0 = isoparse(data)

                return started_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        started_at = _parse_started_at(d.pop("started_at", UNSET))

        def _parse_ended_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ended_at_type_0 = isoparse(data)

                return ended_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        ended_at = _parse_ended_at(d.pop("ended_at", UNSET))

        def _parse_duration_minutes(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        duration_minutes = _parse_duration_minutes(d.pop("duration_minutes", UNSET))

        speaker_count = d.pop("speaker_count", UNSET)

        word_count = d.pop("word_count", UNSET)

        def _parse_transcript_summary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        transcript_summary = _parse_transcript_summary(d.pop("transcript_summary", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_meeting_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        meeting_url = _parse_meeting_url(d.pop("meeting_url", UNSET))

        def _parse_video_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        video_url = _parse_video_url(d.pop("video_url", UNSET))

        def _parse_created_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))

        def _parse_transcript(
            data: object,
        ) -> list[MeetingRecordingTranscriptSegment] | MeetingRecordingDetailTranscriptType1 | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                transcript_type_0 = []
                _transcript_type_0 = data
                for transcript_type_0_item_data in _transcript_type_0:
                    transcript_type_0_item = MeetingRecordingTranscriptSegment.from_dict(transcript_type_0_item_data)

                    transcript_type_0.append(transcript_type_0_item)

                return transcript_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            transcript_type_1 = MeetingRecordingDetailTranscriptType1.from_dict(data)

            return transcript_type_1

        transcript = _parse_transcript(d.pop("transcript", UNSET))

        def _parse_recall_upload_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        recall_upload_id = _parse_recall_upload_id(d.pop("recall_upload_id", UNSET))

        def _parse_recordable_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        recordable_id = _parse_recordable_id(d.pop("recordable_id", UNSET))

        def _parse_recordable_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        recordable_type = _parse_recordable_type(d.pop("recordable_type", UNSET))

        meeting_recording_detail = cls(
            platform=platform,
            session_number=session_number,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
            started_at=started_at,
            ended_at=ended_at,
            duration_minutes=duration_minutes,
            speaker_count=speaker_count,
            word_count=word_count,
            transcript_summary=transcript_summary,
            title=title,
            meeting_url=meeting_url,
            video_url=video_url,
            created_by=created_by,
            transcript=transcript,
            recall_upload_id=recall_upload_id,
            recordable_id=recordable_id,
            recordable_type=recordable_type,
        )

        meeting_recording_detail.additional_properties = d
        return meeting_recording_detail

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
