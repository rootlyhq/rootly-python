from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.import_meeting_recording_platform import check_import_meeting_recording_platform
from ..models.import_meeting_recording_platform import ImportMeetingRecordingPlatform
from ..models.import_meeting_recording_source import check_import_meeting_recording_source
from ..models.import_meeting_recording_source import ImportMeetingRecordingSource
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime


T = TypeVar("T", bound="ImportMeetingRecording")


@_attrs_define
class ImportMeetingRecording:
    """
    Attributes:
        source (ImportMeetingRecordingSource): Import source (currently only "recall_desktop_sdk")
        recall_recording_id (UUID): External recording UUID (required when source is recall_desktop_sdk)
        platform (ImportMeetingRecordingPlatform): Meeting platform
        started_at (datetime.datetime | None | Unset): When the recording started
        ended_at (datetime.datetime | None | Unset): When the recording ended
        meeting_url (None | str | Unset): Original meeting URL
    """

    source: ImportMeetingRecordingSource
    recall_recording_id: UUID
    platform: ImportMeetingRecordingPlatform
    started_at: datetime.datetime | None | Unset = UNSET
    ended_at: datetime.datetime | None | Unset = UNSET
    meeting_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source: str = self.source

        recall_recording_id = str(self.recall_recording_id)

        platform: str = self.platform

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

        meeting_url: None | str | Unset
        if isinstance(self.meeting_url, Unset):
            meeting_url = UNSET
        else:
            meeting_url = self.meeting_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source": source,
                "recall_recording_id": recall_recording_id,
                "platform": platform,
            }
        )
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if ended_at is not UNSET:
            field_dict["ended_at"] = ended_at
        if meeting_url is not UNSET:
            field_dict["meeting_url"] = meeting_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source = check_import_meeting_recording_source(d.pop("source"))

        recall_recording_id = UUID(d.pop("recall_recording_id"))

        platform = check_import_meeting_recording_platform(d.pop("platform"))

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

        def _parse_meeting_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        meeting_url = _parse_meeting_url(d.pop("meeting_url", UNSET))

        import_meeting_recording = cls(
            source=source,
            recall_recording_id=recall_recording_id,
            platform=platform,
            started_at=started_at,
            ended_at=ended_at,
            meeting_url=meeting_url,
        )

        import_meeting_recording.additional_properties = d
        return import_meeting_recording

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
