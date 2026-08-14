from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.verified_domain_source import VerifiedDomainSource, check_verified_domain_source
from ..models.verified_domain_verification_status import (
    VerifiedDomainVerificationStatus,
    check_verified_domain_verification_status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="VerifiedDomain")


@_attrs_define
class VerifiedDomain:
    """
    Attributes:
        domain (str): The domain name
        verification_status (VerifiedDomainVerificationStatus): Verification status
        verification_token (str): The verification token
        txt_host (str): The TXT record hostname to add
        txt_value (str): The TXT record value to add
        created_at (str): Date of creation
        updated_at (str): Date of last update
        verified_at (Union[None, Unset, str]): When the domain was first verified
        last_checked_at (Union[None, Unset, str]): When the domain was last checked
        last_check_passed_at (Union[None, Unset, str]): When the TXT record was last found
        check_failures_count (Union[Unset, int]): Number of consecutive check failures
        source (Union[Unset, VerifiedDomainSource]): How the domain was added
    """

    domain: str
    verification_status: VerifiedDomainVerificationStatus
    verification_token: str
    txt_host: str
    txt_value: str
    created_at: str
    updated_at: str
    verified_at: None | Unset | str = UNSET
    last_checked_at: None | Unset | str = UNSET
    last_check_passed_at: None | Unset | str = UNSET
    check_failures_count: Unset | int = UNSET
    source: Unset | VerifiedDomainSource = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain = self.domain

        verification_status: str = self.verification_status

        verification_token = self.verification_token

        txt_host = self.txt_host

        txt_value = self.txt_value

        created_at = self.created_at

        updated_at = self.updated_at

        verified_at: None | Unset | str
        if isinstance(self.verified_at, Unset):
            verified_at = UNSET
        else:
            verified_at = self.verified_at

        last_checked_at: None | Unset | str
        if isinstance(self.last_checked_at, Unset):
            last_checked_at = UNSET
        else:
            last_checked_at = self.last_checked_at

        last_check_passed_at: None | Unset | str
        if isinstance(self.last_check_passed_at, Unset):
            last_check_passed_at = UNSET
        else:
            last_check_passed_at = self.last_check_passed_at

        check_failures_count = self.check_failures_count

        source: Unset | str = UNSET
        if not isinstance(self.source, Unset):
            source = self.source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domain": domain,
                "verification_status": verification_status,
                "verification_token": verification_token,
                "txt_host": txt_host,
                "txt_value": txt_value,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if verified_at is not UNSET:
            field_dict["verified_at"] = verified_at
        if last_checked_at is not UNSET:
            field_dict["last_checked_at"] = last_checked_at
        if last_check_passed_at is not UNSET:
            field_dict["last_check_passed_at"] = last_check_passed_at
        if check_failures_count is not UNSET:
            field_dict["check_failures_count"] = check_failures_count
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        domain = d.pop("domain")

        verification_status = check_verified_domain_verification_status(d.pop("verification_status"))

        verification_token = d.pop("verification_token")

        txt_host = d.pop("txt_host")

        txt_value = d.pop("txt_value")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        def _parse_verified_at(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        verified_at = _parse_verified_at(d.pop("verified_at", UNSET))

        def _parse_last_checked_at(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        last_checked_at = _parse_last_checked_at(d.pop("last_checked_at", UNSET))

        def _parse_last_check_passed_at(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        last_check_passed_at = _parse_last_check_passed_at(d.pop("last_check_passed_at", UNSET))

        check_failures_count = d.pop("check_failures_count", UNSET)

        _source = d.pop("source", UNSET)
        source: Unset | VerifiedDomainSource
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = check_verified_domain_source(_source)

        verified_domain = cls(
            domain=domain,
            verification_status=verification_status,
            verification_token=verification_token,
            txt_host=txt_host,
            txt_value=txt_value,
            created_at=created_at,
            updated_at=updated_at,
            verified_at=verified_at,
            last_checked_at=last_checked_at,
            last_check_passed_at=last_check_passed_at,
            check_failures_count=check_failures_count,
            source=source,
        )

        verified_domain.additional_properties = d
        return verified_domain

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
