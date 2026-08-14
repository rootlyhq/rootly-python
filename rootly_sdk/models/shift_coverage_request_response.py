from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.jsonapi_included_resource import JsonapiIncludedResource
    from ..models.shift_coverage_request_response_data import ShiftCoverageRequestResponseData


T = TypeVar("T", bound="ShiftCoverageRequestResponse")


@_attrs_define
class ShiftCoverageRequestResponse:
    """
    Attributes:
        data (ShiftCoverageRequestResponseData):
        included (Union[Unset, list['JsonapiIncludedResource']]):
    """

    data: "ShiftCoverageRequestResponseData"
    included: Unset | list["JsonapiIncludedResource"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        included: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.included, Unset):
            included = []
            for included_item_data in self.included:
                included_item = included_item_data.to_dict()
                included.append(included_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )
        if included is not UNSET:
            field_dict["included"] = included

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.jsonapi_included_resource import JsonapiIncludedResource
        from ..models.shift_coverage_request_response_data import ShiftCoverageRequestResponseData

        d = dict(src_dict)
        data = ShiftCoverageRequestResponseData.from_dict(d.pop("data"))

        included = []
        _included = d.pop("included", UNSET)
        for included_item_data in _included or []:
            included_item = JsonapiIncludedResource.from_dict(included_item_data)

            included.append(included_item)

        shift_coverage_request_response = cls(
            data=data,
            included=included,
        )

        shift_coverage_request_response.additional_properties = d
        return shift_coverage_request_response

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
