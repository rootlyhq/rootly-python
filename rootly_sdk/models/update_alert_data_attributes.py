import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.update_alert_data_attributes_noise import (
    UpdateAlertDataAttributesNoise,
    check_update_alert_data_attributes_noise,
)
from ..models.update_alert_data_attributes_source import (
    UpdateAlertDataAttributesSource,
    check_update_alert_data_attributes_source,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_alert_data_attributes_alert_field_values_attributes_item_type_0 import (
        UpdateAlertDataAttributesAlertFieldValuesAttributesItemType0,
    )
    from ..models.update_alert_data_attributes_data_type_0 import UpdateAlertDataAttributesDataType0
    from ..models.update_alert_data_attributes_labels_item_type_0 import UpdateAlertDataAttributesLabelsItemType0


T = TypeVar("T", bound="UpdateAlertDataAttributes")


@_attrs_define
class UpdateAlertDataAttributes:
    """
    Attributes:
        noise (Union[Unset, UpdateAlertDataAttributesNoise]): Whether the alert is marked as noise
        source (Union[Unset, UpdateAlertDataAttributesSource]): The source of the alert
        summary (Union[Unset, str]): The summary of the alert
        description (Union[None, Unset, str]): The description of the alert
        service_ids (Union[None, Unset, list[str]]): The Service IDs to attach to the alert
        group_ids (Union[None, Unset, list[str]]): The Group IDs to attach to the alert
        environment_ids (Union[None, Unset, list[str]]): The Environment IDs to attach to the alert
        started_at (Union[None, Unset, datetime.datetime]): Alert start datetime
        ended_at (Union[None, Unset, datetime.datetime]): Alert end datetime
        external_id (Union[None, Unset, str]): External ID
        external_url (Union[None, Unset, str]): External Url
        alert_urgency_id (Union[None, Unset, str]): The ID of the alert urgency
        labels (Union[Unset, list[Union['UpdateAlertDataAttributesLabelsItemType0', None]]]):
        data (Union['UpdateAlertDataAttributesDataType0', None, Unset]): Additional data
        deduplication_key (Union[None, Unset, str]): Alerts sharing the same deduplication key are treated as a single
            alert.
        alert_field_values_attributes (Union[Unset,
            list[Union['UpdateAlertDataAttributesAlertFieldValuesAttributesItemType0', None]]]): Custom alert field values
            to create with the alert
    """

    noise: Union[Unset, UpdateAlertDataAttributesNoise] = UNSET
    source: Union[Unset, UpdateAlertDataAttributesSource] = UNSET
    summary: Union[Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    service_ids: Union[None, Unset, list[str]] = UNSET
    group_ids: Union[None, Unset, list[str]] = UNSET
    environment_ids: Union[None, Unset, list[str]] = UNSET
    started_at: Union[None, Unset, datetime.datetime] = UNSET
    ended_at: Union[None, Unset, datetime.datetime] = UNSET
    external_id: Union[None, Unset, str] = UNSET
    external_url: Union[None, Unset, str] = UNSET
    alert_urgency_id: Union[None, Unset, str] = UNSET
    labels: Union[Unset, list[Union["UpdateAlertDataAttributesLabelsItemType0", None]]] = UNSET
    data: Union["UpdateAlertDataAttributesDataType0", None, Unset] = UNSET
    deduplication_key: Union[None, Unset, str] = UNSET
    alert_field_values_attributes: Union[
        Unset, list[Union["UpdateAlertDataAttributesAlertFieldValuesAttributesItemType0", None]]
    ] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_alert_data_attributes_alert_field_values_attributes_item_type_0 import (
            UpdateAlertDataAttributesAlertFieldValuesAttributesItemType0,
        )
        from ..models.update_alert_data_attributes_data_type_0 import UpdateAlertDataAttributesDataType0
        from ..models.update_alert_data_attributes_labels_item_type_0 import UpdateAlertDataAttributesLabelsItemType0

        noise: Union[Unset, str] = UNSET
        if not isinstance(self.noise, Unset):
            noise = self.noise

        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source

        summary = self.summary

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

        labels: Union[Unset, list[Union[None, dict[str, Any]]]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item: Union[None, dict[str, Any]]
                if isinstance(labels_item_data, UpdateAlertDataAttributesLabelsItemType0):
                    labels_item = labels_item_data.to_dict()
                else:
                    labels_item = labels_item_data
                labels.append(labels_item)

        data: Union[None, Unset, dict[str, Any]]
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, UpdateAlertDataAttributesDataType0):
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
                    alert_field_values_attributes_item_data,
                    UpdateAlertDataAttributesAlertFieldValuesAttributesItemType0,
                ):
                    alert_field_values_attributes_item = alert_field_values_attributes_item_data.to_dict()
                else:
                    alert_field_values_attributes_item = alert_field_values_attributes_item_data
                alert_field_values_attributes.append(alert_field_values_attributes_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if noise is not UNSET:
            field_dict["noise"] = noise
        if source is not UNSET:
            field_dict["source"] = source
        if summary is not UNSET:
            field_dict["summary"] = summary
        if description is not UNSET:
            field_dict["description"] = description
        if service_ids is not UNSET:
            field_dict["service_ids"] = service_ids
        if group_ids is not UNSET:
            field_dict["group_ids"] = group_ids
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
        from ..models.update_alert_data_attributes_alert_field_values_attributes_item_type_0 import (
            UpdateAlertDataAttributesAlertFieldValuesAttributesItemType0,
        )
        from ..models.update_alert_data_attributes_data_type_0 import UpdateAlertDataAttributesDataType0
        from ..models.update_alert_data_attributes_labels_item_type_0 import UpdateAlertDataAttributesLabelsItemType0

        d = dict(src_dict)
        _noise = d.pop("noise", UNSET)
        noise: Union[Unset, UpdateAlertDataAttributesNoise]
        if isinstance(_noise, Unset):
            noise = UNSET
        else:
            noise = check_update_alert_data_attributes_noise(_noise)

        _source = d.pop("source", UNSET)
        source: Union[Unset, UpdateAlertDataAttributesSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = check_update_alert_data_attributes_source(_source)

        summary = d.pop("summary", UNSET)

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

        labels = []
        _labels = d.pop("labels", UNSET)
        for labels_item_data in _labels or []:

            def _parse_labels_item(data: object) -> Union["UpdateAlertDataAttributesLabelsItemType0", None]:
                if data is None:
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    labels_item_type_0 = UpdateAlertDataAttributesLabelsItemType0.from_dict(data)

                    return labels_item_type_0
                except:  # noqa: E722
                    pass
                return cast(Union["UpdateAlertDataAttributesLabelsItemType0", None], data)

            labels_item = _parse_labels_item(labels_item_data)

            labels.append(labels_item)

        def _parse_data(data: object) -> Union["UpdateAlertDataAttributesDataType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = UpdateAlertDataAttributesDataType0.from_dict(data)

                return data_type_0
            except:  # noqa: E722
                pass
            return cast(Union["UpdateAlertDataAttributesDataType0", None, Unset], data)

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
            ) -> Union["UpdateAlertDataAttributesAlertFieldValuesAttributesItemType0", None]:
                if data is None:
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    alert_field_values_attributes_item_type_0 = (
                        UpdateAlertDataAttributesAlertFieldValuesAttributesItemType0.from_dict(data)
                    )

                    return alert_field_values_attributes_item_type_0
                except:  # noqa: E722
                    pass
                return cast(Union["UpdateAlertDataAttributesAlertFieldValuesAttributesItemType0", None], data)

            alert_field_values_attributes_item = _parse_alert_field_values_attributes_item(
                alert_field_values_attributes_item_data
            )

            alert_field_values_attributes.append(alert_field_values_attributes_item)

        update_alert_data_attributes = cls(
            noise=noise,
            source=source,
            summary=summary,
            description=description,
            service_ids=service_ids,
            group_ids=group_ids,
            environment_ids=environment_ids,
            started_at=started_at,
            ended_at=ended_at,
            external_id=external_id,
            external_url=external_url,
            alert_urgency_id=alert_urgency_id,
            labels=labels,
            data=data,
            deduplication_key=deduplication_key,
            alert_field_values_attributes=alert_field_values_attributes,
        )

        return update_alert_data_attributes
