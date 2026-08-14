from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.jsonapi_included_resource import JsonapiIncludedResource
    from ..models.schedule_rotation_active_day_response_data import ScheduleRotationActiveDayResponseData


T = TypeVar("T", bound="ScheduleRotationActiveDayResponse")


@_attrs_define
class ScheduleRotationActiveDayResponse:
    """
    Attributes:
        data (Union[Unset, ScheduleRotationActiveDayResponseData]):
        included (Union[Unset, list['JsonapiIncludedResource']]):
    """

    data: Union[Unset, "ScheduleRotationActiveDayResponseData"] = UNSET
    included: Union[Unset, list["JsonapiIncludedResource"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        included: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.included, Unset):
            included = []
            for included_item_data in self.included:
                included_item = included_item_data.to_dict()
                included.append(included_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if included is not UNSET:
            field_dict["included"] = included

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.jsonapi_included_resource import JsonapiIncludedResource
        from ..models.schedule_rotation_active_day_response_data import ScheduleRotationActiveDayResponseData

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: Union[Unset, ScheduleRotationActiveDayResponseData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = ScheduleRotationActiveDayResponseData.from_dict(_data)

        included = []
        _included = d.pop("included", UNSET)
        for included_item_data in _included or []:
            included_item = JsonapiIncludedResource.from_dict(included_item_data)

            included.append(included_item)

        schedule_rotation_active_day_response = cls(
            data=data,
            included=included,
        )

        schedule_rotation_active_day_response.additional_properties = d
        return schedule_rotation_active_day_response

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
