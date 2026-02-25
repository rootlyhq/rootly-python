from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="NewRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteriaType2")


@_attrs_define
class NewRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteriaType2:
    """
    Attributes:
        incident_type_ids (list[str]): Incident type IDs for retrospective process matching criteria
    """

    incident_type_ids: list[str]

    def to_dict(self) -> dict[str, Any]:
        incident_type_ids = self.incident_type_ids

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "incident_type_ids": incident_type_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        incident_type_ids = cast(list[str], d.pop("incident_type_ids"))

        new_retrospective_process_data_attributes_retrospective_process_matching_criteria_type_2 = cls(
            incident_type_ids=incident_type_ids,
        )

        return new_retrospective_process_data_attributes_retrospective_process_matching_criteria_type_2
