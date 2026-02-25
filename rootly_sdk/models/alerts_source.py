from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alerts_source_deduplication_key_kind import (
    AlertsSourceDeduplicationKeyKind,
    check_alerts_source_deduplication_key_kind,
)
from ..models.alerts_source_source_type import AlertsSourceSourceType, check_alerts_source_source_type
from ..models.alerts_source_status import AlertsSourceStatus, check_alerts_source_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alerts_source_alert_source_fields_attributes_item import AlertsSourceAlertSourceFieldsAttributesItem
    from ..models.alerts_source_alert_source_urgency_rules_attributes_item import (
        AlertsSourceAlertSourceUrgencyRulesAttributesItem,
    )
    from ..models.alerts_source_alert_template_attributes_type_0 import AlertsSourceAlertTemplateAttributesType0
    from ..models.alerts_source_resolution_rule_attributes_type_0 import AlertsSourceResolutionRuleAttributesType0
    from ..models.alerts_source_sourceable_attributes_type_0 import AlertsSourceSourceableAttributesType0


T = TypeVar("T", bound="AlertsSource")


@_attrs_define
class AlertsSource:
    """
    Attributes:
        name (str): The name of the alert source
        status (AlertsSourceStatus): The status of the alert source
        secret (str): The secret used to authenticate non-email alert sources
        created_at (str): Date of creation
        updated_at (str): Date of last update
        source_type (Union[Unset, AlertsSourceSourceType]): The alert source type
        alert_urgency_id (Union[Unset, str]): ID for the default alert urgency assigned to this alert source
        deduplicate_alerts_by_key (Union[Unset, bool]): Toggle alert deduplication using deduplication key. If enabled,
            deduplication_key_kind and deduplication_key_path are required.
        deduplication_key_kind (Union[Unset, AlertsSourceDeduplicationKeyKind]): Kind of deduplication key.
        deduplication_key_path (Union[None, Unset, str]): Path to deduplication key. This is a JSON Path to extract the
            deduplication key from the request body.
        deduplication_key_regexp (Union[None, Unset, str]): Regular expression to extract key from value found at key
            path.
        owner_group_ids (Union[Unset, list[str]]): List of team IDs that will own the alert source
        alert_template_attributes (Union['AlertsSourceAlertTemplateAttributesType0', None, Unset]):
        alert_source_urgency_rules_attributes (Union[Unset, list['AlertsSourceAlertSourceUrgencyRulesAttributesItem']]):
            List of rules that define the conditions under which the alert urgency will be set automatically based on the
            alert payload
        sourceable_attributes (Union['AlertsSourceSourceableAttributesType0', None, Unset]): Provide additional
            attributes for generic_webhook alerts source
        resolution_rule_attributes (Union['AlertsSourceResolutionRuleAttributesType0', None, Unset]): Provide additional
            attributes for email alerts source
        alert_source_fields_attributes (Union[Unset, list['AlertsSourceAlertSourceFieldsAttributesItem']]): List of
            alert fields to be added to the alert source. Note: This attribute requires the alert field feature to be
            enabled on your account. Contact Rootly customer support if you need assistance with this feature.
        email (Union[None, Unset, str]): The email generated for email alert sources
        webhook_endpoint (Union[None, Unset, str]): The webhook URL generated for non-email alert sources
    """

    name: str
    status: AlertsSourceStatus
    secret: str
    created_at: str
    updated_at: str
    source_type: Unset | AlertsSourceSourceType = UNSET
    alert_urgency_id: Unset | str = UNSET
    deduplicate_alerts_by_key: Unset | bool = UNSET
    deduplication_key_kind: Unset | AlertsSourceDeduplicationKeyKind = UNSET
    deduplication_key_path: None | Unset | str = UNSET
    deduplication_key_regexp: None | Unset | str = UNSET
    owner_group_ids: Unset | list[str] = UNSET
    alert_template_attributes: Union["AlertsSourceAlertTemplateAttributesType0", None, Unset] = UNSET
    alert_source_urgency_rules_attributes: Unset | list["AlertsSourceAlertSourceUrgencyRulesAttributesItem"] = UNSET
    sourceable_attributes: Union["AlertsSourceSourceableAttributesType0", None, Unset] = UNSET
    resolution_rule_attributes: Union["AlertsSourceResolutionRuleAttributesType0", None, Unset] = UNSET
    alert_source_fields_attributes: Unset | list["AlertsSourceAlertSourceFieldsAttributesItem"] = UNSET
    email: None | Unset | str = UNSET
    webhook_endpoint: None | Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.alerts_source_alert_template_attributes_type_0 import AlertsSourceAlertTemplateAttributesType0
        from ..models.alerts_source_resolution_rule_attributes_type_0 import AlertsSourceResolutionRuleAttributesType0
        from ..models.alerts_source_sourceable_attributes_type_0 import AlertsSourceSourceableAttributesType0

        name = self.name

        status: str = self.status

        secret = self.secret

        created_at = self.created_at

        updated_at = self.updated_at

        source_type: Unset | str = UNSET
        if not isinstance(self.source_type, Unset):
            source_type = self.source_type

        alert_urgency_id = self.alert_urgency_id

        deduplicate_alerts_by_key = self.deduplicate_alerts_by_key

        deduplication_key_kind: Unset | str = UNSET
        if not isinstance(self.deduplication_key_kind, Unset):
            deduplication_key_kind = self.deduplication_key_kind

        deduplication_key_path: None | Unset | str
        if isinstance(self.deduplication_key_path, Unset):
            deduplication_key_path = UNSET
        else:
            deduplication_key_path = self.deduplication_key_path

        deduplication_key_regexp: None | Unset | str
        if isinstance(self.deduplication_key_regexp, Unset):
            deduplication_key_regexp = UNSET
        else:
            deduplication_key_regexp = self.deduplication_key_regexp

        owner_group_ids: Unset | list[str] = UNSET
        if not isinstance(self.owner_group_ids, Unset):
            owner_group_ids = self.owner_group_ids

        alert_template_attributes: None | Unset | dict[str, Any]
        if isinstance(self.alert_template_attributes, Unset):
            alert_template_attributes = UNSET
        elif isinstance(self.alert_template_attributes, AlertsSourceAlertTemplateAttributesType0):
            alert_template_attributes = self.alert_template_attributes.to_dict()
        else:
            alert_template_attributes = self.alert_template_attributes

        alert_source_urgency_rules_attributes: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.alert_source_urgency_rules_attributes, Unset):
            alert_source_urgency_rules_attributes = []
            for alert_source_urgency_rules_attributes_item_data in self.alert_source_urgency_rules_attributes:
                alert_source_urgency_rules_attributes_item = alert_source_urgency_rules_attributes_item_data.to_dict()
                alert_source_urgency_rules_attributes.append(alert_source_urgency_rules_attributes_item)

        sourceable_attributes: None | Unset | dict[str, Any]
        if isinstance(self.sourceable_attributes, Unset):
            sourceable_attributes = UNSET
        elif isinstance(self.sourceable_attributes, AlertsSourceSourceableAttributesType0):
            sourceable_attributes = self.sourceable_attributes.to_dict()
        else:
            sourceable_attributes = self.sourceable_attributes

        resolution_rule_attributes: None | Unset | dict[str, Any]
        if isinstance(self.resolution_rule_attributes, Unset):
            resolution_rule_attributes = UNSET
        elif isinstance(self.resolution_rule_attributes, AlertsSourceResolutionRuleAttributesType0):
            resolution_rule_attributes = self.resolution_rule_attributes.to_dict()
        else:
            resolution_rule_attributes = self.resolution_rule_attributes

        alert_source_fields_attributes: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.alert_source_fields_attributes, Unset):
            alert_source_fields_attributes = []
            for alert_source_fields_attributes_item_data in self.alert_source_fields_attributes:
                alert_source_fields_attributes_item = alert_source_fields_attributes_item_data.to_dict()
                alert_source_fields_attributes.append(alert_source_fields_attributes_item)

        email: None | Unset | str
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        webhook_endpoint: None | Unset | str
        if isinstance(self.webhook_endpoint, Unset):
            webhook_endpoint = UNSET
        else:
            webhook_endpoint = self.webhook_endpoint

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "status": status,
                "secret": secret,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if source_type is not UNSET:
            field_dict["source_type"] = source_type
        if alert_urgency_id is not UNSET:
            field_dict["alert_urgency_id"] = alert_urgency_id
        if deduplicate_alerts_by_key is not UNSET:
            field_dict["deduplicate_alerts_by_key"] = deduplicate_alerts_by_key
        if deduplication_key_kind is not UNSET:
            field_dict["deduplication_key_kind"] = deduplication_key_kind
        if deduplication_key_path is not UNSET:
            field_dict["deduplication_key_path"] = deduplication_key_path
        if deduplication_key_regexp is not UNSET:
            field_dict["deduplication_key_regexp"] = deduplication_key_regexp
        if owner_group_ids is not UNSET:
            field_dict["owner_group_ids"] = owner_group_ids
        if alert_template_attributes is not UNSET:
            field_dict["alert_template_attributes"] = alert_template_attributes
        if alert_source_urgency_rules_attributes is not UNSET:
            field_dict["alert_source_urgency_rules_attributes"] = alert_source_urgency_rules_attributes
        if sourceable_attributes is not UNSET:
            field_dict["sourceable_attributes"] = sourceable_attributes
        if resolution_rule_attributes is not UNSET:
            field_dict["resolution_rule_attributes"] = resolution_rule_attributes
        if alert_source_fields_attributes is not UNSET:
            field_dict["alert_source_fields_attributes"] = alert_source_fields_attributes
        if email is not UNSET:
            field_dict["email"] = email
        if webhook_endpoint is not UNSET:
            field_dict["webhook_endpoint"] = webhook_endpoint

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alerts_source_alert_source_fields_attributes_item import (
            AlertsSourceAlertSourceFieldsAttributesItem,
        )
        from ..models.alerts_source_alert_source_urgency_rules_attributes_item import (
            AlertsSourceAlertSourceUrgencyRulesAttributesItem,
        )
        from ..models.alerts_source_alert_template_attributes_type_0 import AlertsSourceAlertTemplateAttributesType0
        from ..models.alerts_source_resolution_rule_attributes_type_0 import AlertsSourceResolutionRuleAttributesType0
        from ..models.alerts_source_sourceable_attributes_type_0 import AlertsSourceSourceableAttributesType0

        d = dict(src_dict)
        name = d.pop("name")

        status = check_alerts_source_status(d.pop("status"))

        secret = d.pop("secret")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        _source_type = d.pop("source_type", UNSET)
        source_type: Unset | AlertsSourceSourceType
        if isinstance(_source_type, Unset):
            source_type = UNSET
        else:
            source_type = check_alerts_source_source_type(_source_type)

        alert_urgency_id = d.pop("alert_urgency_id", UNSET)

        deduplicate_alerts_by_key = d.pop("deduplicate_alerts_by_key", UNSET)

        _deduplication_key_kind = d.pop("deduplication_key_kind", UNSET)
        deduplication_key_kind: Unset | AlertsSourceDeduplicationKeyKind
        if isinstance(_deduplication_key_kind, Unset):
            deduplication_key_kind = UNSET
        else:
            deduplication_key_kind = check_alerts_source_deduplication_key_kind(_deduplication_key_kind)

        def _parse_deduplication_key_path(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        deduplication_key_path = _parse_deduplication_key_path(d.pop("deduplication_key_path", UNSET))

        def _parse_deduplication_key_regexp(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        deduplication_key_regexp = _parse_deduplication_key_regexp(d.pop("deduplication_key_regexp", UNSET))

        owner_group_ids = cast(list[str], d.pop("owner_group_ids", UNSET))

        def _parse_alert_template_attributes(
            data: object,
        ) -> Union["AlertsSourceAlertTemplateAttributesType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                alert_template_attributes_type_0 = AlertsSourceAlertTemplateAttributesType0.from_dict(data)

                return alert_template_attributes_type_0
            except:  # noqa: E722
                pass
            return cast(Union["AlertsSourceAlertTemplateAttributesType0", None, Unset], data)

        alert_template_attributes = _parse_alert_template_attributes(d.pop("alert_template_attributes", UNSET))

        alert_source_urgency_rules_attributes = []
        _alert_source_urgency_rules_attributes = d.pop("alert_source_urgency_rules_attributes", UNSET)
        for alert_source_urgency_rules_attributes_item_data in _alert_source_urgency_rules_attributes or []:
            alert_source_urgency_rules_attributes_item = AlertsSourceAlertSourceUrgencyRulesAttributesItem.from_dict(
                alert_source_urgency_rules_attributes_item_data
            )

            alert_source_urgency_rules_attributes.append(alert_source_urgency_rules_attributes_item)

        def _parse_sourceable_attributes(data: object) -> Union["AlertsSourceSourceableAttributesType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                sourceable_attributes_type_0 = AlertsSourceSourceableAttributesType0.from_dict(data)

                return sourceable_attributes_type_0
            except:  # noqa: E722
                pass
            return cast(Union["AlertsSourceSourceableAttributesType0", None, Unset], data)

        sourceable_attributes = _parse_sourceable_attributes(d.pop("sourceable_attributes", UNSET))

        def _parse_resolution_rule_attributes(
            data: object,
        ) -> Union["AlertsSourceResolutionRuleAttributesType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                resolution_rule_attributes_type_0 = AlertsSourceResolutionRuleAttributesType0.from_dict(data)

                return resolution_rule_attributes_type_0
            except:  # noqa: E722
                pass
            return cast(Union["AlertsSourceResolutionRuleAttributesType0", None, Unset], data)

        resolution_rule_attributes = _parse_resolution_rule_attributes(d.pop("resolution_rule_attributes", UNSET))

        alert_source_fields_attributes = []
        _alert_source_fields_attributes = d.pop("alert_source_fields_attributes", UNSET)
        for alert_source_fields_attributes_item_data in _alert_source_fields_attributes or []:
            alert_source_fields_attributes_item = AlertsSourceAlertSourceFieldsAttributesItem.from_dict(
                alert_source_fields_attributes_item_data
            )

            alert_source_fields_attributes.append(alert_source_fields_attributes_item)

        def _parse_email(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_webhook_endpoint(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        webhook_endpoint = _parse_webhook_endpoint(d.pop("webhook_endpoint", UNSET))

        alerts_source = cls(
            name=name,
            status=status,
            secret=secret,
            created_at=created_at,
            updated_at=updated_at,
            source_type=source_type,
            alert_urgency_id=alert_urgency_id,
            deduplicate_alerts_by_key=deduplicate_alerts_by_key,
            deduplication_key_kind=deduplication_key_kind,
            deduplication_key_path=deduplication_key_path,
            deduplication_key_regexp=deduplication_key_regexp,
            owner_group_ids=owner_group_ids,
            alert_template_attributes=alert_template_attributes,
            alert_source_urgency_rules_attributes=alert_source_urgency_rules_attributes,
            sourceable_attributes=sourceable_attributes,
            resolution_rule_attributes=resolution_rule_attributes,
            alert_source_fields_attributes=alert_source_fields_attributes,
            email=email,
            webhook_endpoint=webhook_endpoint,
        )

        alerts_source.additional_properties = d
        return alerts_source

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
