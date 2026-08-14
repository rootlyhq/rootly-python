import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.import_meeting_recording_platform import (
    ImportMeetingRecordingPlatform,
    check_import_meeting_recording_platform,
)
from ..models.import_meeting_recording_source import ImportMeetingRecordingSource, check_import_meeting_recording_source
from ..types import UNSET, Unset

T = TypeVar("T", bound="ImportMeetingRecording")


@_attrs_define
class ImportMeetingRecording:
    """
    Attributes:
        source (ImportMeetingRecordingSource): Import source (currently only "recall_desktop_sdk")
        recall_recording_id (UUID): External recording UUID (required when source is recall_desktop_sdk)
        platform (ImportMeetingRecordingPlatform): Meeting platform
        started_at (Union[None, Unset, datetime.datetime]): When the recording started
        ended_at (Union[None, Unset, datetime.datetime]): When the recording ended
        meeting_url (Union[None, Unset, str]): Original meeting URL
    """

    source: ImportMeetingRecordingSource
    recall_recording_id: UUID
    platform: ImportMeetingRecordingPlatform
    started_at: None | Unset | datetime.datetime = UNSET
    ended_at: None | Unset | datetime.datetime = UNSET
    meeting_url: None | Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source: str = self.source

        recall_recording_id = str(self.recall_recording_id)

        platform: str = self.platform

        started_at: None | Unset | str
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        elif isinstance(self.started_at, datetime.datetime):
            started_at = self.started_at.isoformat()
        else:
            started_at = self.started_at

        ended_at: None | Unset | str
        if isinstance(self.ended_at, Unset):
            ended_at = UNSET
        elif isinstance(self.ended_at, datetime.datetime):
            ended_at = self.ended_at.isoformat()
        else:
            ended_at = self.ended_at

        meeting_url: None | Unset | str
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

        def _parse_started_at(data: object) -> None | Unset | datetime.datetime:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                started_at_type_0 = isoparse(data)

                return started_at_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | datetime.datetime, data)

        started_at = _parse_started_at(d.pop("started_at", UNSET))

        def _parse_ended_at(data: object) -> None | Unset | datetime.datetime:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ended_at_type_0 = isoparse(data)

                return ended_at_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | datetime.datetime, data)

        ended_at = _parse_ended_at(d.pop("ended_at", UNSET))

        def _parse_meeting_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

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
