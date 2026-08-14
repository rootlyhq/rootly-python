import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.new_alert_data_attributes_noise import NewAlertDataAttributesNoise, check_new_alert_data_attributes_noise
from ..models.new_alert_data_attributes_notification_target_type import (
    NewAlertDataAttributesNotificationTargetType,
    check_new_alert_data_attributes_notification_target_type,
)
from ..models.new_alert_data_attributes_status import (
    NewAlertDataAttributesStatus,
    check_new_alert_data_attributes_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_alert_data_attributes_alert_field_values_attributes_item_type_0 import (
        NewAlertDataAttributesAlertFieldValuesAttributesItemType0,
    )
    from ..models.new_alert_data_attributes_data_type_0 import NewAlertDataAttributesDataType0
    from ..models.new_alert_data_attributes_labels_item_type_0 import NewAlertDataAttributesLabelsItemType0
    from ..models.new_alert_data_attributes_notification_targets_type_0_item import (
        NewAlertDataAttributesNotificationTargetsType0Item,
    )


T = TypeVar("T", bound="NewAlertDataAttributes")


@_attrs_define
class NewAlertDataAttributes:
    """
    Attributes:
        summary (str): The summary of the alert
        noise (Union[Unset, NewAlertDataAttributesNoise]): Whether the alert is marked as noise
        source (Union[Unset, str]): Deprecated. Accepted for backwards compatibility; new clients should omit. Defaults
            to `api`.
        status (Union[Unset, NewAlertDataAttributesStatus]): Only available for organizations with Rootly On-Call
            enabled. Can be one of open, triggered.
        description (Union[None, Unset, str]): The description of the alert
        service_ids (Union[None, Unset, list[str]]): The Service IDs to attach to the alert. If your organization has
            On-Call enabled and your notification target is a Service. This field will be automatically set for you.
        group_ids (Union[None, Unset, list[str]]): The Group IDs to attach to the alert. If your organization has On-
            Call enabled and your notification target is a Group. This field will be automatically set for you.
        functionality_ids (Union[None, Unset, list[str]]): The Functionality IDs to attach to the alert
        environment_ids (Union[None, Unset, list[str]]): The Environment IDs to attach to the alert
        started_at (Union[None, Unset, datetime.datetime]): Alert start datetime
        ended_at (Union[None, Unset, datetime.datetime]): Alert end datetime
        external_id (Union[None, Unset, str]): External ID
        external_url (Union[None, Unset, str]): External Url
        alert_urgency_id (Union[None, Unset, str]): The ID of the alert urgency
        notification_target_type (Union[Unset, NewAlertDataAttributesNotificationTargetType]): Only available for
            organizations with Rootly On-Call enabled. Can be one of Group, Service, EscalationPolicy, Functionality, User.
            Please contact support if you encounter issues using `Functionality` as a notification target type.
        notification_target_id (Union[None, Unset, str]): Only available for organizations with Rootly On-Call enabled.
            The _identifier_ of the notification target object.
        notification_targets (Union[None, Unset, list['NewAlertDataAttributesNotificationTargetsType0Item']]): Only
            available for organizations with Rootly On-Call enabled. Page multiple destinations (any combination of Group,
            Service, EscalationPolicy, Functionality, or User) in a single request. `Functionality` targets require the
            `enable_paging_functionalities` feature; a request that includes one while it is disabled is rejected. Applies
            to alert creation only. When provided, this takes precedence over the singular `notification_target_type` /
            `notification_target_id` fields.
        labels (Union[Unset, list[Union['NewAlertDataAttributesLabelsItemType0', None]]]):
        data (Union['NewAlertDataAttributesDataType0', None, Unset]): Additional data
        deduplication_key (Union[None, Unset, str]): Alerts sharing the same deduplication key are treated as a single
            alert.
        alert_field_values_attributes (Union[Unset,
            list[Union['NewAlertDataAttributesAlertFieldValuesAttributesItemType0', None]]]): Custom alert field values to
            create with the alert
    """

    summary: str
    noise: Union[Unset, NewAlertDataAttributesNoise] = UNSET
    source: Union[Unset, str] = UNSET
    status: Union[Unset, NewAlertDataAttributesStatus] = UNSET
    description: Union[None, Unset, str] = UNSET
    service_ids: Union[None, Unset, list[str]] = UNSET
    group_ids: Union[None, Unset, list[str]] = UNSET
    functionality_ids: Union[None, Unset, list[str]] = UNSET
    environment_ids: Union[None, Unset, list[str]] = UNSET
    started_at: Union[None, Unset, datetime.datetime] = UNSET
    ended_at: Union[None, Unset, datetime.datetime] = UNSET
    external_id: Union[None, Unset, str] = UNSET
    external_url: Union[None, Unset, str] = UNSET
    alert_urgency_id: Union[None, Unset, str] = UNSET
    notification_target_type: Union[Unset, NewAlertDataAttributesNotificationTargetType] = UNSET
    notification_target_id: Union[None, Unset, str] = UNSET
    notification_targets: Union[None, Unset, list["NewAlertDataAttributesNotificationTargetsType0Item"]] = UNSET
    labels: Union[Unset, list[Union["NewAlertDataAttributesLabelsItemType0", None]]] = UNSET
    data: Union["NewAlertDataAttributesDataType0", None, Unset] = UNSET
    deduplication_key: Union[None, Unset, str] = UNSET
    alert_field_values_attributes: Union[
        Unset, list[Union["NewAlertDataAttributesAlertFieldValuesAttributesItemType0", None]]
    ] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.new_alert_data_attributes_alert_field_values_attributes_item_type_0 import (
            NewAlertDataAttributesAlertFieldValuesAttributesItemType0,
        )
        from ..models.new_alert_data_attributes_data_type_0 import NewAlertDataAttributesDataType0
        from ..models.new_alert_data_attributes_labels_item_type_0 import NewAlertDataAttributesLabelsItemType0

        summary = self.summary

        noise: Union[Unset, str] = UNSET
        if not isinstance(self.noise, Unset):
            noise = self.noise

        source = self.source

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        service_ids: Union[None, Unset, list[str]]
        if isinstance(self.service_ids, Unset):
            service_ids = UNSET
        elif isinstance(self.service_ids, list):
            service_ids = self.service_ids

        else:
            service_ids = self.service_ids

        group_ids: Union[None, Unset, list[str]]
        if isinstance(self.group_ids, Unset):
            group_ids = UNSET
        elif isinstance(self.group_ids, list):
            group_ids = self.group_ids

        else:
            group_ids = self.group_ids

        functionality_ids: Union[None, Unset, list[str]]
        if isinstance(self.functionality_ids, Unset):
            functionality_ids = UNSET
        elif isinstance(self.functionality_ids, list):
            functionality_ids = self.functionality_ids

        else:
            functionality_ids = self.functionality_ids

        environment_ids: Union[None, Unset, list[str]]
        if isinstance(self.environment_ids, Unset):
            environment_ids = UNSET
        elif isinstance(self.environment_ids, list):
            environment_ids = self.environment_ids

        else:
            environment_ids = self.environment_ids

        started_at: Union[None, Unset, str]
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        elif isinstance(self.started_at, datetime.datetime):
            started_at = self.started_at.isoformat()
        else:
            started_at = self.started_at

        ended_at: Union[None, Unset, str]
        if isinstance(self.ended_at, Unset):
            ended_at = UNSET
        elif isinstance(self.ended_at, datetime.datetime):
            ended_at = self.ended_at.isoformat()
        else:
            ended_at = self.ended_at

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        external_url: Union[None, Unset, str]
        if isinstance(self.external_url, Unset):
            external_url = UNSET
        else:
            external_url = self.external_url

        alert_urgency_id: Union[None, Unset, str]
        if isinstance(self.alert_urgency_id, Unset):
            alert_urgency_id = UNSET
        else:
            alert_urgency_id = self.alert_urgency_id

        notification_target_type: Union[Unset, str] = UNSET
        if not isinstance(self.notification_target_type, Unset):
            notification_target_type = self.notification_target_type

        notification_target_id: Union[None, Unset, str]
        if isinstance(self.notification_target_id, Unset):
            notification_target_id = UNSET
        else:
            notification_target_id = self.notification_target_id

        notification_targets: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.notification_targets, Unset):
            notification_targets = UNSET
        elif isinstance(self.notification_targets, list):
            notification_targets = []
            for notification_targets_type_0_item_data in self.notification_targets:
                notification_targets_type_0_item = notification_targets_type_0_item_data.to_dict()
                notification_targets.append(notification_targets_type_0_item)

        else:
            notification_targets = self.notification_targets

        labels: Union[Unset, list[Union[None, dict[str, Any]]]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item: Union[None, dict[str, Any]]
                if isinstance(labels_item_data, NewAlertDataAttributesLabelsItemType0):
                    labels_item = labels_item_data.to_dict()
                else:
                    labels_item = labels_item_data
                labels.append(labels_item)

        data: Union[None, Unset, dict[str, Any]]
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, NewAlertDataAttributesDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        deduplication_key: Union[None, Unset, str]
        if isinstance(self.deduplication_key, Unset):
            deduplication_key = UNSET
        else:
            deduplication_key = self.deduplication_key

        alert_field_values_attributes: Union[Unset, list[Union[None, dict[str, Any]]]] = UNSET
        if not isinstance(self.alert_field_values_attributes, Unset):
            alert_field_values_attributes = []
            for alert_field_values_attributes_item_data in self.alert_field_values_attributes:
                alert_field_values_attributes_item: Union[None, dict[str, Any]]
                if isinstance(
                    alert_field_values_attributes_item_data, NewAlertDataAttributesAlertFieldValuesAttributesItemType0
                ):
                    alert_field_values_attributes_item = alert_field_values_attributes_item_data.to_dict()
                else:
                    alert_field_values_attributes_item = alert_field_values_attributes_item_data
                alert_field_values_attributes.append(alert_field_values_attributes_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "summary": summary,
            }
        )
        if noise is not UNSET:
            field_dict["noise"] = noise
        if source is not UNSET:
            field_dict["source"] = source
        if status is not UNSET:
            field_dict["status"] = status
        if description is not UNSET:
            field_dict["description"] = description
        if service_ids is not UNSET:
            field_dict["service_ids"] = service_ids
        if group_ids is not UNSET:
            field_dict["group_ids"] = group_ids
        if functionality_ids is not UNSET:
            field_dict["functionality_ids"] = functionality_ids
        if environment_ids is not UNSET:
            field_dict["environment_ids"] = environment_ids
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if ended_at is not UNSET:
            field_dict["ended_at"] = ended_at
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if external_url is not UNSET:
            field_dict["external_url"] = external_url
        if alert_urgency_id is not UNSET:
            field_dict["alert_urgency_id"] = alert_urgency_id
        if notification_target_type is not UNSET:
            field_dict["notification_target_type"] = notification_target_type
        if notification_target_id is not UNSET:
            field_dict["notification_target_id"] = notification_target_id
        if notification_targets is not UNSET:
            field_dict["notification_targets"] = notification_targets
        if labels is not UNSET:
            field_dict["labels"] = labels
        if data is not UNSET:
            field_dict["data"] = data
        if deduplication_key is not UNSET:
            field_dict["deduplication_key"] = deduplication_key
        if alert_field_values_attributes is not UNSET:
            field_dict["alert_field_values_attributes"] = alert_field_values_attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_alert_data_attributes_alert_field_values_attributes_item_type_0 import (
            NewAlertDataAttributesAlertFieldValuesAttributesItemType0,
        )
        from ..models.new_alert_data_attributes_data_type_0 import NewAlertDataAttributesDataType0
        from ..models.new_alert_data_attributes_labels_item_type_0 import NewAlertDataAttributesLabelsItemType0
        from ..models.new_alert_data_attributes_notification_targets_type_0_item import (
            NewAlertDataAttributesNotificationTargetsType0Item,
        )

        d = dict(src_dict)
        summary = d.pop("summary")

        _noise = d.pop("noise", UNSET)
        noise: Union[Unset, NewAlertDataAttributesNoise]
        if isinstance(_noise, Unset):
            noise = UNSET
        else:
            noise = check_new_alert_data_attributes_noise(_noise)

        source = d.pop("source", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, NewAlertDataAttributesStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_new_alert_data_attributes_status(_status)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_service_ids(data: object) -> Union[None, Unset, list[str]]:
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
            return cast(Union[None, Unset, list[str]], data)

        service_ids = _parse_service_ids(d.pop("service_ids", UNSET))

        def _parse_group_ids(data: object) -> Union[None, Unset, list[str]]:
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
            return cast(Union[None, Unset, list[str]], data)

        group_ids = _parse_group_ids(d.pop("group_ids", UNSET))

        def _parse_functionality_ids(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                functionality_ids_type_0 = cast(list[str], data)

                return functionality_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        functionality_ids = _parse_functionality_ids(d.pop("functionality_ids", UNSET))

        def _parse_environment_ids(data: object) -> Union[None, Unset, list[str]]:
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
            return cast(Union[None, Unset, list[str]], data)

        environment_ids = _parse_environment_ids(d.pop("environment_ids", UNSET))

        def _parse_started_at(data: object) -> Union[None, Unset, datetime.datetime]:
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
            return cast(Union[None, Unset, datetime.datetime], data)

        started_at = _parse_started_at(d.pop("started_at", UNSET))

        def _parse_ended_at(data: object) -> Union[None, Unset, datetime.datetime]:
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
            return cast(Union[None, Unset, datetime.datetime], data)

        ended_at = _parse_ended_at(d.pop("ended_at", UNSET))

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("external_id", UNSET))

        def _parse_external_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_url = _parse_external_url(d.pop("external_url", UNSET))

        def _parse_alert_urgency_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        alert_urgency_id = _parse_alert_urgency_id(d.pop("alert_urgency_id", UNSET))

        _notification_target_type = d.pop("notification_target_type", UNSET)
        notification_target_type: Union[Unset, NewAlertDataAttributesNotificationTargetType]
        if isinstance(_notification_target_type, Unset):
            notification_target_type = UNSET
        else:
            notification_target_type = check_new_alert_data_attributes_notification_target_type(
                _notification_target_type
            )

        def _parse_notification_target_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        notification_target_id = _parse_notification_target_id(d.pop("notification_target_id", UNSET))

        def _parse_notification_targets(
            data: object,
        ) -> Union[None, Unset, list["NewAlertDataAttributesNotificationTargetsType0Item"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                notification_targets_type_0 = []
                _notification_targets_type_0 = data
                for notification_targets_type_0_item_data in _notification_targets_type_0:
                    notification_targets_type_0_item = NewAlertDataAttributesNotificationTargetsType0Item.from_dict(
                        notification_targets_type_0_item_data
                    )

                    notification_targets_type_0.append(notification_targets_type_0_item)

                return notification_targets_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["NewAlertDataAttributesNotificationTargetsType0Item"]], data)

        notification_targets = _parse_notification_targets(d.pop("notification_targets", UNSET))

        labels = []
        _labels = d.pop("labels", UNSET)
        for labels_item_data in _labels or []:

            def _parse_labels_item(data: object) -> Union["NewAlertDataAttributesLabelsItemType0", None]:
                if data is None:
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    labels_item_type_0 = NewAlertDataAttributesLabelsItemType0.from_dict(data)

                    return labels_item_type_0
                except:  # noqa: E722
                    pass
                return cast(Union["NewAlertDataAttributesLabelsItemType0", None], data)

            labels_item = _parse_labels_item(labels_item_data)

            labels.append(labels_item)

        def _parse_data(data: object) -> Union["NewAlertDataAttributesDataType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = NewAlertDataAttributesDataType0.from_dict(data)

                return data_type_0
            except:  # noqa: E722
                pass
            return cast(Union["NewAlertDataAttributesDataType0", None, Unset], data)

        data = _parse_data(d.pop("data", UNSET))

        def _parse_deduplication_key(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deduplication_key = _parse_deduplication_key(d.pop("deduplication_key", UNSET))

        alert_field_values_attributes = []
        _alert_field_values_attributes = d.pop("alert_field_values_attributes", UNSET)
        for alert_field_values_attributes_item_data in _alert_field_values_attributes or []:

            def _parse_alert_field_values_attributes_item(
                data: object,
            ) -> Union["NewAlertDataAttributesAlertFieldValuesAttributesItemType0", None]:
                if data is None:
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    alert_field_values_attributes_item_type_0 = (
                        NewAlertDataAttributesAlertFieldValuesAttributesItemType0.from_dict(data)
                    )

                    return alert_field_values_attributes_item_type_0
                except:  # noqa: E722
                    pass
                return cast(Union["NewAlertDataAttributesAlertFieldValuesAttributesItemType0", None], data)

            alert_field_values_attributes_item = _parse_alert_field_values_attributes_item(
                alert_field_values_attributes_item_data
            )

            alert_field_values_attributes.append(alert_field_values_attributes_item)

        new_alert_data_attributes = cls(
            summary=summary,
            noise=noise,
            source=source,
            status=status,
            description=description,
            service_ids=service_ids,
            group_ids=group_ids,
            functionality_ids=functionality_ids,
            environment_ids=environment_ids,
            started_at=started_at,
            ended_at=ended_at,
            external_id=external_id,
            external_url=external_url,
            alert_urgency_id=alert_urgency_id,
            notification_target_type=notification_target_type,
            notification_target_id=notification_target_id,
            notification_targets=notification_targets,
            labels=labels,
            data=data,
            deduplication_key=deduplication_key,
            alert_field_values_attributes=alert_field_values_attributes,
        )

        return new_alert_data_attributes
