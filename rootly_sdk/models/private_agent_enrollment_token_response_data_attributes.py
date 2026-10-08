from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="PrivateAgentEnrollmentTokenResponseDataAttributes")


@_attrs_define
class PrivateAgentEnrollmentTokenResponseDataAttributes:
    """
    Attributes:
        token (str): One-time secret. Returned only on creation; do not log or store in source control.
        expires_at (datetime.datetime):
    """

    token: str
    expires_at: datetime.datetime

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        expires_at = self.expires_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "token": token,
                "expires_at": expires_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        token = d.pop("token")

        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        private_agent_enrollment_token_response_data_attributes = cls(
            token=token,
            expires_at=expires_at,
        )

        return private_agent_enrollment_token_response_data_attributes
