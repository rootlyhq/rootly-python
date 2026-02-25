from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="NewRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteriaType1")


@_attrs_define
class NewRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteriaType1:
    """
    Attributes:
        group_ids (list[str]): Team IDs for retrospective process matching criteria
    """

    group_ids: list[str]

    def to_dict(self) -> dict[str, Any]:
        group_ids = self.group_ids

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "group_ids": group_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        group_ids = cast(list[str], d.pop("group_ids"))

        new_retrospective_process_data_attributes_retrospective_process_matching_criteria_type_1 = cls(
            group_ids=group_ids,
        )

        return new_retrospective_process_data_attributes_retrospective_process_matching_criteria_type_1
