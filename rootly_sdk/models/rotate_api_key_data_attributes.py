import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="RotateApiKeyDataAttributes")


@_attrs_define
class RotateApiKeyDataAttributes:
    """
    Attributes:
        expires_at (Union[None, Unset, datetime.datetime]): The new expiration date after rotation (ISO 8601)
        grace_period_minutes (Union[Unset, int]): How many minutes to keep the old token valid. Only applies when the
            grace period feature is enabled for your organization. Defaults to 30. Default: 30.
    """

    expires_at: None | Unset | datetime.datetime = UNSET
    grace_period_minutes: Unset | int = 30

    def to_dict(self) -> dict[str, Any]:
        expires_at: None | Unset | str
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        grace_period_minutes = self.grace_period_minutes

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if grace_period_minutes is not UNSET:
            field_dict["grace_period_minutes"] = grace_period_minutes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_expires_at(data: object) -> None | Unset | datetime.datetime:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = isoparse(data)

                return expires_at_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | datetime.datetime, data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))

        grace_period_minutes = d.pop("grace_period_minutes", UNSET)

        rotate_api_key_data_attributes = cls(
            expires_at=expires_at,
            grace_period_minutes=grace_period_minutes,
        )

        return rotate_api_key_data_attributes
