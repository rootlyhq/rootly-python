from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_retrospective_process_data_attributes_retrospective_process_matching_criteria_type_0 import (
        NewRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteriaType0,
    )
    from ..models.new_retrospective_process_data_attributes_retrospective_process_matching_criteria_type_1 import (
        NewRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteriaType1,
    )
    from ..models.new_retrospective_process_data_attributes_retrospective_process_matching_criteria_type_2 import (
        NewRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteriaType2,
    )


T = TypeVar("T", bound="NewRetrospectiveProcessDataAttributes")


@_attrs_define
class NewRetrospectiveProcessDataAttributes:
    """
    Attributes:
        name (str): The name of the retrospective process
        copy_from (str): Retrospective process ID from which retrospective steps have to be copied. To use starter
            template for retrospective steps provide value: 'starter_template'
        description (Union[None, Unset, str]): The description of the retrospective process
        retrospective_process_matching_criteria
            (Union['NewRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteriaType0',
            'NewRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteriaType1',
            'NewRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteriaType2', Unset]):
    """

    name: str
    copy_from: str
    description: None | Unset | str = UNSET
    retrospective_process_matching_criteria: Union[
        "NewRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteriaType0",
        "NewRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteriaType1",
        "NewRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteriaType2",
        Unset,
    ] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.new_retrospective_process_data_attributes_retrospective_process_matching_criteria_type_0 import (
            NewRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteriaType0,
        )
        from ..models.new_retrospective_process_data_attributes_retrospective_process_matching_criteria_type_1 import (
            NewRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteriaType1,
        )

        name = self.name

        copy_from = self.copy_from

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        retrospective_process_matching_criteria: Unset | dict[str, Any]
        if isinstance(self.retrospective_process_matching_criteria, Unset):
            retrospective_process_matching_criteria = UNSET
        elif isinstance(
            self.retrospective_process_matching_criteria,
            NewRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteriaType0,
        ):
            retrospective_process_matching_criteria = self.retrospective_process_matching_criteria.to_dict()
        elif isinstance(
            self.retrospective_process_matching_criteria,
            NewRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteriaType1,
        ):
            retrospective_process_matching_criteria = self.retrospective_process_matching_criteria.to_dict()
        else:
            retrospective_process_matching_criteria = self.retrospective_process_matching_criteria.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "copy_from": copy_from,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if retrospective_process_matching_criteria is not UNSET:
            field_dict["retrospective_process_matching_criteria"] = retrospective_process_matching_criteria

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_retrospective_process_data_attributes_retrospective_process_matching_criteria_type_0 import (
            NewRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteriaType0,
        )
        from ..models.new_retrospective_process_data_attributes_retrospective_process_matching_criteria_type_1 import (
            NewRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteriaType1,
        )
        from ..models.new_retrospective_process_data_attributes_retrospective_process_matching_criteria_type_2 import (
            NewRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteriaType2,
        )

        d = dict(src_dict)
        name = d.pop("name")

        copy_from = d.pop("copy_from")

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_retrospective_process_matching_criteria(
            data: object,
        ) -> Union[
            "NewRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteriaType0",
            "NewRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteriaType1",
            "NewRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteriaType2",
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                retrospective_process_matching_criteria_type_0 = (
                    NewRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteriaType0.from_dict(data)
                )

                return retrospective_process_matching_criteria_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                retrospective_process_matching_criteria_type_1 = (
                    NewRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteriaType1.from_dict(data)
                )

                return retrospective_process_matching_criteria_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            retrospective_process_matching_criteria_type_2 = (
                NewRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteriaType2.from_dict(data)
            )

            return retrospective_process_matching_criteria_type_2

        retrospective_process_matching_criteria = _parse_retrospective_process_matching_criteria(
            d.pop("retrospective_process_matching_criteria", UNSET)
        )

        new_retrospective_process_data_attributes = cls(
            name=name,
            copy_from=copy_from,
            description=description,
            retrospective_process_matching_criteria=retrospective_process_matching_criteria,
        )

        return new_retrospective_process_data_attributes
