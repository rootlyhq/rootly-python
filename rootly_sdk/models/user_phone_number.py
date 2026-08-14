import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserPhoneNumber")


@_attrs_define
class UserPhoneNumber:
    """
    Attributes:
        user_id (Union[Unset, int]):
        phone (Union[Unset, str]): Phone number in international format
        primary (Union[Unset, bool]): Whether this is the primary phone number
        verified_at (Union[None, Unset, datetime.datetime]): Date when phone number was verified
        verification_attempts_today (Union[Unset, int]): Number of verification attempts made today
        created_at (Union[Unset, str]): Date of creation
        updated_at (Union[Unset, str]): Date of last update
    """

    user_id: Unset | int = UNSET
    phone: Unset | str = UNSET
    primary: Unset | bool = UNSET
    verified_at: None | Unset | datetime.datetime = UNSET
    verification_attempts_today: Unset | int = UNSET
    created_at: Unset | str = UNSET
    updated_at: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        phone = self.phone

        primary = self.primary

        verified_at: None | Unset | str
        if isinstance(self.verified_at, Unset):
            verified_at = UNSET
        elif isinstance(self.verified_at, datetime.datetime):
            verified_at = self.verified_at.isoformat()
        else:
            verified_at = self.verified_at

        verification_attempts_today = self.verification_attempts_today

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if phone is not UNSET:
            field_dict["phone"] = phone
        if primary is not UNSET:
            field_dict["primary"] = primary
        if verified_at is not UNSET:
            field_dict["verified_at"] = verified_at
        if verification_attempts_today is not UNSET:
            field_dict["verification_attempts_today"] = verification_attempts_today
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("user_id", UNSET)

        phone = d.pop("phone", UNSET)

        primary = d.pop("primary", UNSET)

        def _parse_verified_at(data: object) -> None | Unset | datetime.datetime:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                verified_at_type_0 = isoparse(data)

                return verified_at_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | datetime.datetime, data)

        verified_at = _parse_verified_at(d.pop("verified_at", UNSET))

        verification_attempts_today = d.pop("verification_attempts_today", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        user_phone_number = cls(
            user_id=user_id,
            phone=phone,
            primary=primary,
            verified_at=verified_at,
            verification_attempts_today=verification_attempts_today,
            created_at=created_at,
            updated_at=updated_at,
        )

        user_phone_number.additional_properties = d
        return user_phone_number

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
