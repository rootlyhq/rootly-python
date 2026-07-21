from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BulkDestroyEnvironmentsResponseData")


@_attrs_define
class BulkDestroyEnvironmentsResponseData:
    """
    Attributes:
        deleted_external_ids (list[str] | Unset): External IDs that were successfully deleted
        failed_external_ids (list[str] | Unset): External IDs whose deletion the record itself blocked (e.g. minimum-one
            guard, restrict associations). Records the caller is not authorized to destroy are NOT listed here.
        not_found_external_ids (list[str] | Unset): External IDs that were not found or not accessible to the caller
            (external_ids mode only)
    """

    deleted_external_ids: list[str] | Unset = UNSET
    failed_external_ids: list[str] | Unset = UNSET
    not_found_external_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deleted_external_ids: list[str] | Unset = UNSET
        if not isinstance(self.deleted_external_ids, Unset):
            deleted_external_ids = self.deleted_external_ids

        failed_external_ids: list[str] | Unset = UNSET
        if not isinstance(self.failed_external_ids, Unset):
            failed_external_ids = self.failed_external_ids

        not_found_external_ids: list[str] | Unset = UNSET
        if not isinstance(self.not_found_external_ids, Unset):
            not_found_external_ids = self.not_found_external_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deleted_external_ids is not UNSET:
            field_dict["deleted_external_ids"] = deleted_external_ids
        if failed_external_ids is not UNSET:
            field_dict["failed_external_ids"] = failed_external_ids
        if not_found_external_ids is not UNSET:
            field_dict["not_found_external_ids"] = not_found_external_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        deleted_external_ids = cast(list[str], d.pop("deleted_external_ids", UNSET))

        failed_external_ids = cast(list[str], d.pop("failed_external_ids", UNSET))

        not_found_external_ids = cast(list[str], d.pop("not_found_external_ids", UNSET))

        bulk_destroy_environments_response_data = cls(
            deleted_external_ids=deleted_external_ids,
            failed_external_ids=failed_external_ids,
            not_found_external_ids=not_found_external_ids,
        )

        bulk_destroy_environments_response_data.additional_properties = d
        return bulk_destroy_environments_response_data

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
