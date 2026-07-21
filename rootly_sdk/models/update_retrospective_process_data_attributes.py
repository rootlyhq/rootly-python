from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_retrospective_process_data_attributes_retrospective_process_matching_criteria_type_0 import (
        UpdateRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteriaType0,
    )
    from ..models.update_retrospective_process_data_attributes_retrospective_process_matching_criteria_type_1 import (
        UpdateRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteriaType1,
    )
    from ..models.update_retrospective_process_data_attributes_retrospective_process_matching_criteria_type_2 import (
        UpdateRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteriaType2,
    )


T = TypeVar("T", bound="UpdateRetrospectiveProcessDataAttributes")


@_attrs_define
class UpdateRetrospectiveProcessDataAttributes:
    """
    Attributes:
        name (str | Unset): The name of the retrospective process
        description (None | str | Unset): The description of the retrospective process
        retrospective_process_matching_criteria (Unset |
            UpdateRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteriaType0 |
            UpdateRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteriaType1 |
            UpdateRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteriaType2):
    """

    name: str | Unset = UNSET
    description: None | str | Unset = UNSET
    retrospective_process_matching_criteria: (
        Unset
        | UpdateRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteriaType0
        | UpdateRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteriaType1
        | UpdateRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteriaType2
    ) = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_retrospective_process_data_attributes_retrospective_process_matching_criteria_type_0 import (
            UpdateRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteriaType0,
        )
        from ..models.update_retrospective_process_data_attributes_retrospective_process_matching_criteria_type_1 import (
            UpdateRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteriaType1,
        )

        name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        retrospective_process_matching_criteria: dict[str, Any] | Unset
        if isinstance(self.retrospective_process_matching_criteria, Unset):
            retrospective_process_matching_criteria = UNSET
        elif isinstance(
            self.retrospective_process_matching_criteria,
            UpdateRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteriaType0,
        ):
            retrospective_process_matching_criteria = self.retrospective_process_matching_criteria.to_dict()
        elif isinstance(
            self.retrospective_process_matching_criteria,
            UpdateRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteriaType1,
        ):
            retrospective_process_matching_criteria = self.retrospective_process_matching_criteria.to_dict()
        else:
            retrospective_process_matching_criteria = self.retrospective_process_matching_criteria.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if retrospective_process_matching_criteria is not UNSET:
            field_dict["retrospective_process_matching_criteria"] = retrospective_process_matching_criteria

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_retrospective_process_data_attributes_retrospective_process_matching_criteria_type_0 import (
            UpdateRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteriaType0,
        )
        from ..models.update_retrospective_process_data_attributes_retrospective_process_matching_criteria_type_1 import (
            UpdateRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteriaType1,
        )
        from ..models.update_retrospective_process_data_attributes_retrospective_process_matching_criteria_type_2 import (
            UpdateRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteriaType2,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_retrospective_process_matching_criteria(
            data: object,
        ) -> (
            Unset
            | UpdateRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteriaType0
            | UpdateRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteriaType1
            | UpdateRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteriaType2
        ):
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                retrospective_process_matching_criteria_type_0 = (
                    UpdateRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteriaType0.from_dict(data)
                )

                return retrospective_process_matching_criteria_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                retrospective_process_matching_criteria_type_1 = (
                    UpdateRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteriaType1.from_dict(data)
                )

                return retrospective_process_matching_criteria_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            retrospective_process_matching_criteria_type_2 = (
                UpdateRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteriaType2.from_dict(data)
            )

            return retrospective_process_matching_criteria_type_2

        retrospective_process_matching_criteria = _parse_retrospective_process_matching_criteria(
            d.pop("retrospective_process_matching_criteria", UNSET)
        )

        update_retrospective_process_data_attributes = cls(
            name=name,
            description=description,
            retrospective_process_matching_criteria=retrospective_process_matching_criteria,
        )

        return update_retrospective_process_data_attributes
