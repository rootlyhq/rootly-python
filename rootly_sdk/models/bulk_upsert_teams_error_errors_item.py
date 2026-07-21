from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BulkUpsertTeamsErrorErrorsItem")


@_attrs_define
class BulkUpsertTeamsErrorErrorsItem:
    """
    Attributes:
        index (int): Position of the failed record in the batch
        external_id (str):
        errors (list[str]):
    """

    index: int
    external_id: str
    errors: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        index = self.index

        external_id = self.external_id

        errors = self.errors

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "index": index,
                "external_id": external_id,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        index = d.pop("index")

        external_id = d.pop("external_id")

        errors = cast(list[str], d.pop("errors"))

        bulk_upsert_teams_error_errors_item = cls(
            index=index,
            external_id=external_id,
            errors=errors,
        )

        bulk_upsert_teams_error_errors_item.additional_properties = d
        return bulk_upsert_teams_error_errors_item

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
