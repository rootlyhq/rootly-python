from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alert_list_data_item_source import AlertListDataItemSource, check_alert_list_data_item_source
from ..models.alert_list_data_item_type import AlertListDataItemType, check_alert_list_data_item_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert import Alert


T = TypeVar("T", bound="AlertListDataItem")


@_attrs_define
class AlertListDataItem:
    """
    Attributes:
        id (str): Unique ID of the alert
        type_ (AlertListDataItemType):
        attributes (Alert):
        source (Union[Unset, AlertListDataItemSource]): The source of the alert
    """

    id: str
    type_: AlertListDataItemType
    attributes: "Alert"
    source: Unset | AlertListDataItemSource = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_: str = self.type_

        attributes = self.attributes.to_dict()

        source: Unset | str = UNSET
        if not isinstance(self.source, Unset):
            source = self.source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "attributes": attributes,
            }
        )
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alert import Alert

        d = dict(src_dict)
        id = d.pop("id")

        type_ = check_alert_list_data_item_type(d.pop("type"))

        attributes = Alert.from_dict(d.pop("attributes"))

        _source = d.pop("source", UNSET)
        source: Unset | AlertListDataItemSource
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = check_alert_list_data_item_source(_source)

        alert_list_data_item = cls(
            id=id,
            type_=type_,
            attributes=attributes,
            source=source,
        )

        alert_list_data_item.additional_properties = d
        return alert_list_data_item

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
