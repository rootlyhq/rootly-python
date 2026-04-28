from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

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
        noise (AlertNoise | Unset): Whether the alert is marked as noise
        status (AlertStatus | Unset): The status of the alert
        description (None | str | Unset): The description of the alert
        services (list[Service] | Unset): Services attached to the alert
        groups (list[Team] | Unset): Groups attached to the alert
        environments (list[Environment] | Unset): Environments attached to the alert
        service_ids (list[str] | None | Unset): The Service IDs to attach to the alert. If your organization has On-Call
            enabled and your notification target is a Service. This field will be automatically set for you.
        group_ids (list[str] | None | Unset): The Group IDs to attach to the alert. If your organization has On-Call
            enabled and your notification target is a Group. This field will be automatically set for you.
        environment_ids (list[str] | None | Unset): The Environment IDs to attach to the alert
        external_id (None | str | Unset): External ID
        external_url (None | str | Unset): External Url
        alert_urgency_id (None | str | Unset): The ID of the alert urgency
        group_leader_alert_id (None | str | Unset): The ID of the group leader alert
        is_group_leader_alert (bool | None | Unset): Whether the alert is a group leader alert
        labels (list[AlertLabelsItemType0 | None] | Unset):
        data (AlertDataType0 | None | Unset): Additional data
        deduplication_key (None | str | Unset): Alerts sharing the same deduplication key are treated as a single alert.
        alert_field_values_attributes (list[AlertAlertFieldValuesAttributesItemType0 | None] | Unset): Custom alert
            field values to create with the alert
        started_at (datetime.datetime | None | Unset): When the alert started
        ended_at (datetime.datetime | None | Unset): When the alert ended
    """

    short_id: str
    source: AlertSource
    summary: str
    created_at: str
    updated_at: str
    noise: AlertNoise | Unset = UNSET
    status: AlertStatus | Unset = UNSET
    description: None | str | Unset = UNSET
    services: list[Service] | Unset = UNSET
    groups: list[Team] | Unset = UNSET
    environments: list[Environment] | Unset = UNSET
    service_ids: list[str] | None | Unset = UNSET
    group_ids: list[str] | None | Unset = UNSET
    environment_ids: list[str] | None | Unset = UNSET
    external_id: None | str | Unset = UNSET
    external_url: None | str | Unset = UNSET
    alert_urgency_id: None | str | Unset = UNSET
    group_leader_alert_id: None | str | Unset = UNSET
    is_group_leader_alert: bool | None | Unset = UNSET
    labels: list[AlertLabelsItemType0 | None] | Unset = UNSET
    data: AlertDataType0 | None | Unset = UNSET
    deduplication_key: None | str | Unset = UNSET
    alert_field_values_attributes: list[AlertAlertFieldValuesAttributesItemType0 | None] | Unset = UNSET
    started_at: datetime.datetime | None | Unset = UNSET
    ended_at: datetime.datetime | None | Unset = UNSET
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

        noise: str | Unset = UNSET
        if not isinstance(self.noise, Unset):
            noise = self.noise

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        services: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.services, Unset):
            services = []
            for services_item_data in self.services:
                services_item = services_item_data.to_dict()
                services.append(services_item)

        groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        environments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.environments, Unset):
            environments = []
            for environments_item_data in self.environments:
                environments_item = environments_item_data.to_dict()
                environments.append(environments_item)

        service_ids: list[str] | None | Unset
        if isinstance(self.service_ids, Unset):
            service_ids = UNSET
        elif isinstance(self.service_ids, list):
            service_ids = self.service_ids

        else:
            service_ids = self.service_ids

        group_ids: list[str] | None | Unset
        if isinstance(self.group_ids, Unset):
            group_ids = UNSET
        elif isinstance(self.group_ids, list):
            group_ids = self.group_ids

        else:
            group_ids = self.group_ids

        environment_ids: list[str] | None | Unset
        if isinstance(self.environment_ids, Unset):
            environment_ids = UNSET
        elif isinstance(self.environment_ids, list):
            environment_ids = self.environment_ids

        else:
            environment_ids = self.environment_ids

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        external_url: None | str | Unset
        if isinstance(self.external_url, Unset):
            external_url = UNSET
        else:
            external_url = self.external_url

        alert_urgency_id: None | str | Unset
        if isinstance(self.alert_urgency_id, Unset):
            alert_urgency_id = UNSET
        else:
            alert_urgency_id = self.alert_urgency_id

        group_leader_alert_id: None | str | Unset
        if isinstance(self.group_leader_alert_id, Unset):
            group_leader_alert_id = UNSET
        else:
            group_leader_alert_id = self.group_leader_alert_id

        is_group_leader_alert: bool | None | Unset
        if isinstance(self.is_group_leader_alert, Unset):
            is_group_leader_alert = UNSET
        else:
            is_group_leader_alert = self.is_group_leader_alert

        labels: list[dict[str, Any] | None] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item: dict[str, Any] | None
                if isinstance(labels_item_data, AlertLabelsItemType0):
                    labels_item = labels_item_data.to_dict()
                else:
                    labels_item = labels_item_data
                labels.append(labels_item)

        data: dict[str, Any] | None | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, AlertDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        deduplication_key: None | str | Unset
        if isinstance(self.deduplication_key, Unset):
            deduplication_key = UNSET
        else:
            deduplication_key = self.deduplication_key

        alert_field_values_attributes: list[dict[str, Any] | None] | Unset = UNSET
        if not isinstance(self.alert_field_values_attributes, Unset):
            alert_field_values_attributes = []
            for alert_field_values_attributes_item_data in self.alert_field_values_attributes:
                alert_field_values_attributes_item: dict[str, Any] | None
                if isinstance(alert_field_values_attributes_item_data, AlertAlertFieldValuesAttributesItemType0):
                    alert_field_values_attributes_item = alert_field_values_attributes_item_data.to_dict()
                else:
                    alert_field_values_attributes_item = alert_field_values_attributes_item_data
                alert_field_values_attributes.append(alert_field_values_attributes_item)

        started_at: None | str | Unset
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        elif isinstance(self.started_at, datetime.datetime):
            started_at = self.started_at.isoformat()
        else:
            started_at = self.started_at

        ended_at: None | str | Unset
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
        noise: AlertNoise | Unset
        if isinstance(_noise, Unset):
            noise = UNSET
        else:
            noise = check_alert_noise(_noise)

        _status = d.pop("status", UNSET)
        status: AlertStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_alert_status(_status)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _services = d.pop("services", UNSET)
        services: list[Service] | Unset = UNSET
        if _services is not UNSET:
            services = []
            for services_item_data in _services:
                services_item = Service.from_dict(services_item_data)

                services.append(services_item)

        _groups = d.pop("groups", UNSET)
        groups: list[Team] | Unset = UNSET
        if _groups is not UNSET:
            groups = []
            for groups_item_data in _groups:
                groups_item = Team.from_dict(groups_item_data)

                groups.append(groups_item)

        _environments = d.pop("environments", UNSET)
        environments: list[Environment] | Unset = UNSET
        if _environments is not UNSET:
            environments = []
            for environments_item_data in _environments:
                environments_item = Environment.from_dict(environments_item_data)

                environments.append(environments_item)

        def _parse_service_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                service_ids_type_0 = cast(list[str], data)

                return service_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        service_ids = _parse_service_ids(d.pop("service_ids", UNSET))

        def _parse_group_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                group_ids_type_0 = cast(list[str], data)

                return group_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        group_ids = _parse_group_ids(d.pop("group_ids", UNSET))

        def _parse_environment_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                environment_ids_type_0 = cast(list[str], data)

                return environment_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        environment_ids = _parse_environment_ids(d.pop("environment_ids", UNSET))

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("external_id", UNSET))

        def _parse_external_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_url = _parse_external_url(d.pop("external_url", UNSET))

        def _parse_alert_urgency_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alert_urgency_id = _parse_alert_urgency_id(d.pop("alert_urgency_id", UNSET))

        def _parse_group_leader_alert_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group_leader_alert_id = _parse_group_leader_alert_id(d.pop("group_leader_alert_id", UNSET))

        def _parse_is_group_leader_alert(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_group_leader_alert = _parse_is_group_leader_alert(d.pop("is_group_leader_alert", UNSET))

        _labels = d.pop("labels", UNSET)
        labels: list[AlertLabelsItemType0 | None] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for labels_item_data in _labels:

                def _parse_labels_item(data: object) -> AlertLabelsItemType0 | None:
                    if data is None:
                        return data
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        labels_item_type_0 = AlertLabelsItemType0.from_dict(data)

                        return labels_item_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    return cast(AlertLabelsItemType0 | None, data)

                labels_item = _parse_labels_item(labels_item_data)

                labels.append(labels_item)

        def _parse_data(data: object) -> AlertDataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = AlertDataType0.from_dict(data)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AlertDataType0 | None | Unset, data)

        data = _parse_data(d.pop("data", UNSET))

        def _parse_deduplication_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deduplication_key = _parse_deduplication_key(d.pop("deduplication_key", UNSET))

        _alert_field_values_attributes = d.pop("alert_field_values_attributes", UNSET)
        alert_field_values_attributes: list[AlertAlertFieldValuesAttributesItemType0 | None] | Unset = UNSET
        if _alert_field_values_attributes is not UNSET:
            alert_field_values_attributes = []
            for alert_field_values_attributes_item_data in _alert_field_values_attributes:

                def _parse_alert_field_values_attributes_item(
                    data: object,
                ) -> AlertAlertFieldValuesAttributesItemType0 | None:
                    if data is None:
                        return data
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        alert_field_values_attributes_item_type_0 = AlertAlertFieldValuesAttributesItemType0.from_dict(
                            data
                        )

                        return alert_field_values_attributes_item_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    return cast(AlertAlertFieldValuesAttributesItemType0 | None, data)

                alert_field_values_attributes_item = _parse_alert_field_values_attributes_item(
                    alert_field_values_attributes_item_data
                )

                alert_field_values_attributes.append(alert_field_values_attributes_item)

        def _parse_started_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                started_at_type_0 = isoparse(data)

                return started_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        started_at = _parse_started_at(d.pop("started_at", UNSET))

        def _parse_ended_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ended_at_type_0 = isoparse(data)

                return ended_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

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
