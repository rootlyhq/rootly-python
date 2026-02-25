import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.alert_noise import AlertNoise, check_alert_noise
from ..models.alert_source import AlertSource, check_alert_source
from ..models.alert_status import AlertStatus, check_alert_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_alert_field_values_attributes_item_type_0 import AlertAlertFieldValuesAttributesItemType0
    from ..models.alert_data_type_0 import AlertDataType0
    from ..models.alert_labels_item_type_0 import AlertLabelsItemType0
    from ..models.environment import Environment
    from ..models.service import Service
    from ..models.team import Team


T = TypeVar("T", bound="Alert")


@_attrs_define
class Alert:
    """
    Attributes:
        short_id (str): Human-readable short identifier for the alert
        source (AlertSource): The source of the alert
        summary (str): The summary of the alert
        created_at (str): Date of creation
        updated_at (str): Date of last update
        noise (Union[Unset, AlertNoise]): Whether the alert is marked as noise
        status (Union[Unset, AlertStatus]): The status of the alert
        description (Union[None, Unset, str]): The description of the alert
        services (Union[Unset, list['Service']]): Services attached to the alert
        groups (Union[Unset, list['Team']]): Groups attached to the alert
        environments (Union[Unset, list['Environment']]): Environments attached to the alert
        service_ids (Union[None, Unset, list[str]]): The Service IDs to attach to the alert. If your organization has
            On-Call enabled and your notification target is a Service. This field will be automatically set for you.
        group_ids (Union[None, Unset, list[str]]): The Group IDs to attach to the alert. If your organization has On-
            Call enabled and your notification target is a Group. This field will be automatically set for you.
        environment_ids (Union[None, Unset, list[str]]): The Environment IDs to attach to the alert
        external_id (Union[None, Unset, str]): External ID
        external_url (Union[None, Unset, str]): External Url
        alert_urgency_id (Union[None, Unset, str]): The ID of the alert urgency
        group_leader_alert_id (Union[None, Unset, str]): The ID of the group leader alert
        is_group_leader_alert (Union[None, Unset, bool]): Whether the alert is a group leader alert
        labels (Union[Unset, list[Union['AlertLabelsItemType0', None]]]):
        data (Union['AlertDataType0', None, Unset]): Additional data
        deduplication_key (Union[None, Unset, str]): Alerts sharing the same deduplication key are treated as a single
            alert.
        alert_field_values_attributes (Union[Unset, list[Union['AlertAlertFieldValuesAttributesItemType0', None]]]):
            Custom alert field values to create with the alert
        started_at (Union[None, Unset, datetime.datetime]): When the alert started
        ended_at (Union[None, Unset, datetime.datetime]): When the alert ended
    """

    short_id: str
    source: AlertSource
    summary: str
    created_at: str
    updated_at: str
    noise: Unset | AlertNoise = UNSET
    status: Unset | AlertStatus = UNSET
    description: None | Unset | str = UNSET
    services: Unset | list["Service"] = UNSET
    groups: Unset | list["Team"] = UNSET
    environments: Unset | list["Environment"] = UNSET
    service_ids: None | Unset | list[str] = UNSET
    group_ids: None | Unset | list[str] = UNSET
    environment_ids: None | Unset | list[str] = UNSET
    external_id: None | Unset | str = UNSET
    external_url: None | Unset | str = UNSET
    alert_urgency_id: None | Unset | str = UNSET
    group_leader_alert_id: None | Unset | str = UNSET
    is_group_leader_alert: None | Unset | bool = UNSET
    labels: Unset | list[Union["AlertLabelsItemType0", None]] = UNSET
    data: Union["AlertDataType0", None, Unset] = UNSET
    deduplication_key: None | Unset | str = UNSET
    alert_field_values_attributes: Unset | list[Union["AlertAlertFieldValuesAttributesItemType0", None]] = UNSET
    started_at: None | Unset | datetime.datetime = UNSET
    ended_at: None | Unset | datetime.datetime = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.alert_alert_field_values_attributes_item_type_0 import AlertAlertFieldValuesAttributesItemType0
        from ..models.alert_data_type_0 import AlertDataType0
        from ..models.alert_labels_item_type_0 import AlertLabelsItemType0

        short_id = self.short_id

        source: str = self.source

        summary = self.summary

        created_at = self.created_at

        updated_at = self.updated_at

        noise: Unset | str = UNSET
        if not isinstance(self.noise, Unset):
            noise = self.noise

        status: Unset | str = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        services: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.services, Unset):
            services = []
            for services_item_data in self.services:
                services_item = services_item_data.to_dict()
                services.append(services_item)

        groups: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        environments: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.environments, Unset):
            environments = []
            for environments_item_data in self.environments:
                environments_item = environments_item_data.to_dict()
                environments.append(environments_item)

        service_ids: None | Unset | list[str]
        if isinstance(self.service_ids, Unset):
            service_ids = UNSET
        elif isinstance(self.service_ids, list):
            service_ids = self.service_ids

        else:
            service_ids = self.service_ids

        group_ids: None | Unset | list[str]
        if isinstance(self.group_ids, Unset):
            group_ids = UNSET
        elif isinstance(self.group_ids, list):
            group_ids = self.group_ids

        else:
            group_ids = self.group_ids

        environment_ids: None | Unset | list[str]
        if isinstance(self.environment_ids, Unset):
            environment_ids = UNSET
        elif isinstance(self.environment_ids, list):
            environment_ids = self.environment_ids

        else:
            environment_ids = self.environment_ids

        external_id: None | Unset | str
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        external_url: None | Unset | str
        if isinstance(self.external_url, Unset):
            external_url = UNSET
        else:
            external_url = self.external_url

        alert_urgency_id: None | Unset | str
        if isinstance(self.alert_urgency_id, Unset):
            alert_urgency_id = UNSET
        else:
            alert_urgency_id = self.alert_urgency_id

        group_leader_alert_id: None | Unset | str
        if isinstance(self.group_leader_alert_id, Unset):
            group_leader_alert_id = UNSET
        else:
            group_leader_alert_id = self.group_leader_alert_id

        is_group_leader_alert: None | Unset | bool
        if isinstance(self.is_group_leader_alert, Unset):
            is_group_leader_alert = UNSET
        else:
            is_group_leader_alert = self.is_group_leader_alert

        labels: Unset | list[None | dict[str, Any]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item: None | dict[str, Any]
                if isinstance(labels_item_data, AlertLabelsItemType0):
                    labels_item = labels_item_data.to_dict()
                else:
                    labels_item = labels_item_data
                labels.append(labels_item)

        data: None | Unset | dict[str, Any]
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, AlertDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        deduplication_key: None | Unset | str
        if isinstance(self.deduplication_key, Unset):
            deduplication_key = UNSET
        else:
            deduplication_key = self.deduplication_key

        alert_field_values_attributes: Unset | list[None | dict[str, Any]] = UNSET
        if not isinstance(self.alert_field_values_attributes, Unset):
            alert_field_values_attributes = []
            for alert_field_values_attributes_item_data in self.alert_field_values_attributes:
                alert_field_values_attributes_item: None | dict[str, Any]
                if isinstance(alert_field_values_attributes_item_data, AlertAlertFieldValuesAttributesItemType0):
                    alert_field_values_attributes_item = alert_field_values_attributes_item_data.to_dict()
                else:
                    alert_field_values_attributes_item = alert_field_values_attributes_item_data
                alert_field_values_attributes.append(alert_field_values_attributes_item)

        started_at: None | Unset | str
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        elif isinstance(self.started_at, datetime.datetime):
            started_at = self.started_at.isoformat()
        else:
            started_at = self.started_at

        ended_at: None | Unset | str
        if isinstance(self.ended_at, Unset):
            ended_at = UNSET
        elif isinstance(self.ended_at, datetime.datetime):
            ended_at = self.ended_at.isoformat()
        else:
            ended_at = self.ended_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "short_id": short_id,
                "source": source,
                "summary": summary,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if noise is not UNSET:
            field_dict["noise"] = noise
        if status is not UNSET:
            field_dict["status"] = status
        if description is not UNSET:
            field_dict["description"] = description
        if services is not UNSET:
            field_dict["services"] = services
        if groups is not UNSET:
            field_dict["groups"] = groups
        if environments is not UNSET:
            field_dict["environments"] = environments
        if service_ids is not UNSET:
            field_dict["service_ids"] = service_ids
        if group_ids is not UNSET:
            field_dict["group_ids"] = group_ids
        if environment_ids is not UNSET:
            field_dict["environment_ids"] = environment_ids
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if external_url is not UNSET:
            field_dict["external_url"] = external_url
        if alert_urgency_id is not UNSET:
            field_dict["alert_urgency_id"] = alert_urgency_id
        if group_leader_alert_id is not UNSET:
            field_dict["group_leader_alert_id"] = group_leader_alert_id
        if is_group_leader_alert is not UNSET:
            field_dict["is_group_leader_alert"] = is_group_leader_alert
        if labels is not UNSET:
            field_dict["labels"] = labels
        if data is not UNSET:
            field_dict["data"] = data
        if deduplication_key is not UNSET:
            field_dict["deduplication_key"] = deduplication_key
        if alert_field_values_attributes is not UNSET:
            field_dict["alert_field_values_attributes"] = alert_field_values_attributes
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if ended_at is not UNSET:
            field_dict["ended_at"] = ended_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alert_alert_field_values_attributes_item_type_0 import AlertAlertFieldValuesAttributesItemType0
        from ..models.alert_data_type_0 import AlertDataType0
        from ..models.alert_labels_item_type_0 import AlertLabelsItemType0
        from ..models.environment import Environment
        from ..models.service import Service
        from ..models.team import Team

        d = dict(src_dict)
        short_id = d.pop("short_id")

        source = check_alert_source(d.pop("source"))

        summary = d.pop("summary")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        _noise = d.pop("noise", UNSET)
        noise: Unset | AlertNoise
        if isinstance(_noise, Unset):
            noise = UNSET
        else:
            noise = check_alert_noise(_noise)

        _status = d.pop("status", UNSET)
        status: Unset | AlertStatus
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_alert_status(_status)

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        description = _parse_description(d.pop("description", UNSET))

        services = []
        _services = d.pop("services", UNSET)
        for services_item_data in _services or []:
            services_item = Service.from_dict(services_item_data)

            services.append(services_item)

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = Team.from_dict(groups_item_data)

            groups.append(groups_item)

        environments = []
        _environments = d.pop("environments", UNSET)
        for environments_item_data in _environments or []:
            environments_item = Environment.from_dict(environments_item_data)

            environments.append(environments_item)

        def _parse_service_ids(data: object) -> None | Unset | list[str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                service_ids_type_0 = cast(list[str], data)

                return service_ids_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | list[str], data)

        service_ids = _parse_service_ids(d.pop("service_ids", UNSET))

        def _parse_group_ids(data: object) -> None | Unset | list[str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                group_ids_type_0 = cast(list[str], data)

                return group_ids_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | list[str], data)

        group_ids = _parse_group_ids(d.pop("group_ids", UNSET))

        def _parse_environment_ids(data: object) -> None | Unset | list[str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                environment_ids_type_0 = cast(list[str], data)

                return environment_ids_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | list[str], data)

        environment_ids = _parse_environment_ids(d.pop("environment_ids", UNSET))

        def _parse_external_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        external_id = _parse_external_id(d.pop("external_id", UNSET))

        def _parse_external_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        external_url = _parse_external_url(d.pop("external_url", UNSET))

        def _parse_alert_urgency_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        alert_urgency_id = _parse_alert_urgency_id(d.pop("alert_urgency_id", UNSET))

        def _parse_group_leader_alert_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        group_leader_alert_id = _parse_group_leader_alert_id(d.pop("group_leader_alert_id", UNSET))

        def _parse_is_group_leader_alert(data: object) -> None | Unset | bool:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | bool, data)

        is_group_leader_alert = _parse_is_group_leader_alert(d.pop("is_group_leader_alert", UNSET))

        labels = []
        _labels = d.pop("labels", UNSET)
        for labels_item_data in _labels or []:

            def _parse_labels_item(data: object) -> Union["AlertLabelsItemType0", None]:
                if data is None:
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    labels_item_type_0 = AlertLabelsItemType0.from_dict(data)

                    return labels_item_type_0
                except:  # noqa: E722
                    pass
                return cast(Union["AlertLabelsItemType0", None], data)

            labels_item = _parse_labels_item(labels_item_data)

            labels.append(labels_item)

        def _parse_data(data: object) -> Union["AlertDataType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = AlertDataType0.from_dict(data)

                return data_type_0
            except:  # noqa: E722
                pass
            return cast(Union["AlertDataType0", None, Unset], data)

        data = _parse_data(d.pop("data", UNSET))

        def _parse_deduplication_key(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        deduplication_key = _parse_deduplication_key(d.pop("deduplication_key", UNSET))

        alert_field_values_attributes = []
        _alert_field_values_attributes = d.pop("alert_field_values_attributes", UNSET)
        for alert_field_values_attributes_item_data in _alert_field_values_attributes or []:

            def _parse_alert_field_values_attributes_item(
                data: object,
            ) -> Union["AlertAlertFieldValuesAttributesItemType0", None]:
                if data is None:
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    alert_field_values_attributes_item_type_0 = AlertAlertFieldValuesAttributesItemType0.from_dict(data)

                    return alert_field_values_attributes_item_type_0
                except:  # noqa: E722
                    pass
                return cast(Union["AlertAlertFieldValuesAttributesItemType0", None], data)

            alert_field_values_attributes_item = _parse_alert_field_values_attributes_item(
                alert_field_values_attributes_item_data
            )

            alert_field_values_attributes.append(alert_field_values_attributes_item)

        def _parse_started_at(data: object) -> None | Unset | datetime.datetime:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                started_at_type_0 = isoparse(data)

                return started_at_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | datetime.datetime, data)

        started_at = _parse_started_at(d.pop("started_at", UNSET))

        def _parse_ended_at(data: object) -> None | Unset | datetime.datetime:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ended_at_type_0 = isoparse(data)

                return ended_at_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | datetime.datetime, data)

        ended_at = _parse_ended_at(d.pop("ended_at", UNSET))

        alert = cls(
            short_id=short_id,
            source=source,
            summary=summary,
            created_at=created_at,
            updated_at=updated_at,
            noise=noise,
            status=status,
            description=description,
            services=services,
            groups=groups,
            environments=environments,
            service_ids=service_ids,
            group_ids=group_ids,
            environment_ids=environment_ids,
            external_id=external_id,
            external_url=external_url,
            alert_urgency_id=alert_urgency_id,
            group_leader_alert_id=group_leader_alert_id,
            is_group_leader_alert=is_group_leader_alert,
            labels=labels,
            data=data,
            deduplication_key=deduplication_key,
            alert_field_values_attributes=alert_field_values_attributes,
            started_at=started_at,
            ended_at=ended_at,
        )

        alert.additional_properties = d
        return alert

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
