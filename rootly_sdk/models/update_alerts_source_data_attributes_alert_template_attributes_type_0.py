from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAlertsSourceDataAttributesAlertTemplateAttributesType0")


@_attrs_define
class UpdateAlertsSourceDataAttributesAlertTemplateAttributesType0:
    """
    Attributes:
        title (Union[None, Unset, str]): The alert title.
        description (Union[None, Unset, str]): The alert description.
        external_url (Union[None, Unset, str]): The alert URL.
    """

    title: None | Unset | str = UNSET
    description: None | Unset | str = UNSET
    external_url: None | Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title: None | Unset | str
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        external_url: None | Unset | str
        if isinstance(self.external_url, Unset):
            external_url = UNSET
        else:
            external_url = self.external_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if external_url is not UNSET:
            field_dict["external_url"] = external_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_title(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_external_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        external_url = _parse_external_url(d.pop("external_url", UNSET))

        update_alerts_source_data_attributes_alert_template_attributes_type_0 = cls(
            title=title,
            description=description,
            external_url=external_url,
        )

        update_alerts_source_data_attributes_alert_template_attributes_type_0.additional_properties = d
        return update_alerts_source_data_attributes_alert_template_attributes_type_0

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
