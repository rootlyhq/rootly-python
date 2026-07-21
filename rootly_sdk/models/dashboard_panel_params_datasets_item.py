from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dashboard_panel_params_datasets_item_collection import (
    DashboardPanelParamsDatasetsItemCollection,
    check_dashboard_panel_params_datasets_item_collection,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_panel_params_datasets_item_aggregate_type_0 import (
        DashboardPanelParamsDatasetsItemAggregateType0,
    )
    from ..models.dashboard_panel_params_datasets_item_filter_item import DashboardPanelParamsDatasetsItemFilterItem
    from ..models.dashboard_panel_params_datasets_item_group_by_type_1_type_0 import (
        DashboardPanelParamsDatasetsItemGroupByType1Type0,
    )


T = TypeVar("T", bound="DashboardPanelParamsDatasetsItem")


@_attrs_define
class DashboardPanelParamsDatasetsItem:
    """
    Attributes:
        name (None | str | Unset):
        collection (DashboardPanelParamsDatasetsItemCollection | Unset):
        filter_ (list[DashboardPanelParamsDatasetsItemFilterItem] | Unset):
        group_by (DashboardPanelParamsDatasetsItemGroupByType1Type0 | None | str | Unset):
        aggregate (DashboardPanelParamsDatasetsItemAggregateType0 | None | Unset):
    """

    name: None | str | Unset = UNSET
    collection: DashboardPanelParamsDatasetsItemCollection | Unset = UNSET
    filter_: list[DashboardPanelParamsDatasetsItemFilterItem] | Unset = UNSET
    group_by: DashboardPanelParamsDatasetsItemGroupByType1Type0 | None | str | Unset = UNSET
    aggregate: DashboardPanelParamsDatasetsItemAggregateType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.dashboard_panel_params_datasets_item_aggregate_type_0 import (
            DashboardPanelParamsDatasetsItemAggregateType0,
        )
        from ..models.dashboard_panel_params_datasets_item_group_by_type_1_type_0 import (
            DashboardPanelParamsDatasetsItemGroupByType1Type0,
        )

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        collection: str | Unset = UNSET
        if not isinstance(self.collection, Unset):
            collection = self.collection

        filter_: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = []
            for filter_item_data in self.filter_:
                filter_item = filter_item_data.to_dict()
                filter_.append(filter_item)

        group_by: dict[str, Any] | None | str | Unset
        if isinstance(self.group_by, Unset):
            group_by = UNSET
        elif isinstance(self.group_by, DashboardPanelParamsDatasetsItemGroupByType1Type0):
            group_by = self.group_by.to_dict()
        else:
            group_by = self.group_by

        aggregate: dict[str, Any] | None | Unset
        if isinstance(self.aggregate, Unset):
            aggregate = UNSET
        elif isinstance(self.aggregate, DashboardPanelParamsDatasetsItemAggregateType0):
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
        from ..models.dashboard_panel_params_datasets_item_aggregate_type_0 import (
            DashboardPanelParamsDatasetsItemAggregateType0,
        )
        from ..models.dashboard_panel_params_datasets_item_filter_item import DashboardPanelParamsDatasetsItemFilterItem
        from ..models.dashboard_panel_params_datasets_item_group_by_type_1_type_0 import (
            DashboardPanelParamsDatasetsItemGroupByType1Type0,
        )

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        _collection = d.pop("collection", UNSET)
        collection: DashboardPanelParamsDatasetsItemCollection | Unset
        if isinstance(_collection, Unset):
            collection = UNSET
        else:
            collection = check_dashboard_panel_params_datasets_item_collection(_collection)

        _filter_ = d.pop("filter", UNSET)
        filter_: list[DashboardPanelParamsDatasetsItemFilterItem] | Unset = UNSET
        if _filter_ is not UNSET:
            filter_ = []
            for filter_item_data in _filter_:
                filter_item = DashboardPanelParamsDatasetsItemFilterItem.from_dict(filter_item_data)

                filter_.append(filter_item)

        def _parse_group_by(data: object) -> DashboardPanelParamsDatasetsItemGroupByType1Type0 | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                group_by_type_1_type_0 = DashboardPanelParamsDatasetsItemGroupByType1Type0.from_dict(data)

                return group_by_type_1_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardPanelParamsDatasetsItemGroupByType1Type0 | None | str | Unset, data)

        group_by = _parse_group_by(d.pop("group_by", UNSET))

        def _parse_aggregate(data: object) -> DashboardPanelParamsDatasetsItemAggregateType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                aggregate_type_0 = DashboardPanelParamsDatasetsItemAggregateType0.from_dict(data)

                return aggregate_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardPanelParamsDatasetsItemAggregateType0 | None | Unset, data)

        aggregate = _parse_aggregate(d.pop("aggregate", UNSET))

        dashboard_panel_params_datasets_item = cls(
            name=name,
            collection=collection,
            filter_=filter_,
            group_by=group_by,
            aggregate=aggregate,
        )

        dashboard_panel_params_datasets_item.additional_properties = d
        return dashboard_panel_params_datasets_item

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
