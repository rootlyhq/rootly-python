from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="NewRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteriaType0")


@_attrs_define
class NewRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteriaType0:
    """
    Attributes:
        severity_ids (list[str]): Severity IDs for retrospective process matching criteria
    """

    severity_ids: list[str]

    def to_dict(self) -> dict[str, Any]:
        severity_ids = self.severity_ids

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "severity_ids": severity_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        severity_ids = cast(list[str], d.pop("severity_ids"))

        new_retrospective_process_data_attributes_retrospective_process_matching_criteria_type_0 = cls(
            severity_ids=severity_ids,
        )

        return new_retrospective_process_data_attributes_retrospective_process_matching_criteria_type_0
