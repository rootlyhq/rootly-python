from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.bulk_destroy_teams_type_1_managed_by import BulkDestroyTeamsType1ManagedBy
from ..models.bulk_destroy_teams_type_1_managed_by import check_bulk_destroy_teams_type_1_managed_by
from ..types import UNSET, Unset
from typing import cast


T = TypeVar("T", bound="BulkDestroyTeamsType1")


@_attrs_define
class BulkDestroyTeamsType1:
    """
    Attributes:
        managed_by (BulkDestroyTeamsType1ManagedBy): Delete all records with this managed_by value (web/admin_web not
            allowed).
        keep_external_ids (list[str] | Unset): Records with these external_ids are preserved.
    """

    managed_by: BulkDestroyTeamsType1ManagedBy
    keep_external_ids: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        managed_by: str = self.managed_by

        keep_external_ids: list[str] | Unset = UNSET
        if not isinstance(self.keep_external_ids, Unset):
            keep_external_ids = self.keep_external_ids

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "managed_by": managed_by,
            }
        )
        if keep_external_ids is not UNSET:
            field_dict["keep_external_ids"] = keep_external_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        managed_by = check_bulk_destroy_teams_type_1_managed_by(d.pop("managed_by"))

        keep_external_ids = cast(list[str], d.pop("keep_external_ids", UNSET))

        bulk_destroy_teams_type_1 = cls(
            managed_by=managed_by,
            keep_external_ids=keep_external_ids,
        )

        return bulk_destroy_teams_type_1
