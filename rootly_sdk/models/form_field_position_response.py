from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.form_field_position_response_data import FormFieldPositionResponseData
    from ..models.jsonapi_included_resource import JsonapiIncludedResource


T = TypeVar("T", bound="FormFieldPositionResponse")


@_attrs_define
class FormFieldPositionResponse:
    """
    Attributes:
        data (FormFieldPositionResponseData):
        included (Union[Unset, list['JsonapiIncludedResource']]):
    """

    data: "FormFieldPositionResponseData"
    included: Union[Unset, list["JsonapiIncludedResource"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        included: Union[Unset, list[dict[str, Any]]] = UNSET
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
        from ..models.form_field_position_response_data import FormFieldPositionResponseData
        from ..models.jsonapi_included_resource import JsonapiIncludedResource

        d = dict(src_dict)
        data = FormFieldPositionResponseData.from_dict(d.pop("data"))

        included = []
        _included = d.pop("included", UNSET)
        for included_item_data in _included or []:
            included_item = JsonapiIncludedResource.from_dict(included_item_data)

            included.append(included_item)

        form_field_position_response = cls(
            data=data,
            included=included,
        )

        form_field_position_response.additional_properties = d
        return form_field_position_response

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
