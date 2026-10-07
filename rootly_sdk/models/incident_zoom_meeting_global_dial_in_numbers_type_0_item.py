from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentZoomMeetingGlobalDialInNumbersType0Item")


@_attrs_define
class IncidentZoomMeetingGlobalDialInNumbersType0Item:
    """
    Attributes:
        country (str | Unset):
        country_name (str | Unset):
        city (str | Unset):
        number (str | Unset):
        type_ (str | Unset):
    """

    country: str | Unset = UNSET
    country_name: str | Unset = UNSET
    city: str | Unset = UNSET
    number: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        country = self.country

        country_name = self.country_name

        city = self.city

        number = self.number

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if country is not UNSET:
            field_dict["country"] = country
        if country_name is not UNSET:
            field_dict["country_name"] = country_name
        if city is not UNSET:
            field_dict["city"] = city
        if number is not UNSET:
            field_dict["number"] = number
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        country = d.pop("country", UNSET)

        country_name = d.pop("country_name", UNSET)

        city = d.pop("city", UNSET)

        number = d.pop("number", UNSET)

        type_ = d.pop("type", UNSET)

        incident_zoom_meeting_global_dial_in_numbers_type_0_item = cls(
            country=country,
            country_name=country_name,
            city=city,
            number=number,
            type_=type_,
        )

        incident_zoom_meeting_global_dial_in_numbers_type_0_item.additional_properties = d
        return incident_zoom_meeting_global_dial_in_numbers_type_0_item

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
