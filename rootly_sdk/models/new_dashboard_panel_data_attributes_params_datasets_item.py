from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.new_dashboard_panel_data_attributes_params_datasets_item_collection import (
    NewDashboardPanelDataAttributesParamsDatasetsItemCollection,
    check_new_dashboard_panel_data_attributes_params_datasets_item_collection,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_dashboard_panel_data_attributes_params_datasets_item_aggregate_type_0 import (
        NewDashboardPanelDataAttributesParamsDatasetsItemAggregateType0,
    )
    from ..models.new_dashboard_panel_data_attributes_params_datasets_item_filter_item import (
        NewDashboardPanelDataAttributesParamsDatasetsItemFilterItem,
    )
    from ..models.new_dashboard_panel_data_attributes_params_datasets_item_group_by_type_1_type_0 import (
        NewDashboardPanelDataAttributesParamsDatasetsItemGroupByType1Type0,
    )


T = TypeVar("T", bound="NewDashboardPanelDataAttributesParamsDatasetsItem")


@_attrs_define
class NewDashboardPanelDataAttributesParamsDatasetsItem:
    """
    Attributes:
        name (Union[None, Unset, str]):
        collection (Union[Unset, NewDashboardPanelDataAttributesParamsDatasetsItemCollection]):
        filter_ (Union[Unset, list['NewDashboardPanelDataAttributesParamsDatasetsItemFilterItem']]):
        group_by (Union['NewDashboardPanelDataAttributesParamsDatasetsItemGroupByType1Type0', None, Unset, str]):
        aggregate (Union['NewDashboardPanelDataAttributesParamsDatasetsItemAggregateType0', None, Unset]):
    """

    name: Union[None, Unset, str] = UNSET
    collection: Union[Unset, NewDashboardPanelDataAttributesParamsDatasetsItemCollection] = UNSET
    filter_: Union[Unset, list["NewDashboardPanelDataAttributesParamsDatasetsItemFilterItem"]] = UNSET
    group_by: Union["NewDashboardPanelDataAttributesParamsDatasetsItemGroupByType1Type0", None, Unset, str] = UNSET
    aggregate: Union["NewDashboardPanelDataAttributesParamsDatasetsItemAggregateType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.new_dashboard_panel_data_attributes_params_datasets_item_aggregate_type_0 import (
            NewDashboardPanelDataAttributesParamsDatasetsItemAggregateType0,
        )
        from ..models.new_dashboard_panel_data_attributes_params_datasets_item_group_by_type_1_type_0 import (
            NewDashboardPanelDataAttributesParamsDatasetsItemGroupByType1Type0,
        )

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        collection: Union[Unset, str] = UNSET
        if not isinstance(self.collection, Unset):
            collection = self.collection

        filter_: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = []
            for filter_item_data in self.filter_:
                filter_item = filter_item_data.to_dict()
                filter_.append(filter_item)

        group_by: Union[None, Unset, dict[str, Any], str]
        if isinstance(self.group_by, Unset):
            group_by = UNSET
        elif isinstance(self.group_by, NewDashboardPanelDataAttributesParamsDatasetsItemGroupByType1Type0):
            group_by = self.group_by.to_dict()
        else:
            group_by = self.group_by

        aggregate: Union[None, Unset, dict[str, Any]]
        if isinstance(self.aggregate, Unset):
            aggregate = UNSET
        elif isinstance(self.aggregate, NewDashboardPanelDataAttributesParamsDatasetsItemAggregateType0):
            aggregate = self.aggregate.to_dict()
        else:
            aggregate = self.aggregate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if collection is not UNSET:
            field_dict["collection"] = collection
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if group_by is not UNSET:
            field_dict["group_by"] = group_by
        if aggregate is not UNSET:
            field_dict["aggregate"] = aggregate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_dashboard_panel_data_attributes_params_datasets_item_aggregate_type_0 import (
            NewDashboardPanelDataAttributesParamsDatasetsItemAggregateType0,
        )
        from ..models.new_dashboard_panel_data_attributes_params_datasets_item_filter_item import (
            NewDashboardPanelDataAttributesParamsDatasetsItemFilterItem,
        )
        from ..models.new_dashboard_panel_data_attributes_params_datasets_item_group_by_type_1_type_0 import (
            NewDashboardPanelDataAttributesParamsDatasetsItemGroupByType1Type0,
        )

        d = dict(src_dict)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        _collection = d.pop("collection", UNSET)
        collection: Union[Unset, NewDashboardPanelDataAttributesParamsDatasetsItemCollection]
        if isinstance(_collection, Unset):
            collection = UNSET
        else:
            collection = check_new_dashboard_panel_data_attributes_params_datasets_item_collection(_collection)

        filter_ = []
        _filter_ = d.pop("filter", UNSET)
        for filter_item_data in _filter_ or []:
            filter_item = NewDashboardPanelDataAttributesParamsDatasetsItemFilterItem.from_dict(filter_item_data)

            filter_.append(filter_item)

        def _parse_group_by(
            data: object,
        ) -> Union["NewDashboardPanelDataAttributesParamsDatasetsItemGroupByType1Type0", None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                group_by_type_1_type_0 = NewDashboardPanelDataAttributesParamsDatasetsItemGroupByType1Type0.from_dict(
                    data
                )

                return group_by_type_1_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union["NewDashboardPanelDataAttributesParamsDatasetsItemGroupByType1Type0", None, Unset, str], data
            )

        group_by = _parse_group_by(d.pop("group_by", UNSET))

        def _parse_aggregate(
            data: object,
        ) -> Union["NewDashboardPanelDataAttributesParamsDatasetsItemAggregateType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                aggregate_type_0 = NewDashboardPanelDataAttributesParamsDatasetsItemAggregateType0.from_dict(data)

                return aggregate_type_0
            except:  # noqa: E722
                pass
            return cast(Union["NewDashboardPanelDataAttributesParamsDatasetsItemAggregateType0", None, Unset], data)

        aggregate = _parse_aggregate(d.pop("aggregate", UNSET))

        new_dashboard_panel_data_attributes_params_datasets_item = cls(
            name=name,
            collection=collection,
            filter_=filter_,
            group_by=group_by,
            aggregate=aggregate,
        )

        new_dashboard_panel_data_attributes_params_datasets_item.additional_properties = d
        return new_dashboard_panel_data_attributes_params_datasets_item

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
