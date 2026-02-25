from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.environment import Environment
    from ..models.pulse_data_type_0 import PulseDataType0
    from ..models.pulse_labels_item_type_0 import PulseLabelsItemType0
    from ..models.pulse_refs_item_type_0 import PulseRefsItemType0
    from ..models.service import Service


T = TypeVar("T", bound="Pulse")


@_attrs_define
class Pulse:
    """
    Attributes:
        summary (str): The summary of the pulse
        created_at (str): Date of creation
        updated_at (str): Date of last update
        source (Union[None, Unset, str]): The source of the pulse (eg: k8s)
        services (Union[Unset, list['Service']]): Services attached to the pulse
        environments (Union[Unset, list['Environment']]): Environments attached to the pulse
        external_url (Union[None, Unset, str]): The external url of the pulse
        labels (Union[Unset, list[Union['PulseLabelsItemType0', None]]]):
        refs (Union[Unset, list[Union['PulseRefsItemType0', None]]]):
        data (Union['PulseDataType0', None, Unset]): Additional data
    """

    summary: str
    created_at: str
    updated_at: str
    source: None | Unset | str = UNSET
    services: Unset | list["Service"] = UNSET
    environments: Unset | list["Environment"] = UNSET
    external_url: None | Unset | str = UNSET
    labels: Unset | list[Union["PulseLabelsItemType0", None]] = UNSET
    refs: Unset | list[Union["PulseRefsItemType0", None]] = UNSET
    data: Union["PulseDataType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.pulse_data_type_0 import PulseDataType0
        from ..models.pulse_labels_item_type_0 import PulseLabelsItemType0
        from ..models.pulse_refs_item_type_0 import PulseRefsItemType0

        summary = self.summary

        created_at = self.created_at

        updated_at = self.updated_at

        source: None | Unset | str
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        services: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.services, Unset):
            services = []
            for services_item_data in self.services:
                services_item = services_item_data.to_dict()
                services.append(services_item)

        environments: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.environments, Unset):
            environments = []
            for environments_item_data in self.environments:
                environments_item = environments_item_data.to_dict()
                environments.append(environments_item)

        external_url: None | Unset | str
        if isinstance(self.external_url, Unset):
            external_url = UNSET
        else:
            external_url = self.external_url

        labels: Unset | list[None | dict[str, Any]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item: None | dict[str, Any]
                if isinstance(labels_item_data, PulseLabelsItemType0):
                    labels_item = labels_item_data.to_dict()
                else:
                    labels_item = labels_item_data
                labels.append(labels_item)

        refs: Unset | list[None | dict[str, Any]] = UNSET
        if not isinstance(self.refs, Unset):
            refs = []
            for refs_item_data in self.refs:
                refs_item: None | dict[str, Any]
                if isinstance(refs_item_data, PulseRefsItemType0):
                    refs_item = refs_item_data.to_dict()
                else:
                    refs_item = refs_item_data
                refs.append(refs_item)

        data: None | Unset | dict[str, Any]
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, PulseDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "summary": summary,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if source is not UNSET:
            field_dict["source"] = source
        if services is not UNSET:
            field_dict["services"] = services
        if environments is not UNSET:
            field_dict["environments"] = environments
        if external_url is not UNSET:
            field_dict["external_url"] = external_url
        if labels is not UNSET:
            field_dict["labels"] = labels
        if refs is not UNSET:
            field_dict["refs"] = refs
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.environment import Environment
        from ..models.pulse_data_type_0 import PulseDataType0
        from ..models.pulse_labels_item_type_0 import PulseLabelsItemType0
        from ..models.pulse_refs_item_type_0 import PulseRefsItemType0
        from ..models.service import Service

        d = dict(src_dict)
        summary = d.pop("summary")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        def _parse_source(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        source = _parse_source(d.pop("source", UNSET))

        services = []
        _services = d.pop("services", UNSET)
        for services_item_data in _services or []:
            services_item = Service.from_dict(services_item_data)

            services.append(services_item)

        environments = []
        _environments = d.pop("environments", UNSET)
        for environments_item_data in _environments or []:
            environments_item = Environment.from_dict(environments_item_data)

            environments.append(environments_item)

        def _parse_external_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        external_url = _parse_external_url(d.pop("external_url", UNSET))

        labels = []
        _labels = d.pop("labels", UNSET)
        for labels_item_data in _labels or []:

            def _parse_labels_item(data: object) -> Union["PulseLabelsItemType0", None]:
                if data is None:
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    labels_item_type_0 = PulseLabelsItemType0.from_dict(data)

                    return labels_item_type_0
                except:  # noqa: E722
                    pass
                return cast(Union["PulseLabelsItemType0", None], data)

            labels_item = _parse_labels_item(labels_item_data)

            labels.append(labels_item)

        refs = []
        _refs = d.pop("refs", UNSET)
        for refs_item_data in _refs or []:

            def _parse_refs_item(data: object) -> Union["PulseRefsItemType0", None]:
                if data is None:
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    refs_item_type_0 = PulseRefsItemType0.from_dict(data)

                    return refs_item_type_0
                except:  # noqa: E722
                    pass
                return cast(Union["PulseRefsItemType0", None], data)

            refs_item = _parse_refs_item(refs_item_data)

            refs.append(refs_item)

        def _parse_data(data: object) -> Union["PulseDataType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = PulseDataType0.from_dict(data)

                return data_type_0
            except:  # noqa: E722
                pass
            return cast(Union["PulseDataType0", None, Unset], data)

        data = _parse_data(d.pop("data", UNSET))

        pulse = cls(
            summary=summary,
            created_at=created_at,
            updated_at=updated_at,
            source=source,
            services=services,
            environments=environments,
            external_url=external_url,
            labels=labels,
            refs=refs,
            data=data,
        )

        pulse.additional_properties = d
        return pulse

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
