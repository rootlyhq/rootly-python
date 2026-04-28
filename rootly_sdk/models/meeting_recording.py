from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.meeting_recording_platform import MeetingRecordingPlatform, check_meeting_recording_platform
from ..models.meeting_recording_status import MeetingRecordingStatus, check_meeting_recording_status
from ..types import UNSET, Unset

T = TypeVar("T", bound="MeetingRecording")


@_attrs_define
class MeetingRecording:
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
        has_video (bool | Unset): Whether a video recording file is attached
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
    has_video: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        has_video = self.has_video

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
        if has_video is not UNSET:
            field_dict["has_video"] = has_video

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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

        has_video = d.pop("has_video", UNSET)

        meeting_recording = cls(
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
            has_video=has_video,
        )

        meeting_recording.additional_properties = d
        return meeting_recording

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
