from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StartSessionResponseData")


@_attrs_define
class StartSessionResponseData:
    """
    Attributes:
        session_id (UUID): Meeting recording UUID
        stream_token (str): Token for the desktop client to stream audio
        meeting_recording_id (UUID): Meeting recording UUID
    """

    session_id: UUID
    stream_token: str
    meeting_recording_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        session_id = str(self.session_id)

        stream_token = self.stream_token

        meeting_recording_id = str(self.meeting_recording_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "session_id": session_id,
                "stream_token": stream_token,
                "meeting_recording_id": meeting_recording_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        session_id = UUID(d.pop("session_id"))

        stream_token = d.pop("stream_token")

        meeting_recording_id = UUID(d.pop("meeting_recording_id"))

        start_session_response_data = cls(
            session_id=session_id,
            stream_token=stream_token,
            meeting_recording_id=meeting_recording_id,
        )

        start_session_response_data.additional_properties = d
        return start_session_response_data

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
