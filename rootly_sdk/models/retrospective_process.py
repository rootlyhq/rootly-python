from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.retrospective_process_retrospective_process_matching_criteria_type_0 import (
        RetrospectiveProcessRetrospectiveProcessMatchingCriteriaType0,
    )
    from ..models.retrospective_process_retrospective_process_matching_criteria_type_1 import (
        RetrospectiveProcessRetrospectiveProcessMatchingCriteriaType1,
    )
    from ..models.retrospective_process_retrospective_process_matching_criteria_type_2 import (
        RetrospectiveProcessRetrospectiveProcessMatchingCriteriaType2,
    )


T = TypeVar("T", bound="RetrospectiveProcess")


@_attrs_define
class RetrospectiveProcess:
    """
    Attributes:
        name (Union[Unset, str]): The name of the retrospective process
        description (Union[None, Unset, str]): The description of the retrospective process
        is_default (Union[None, Unset, bool]): Indicates the default process that Rootly created. This will be used as a
            fallback if no processes match the incident's conditions. The default process cannot have conditions and cannot
            be changed.
        created_at (Union[Unset, str]): Date of creation
        updated_at (Union[Unset, str]): Date of last update
        retrospective_process_matching_criteria (Union['RetrospectiveProcessRetrospectiveProcessMatchingCriteriaType0',
            'RetrospectiveProcessRetrospectiveProcessMatchingCriteriaType1',
            'RetrospectiveProcessRetrospectiveProcessMatchingCriteriaType2', Unset]):
    """

    name: Unset | str = UNSET
    description: None | Unset | str = UNSET
    is_default: None | Unset | bool = UNSET
    created_at: Unset | str = UNSET
    updated_at: Unset | str = UNSET
    retrospective_process_matching_criteria: Union[
        "RetrospectiveProcessRetrospectiveProcessMatchingCriteriaType0",
        "RetrospectiveProcessRetrospectiveProcessMatchingCriteriaType1",
        "RetrospectiveProcessRetrospectiveProcessMatchingCriteriaType2",
        Unset,
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.retrospective_process_retrospective_process_matching_criteria_type_0 import (
            RetrospectiveProcessRetrospectiveProcessMatchingCriteriaType0,
        )
        from ..models.retrospective_process_retrospective_process_matching_criteria_type_1 import (
            RetrospectiveProcessRetrospectiveProcessMatchingCriteriaType1,
        )

        name = self.name

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        is_default: None | Unset | bool
        if isinstance(self.is_default, Unset):
            is_default = UNSET
        else:
            is_default = self.is_default

        created_at = self.created_at

        updated_at = self.updated_at

        retrospective_process_matching_criteria: Unset | dict[str, Any]
        if isinstance(self.retrospective_process_matching_criteria, Unset):
            retrospective_process_matching_criteria = UNSET
        elif isinstance(
            self.retrospective_process_matching_criteria, RetrospectiveProcessRetrospectiveProcessMatchingCriteriaType0
        ):
            retrospective_process_matching_criteria = self.retrospective_process_matching_criteria.to_dict()
        elif isinstance(
            self.retrospective_process_matching_criteria, RetrospectiveProcessRetrospectiveProcessMatchingCriteriaType1
        ):
            retrospective_process_matching_criteria = self.retrospective_process_matching_criteria.to_dict()
        else:
            retrospective_process_matching_criteria = self.retrospective_process_matching_criteria.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if is_default is not UNSET:
            field_dict["is_default"] = is_default
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if retrospective_process_matching_criteria is not UNSET:
            field_dict["retrospective_process_matching_criteria"] = retrospective_process_matching_criteria

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.retrospective_process_retrospective_process_matching_criteria_type_0 import (
            RetrospectiveProcessRetrospectiveProcessMatchingCriteriaType0,
        )
        from ..models.retrospective_process_retrospective_process_matching_criteria_type_1 import (
            RetrospectiveProcessRetrospectiveProcessMatchingCriteriaType1,
        )
        from ..models.retrospective_process_retrospective_process_matching_criteria_type_2 import (
            RetrospectiveProcessRetrospectiveProcessMatchingCriteriaType2,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_is_default(data: object) -> None | Unset | bool:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | bool, data)

        is_default = _parse_is_default(d.pop("is_default", UNSET))

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        def _parse_retrospective_process_matching_criteria(
            data: object,
        ) -> Union[
            "RetrospectiveProcessRetrospectiveProcessMatchingCriteriaType0",
            "RetrospectiveProcessRetrospectiveProcessMatchingCriteriaType1",
            "RetrospectiveProcessRetrospectiveProcessMatchingCriteriaType2",
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                retrospective_process_matching_criteria_type_0 = (
                    RetrospectiveProcessRetrospectiveProcessMatchingCriteriaType0.from_dict(data)
                )

                return retrospective_process_matching_criteria_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                retrospective_process_matching_criteria_type_1 = (
                    RetrospectiveProcessRetrospectiveProcessMatchingCriteriaType1.from_dict(data)
                )

                return retrospective_process_matching_criteria_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            retrospective_process_matching_criteria_type_2 = (
                RetrospectiveProcessRetrospectiveProcessMatchingCriteriaType2.from_dict(data)
            )

            return retrospective_process_matching_criteria_type_2

        retrospective_process_matching_criteria = _parse_retrospective_process_matching_criteria(
            d.pop("retrospective_process_matching_criteria", UNSET)
        )

        retrospective_process = cls(
            name=name,
            description=description,
            is_default=is_default,
            created_at=created_at,
            updated_at=updated_at,
            retrospective_process_matching_criteria=retrospective_process_matching_criteria,
        )

        retrospective_process.additional_properties = d
        return retrospective_process

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
