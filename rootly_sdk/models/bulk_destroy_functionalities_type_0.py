from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="BulkDestroyFunctionalitiesType0")


@_attrs_define
class BulkDestroyFunctionalitiesType0:
    """
    Attributes:
        external_ids (list[str]): Array of external_ids to delete. Max 100 per request.
    """

    external_ids: list[str]

    def to_dict(self) -> dict[str, Any]:
        external_ids = self.external_ids

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "external_ids": external_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        external_ids = cast(list[str], d.pop("external_ids"))

        bulk_destroy_functionalities_type_0 = cls(
            external_ids=external_ids,
        )

        return bulk_destroy_functionalities_type_0
