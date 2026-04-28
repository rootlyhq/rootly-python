from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.update_status_page_data_attributes_authentication_method import (
    UpdateStatusPageDataAttributesAuthenticationMethod,
    check_update_status_page_data_attributes_authentication_method,
)
from ..models.update_status_page_data_attributes_saml_name_identifier_format import (
    UpdateStatusPageDataAttributesSamlNameIdentifierFormat,
    check_update_status_page_data_attributes_saml_name_identifier_format,
)
from ..models.update_status_page_data_attributes_section_order_type_0_item import (
    UpdateStatusPageDataAttributesSectionOrderType0Item,
    check_update_status_page_data_attributes_section_order_type_0_item,
)
from ..models.update_status_page_data_attributes_show_uptime_last_days import (
    UpdateStatusPageDataAttributesShowUptimeLastDays,
    check_update_status_page_data_attributes_show_uptime_last_days,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateStatusPageDataAttributes")


@_attrs_define
class UpdateStatusPageDataAttributes:
    """
    Attributes:
        title (str | Unset): The title of the status page
        public_title (None | str | Unset): The public title of the status page
        description (None | str | Unset): The description of the status page
        public_description (None | str | Unset): The public description of the status page
        header_color (None | str | Unset): The color of the header. Eg. "#0061F2"
        footer_color (None | str | Unset): The color of the footer. Eg. "#1F2F41"
        allow_search_engine_index (bool | None | Unset): Allow search engines to include your public status page in
            search results
        show_uptime (bool | None | Unset): Show uptime
        show_uptime_last_days (UpdateStatusPageDataAttributesShowUptimeLastDays | Unset): Show uptime over x days
        success_message (None | str | Unset): Message showing when all components are operational
        failure_message (None | str | Unset): Message showing when at least one component is not operational
        authentication_method (UpdateStatusPageDataAttributesAuthenticationMethod | Unset): Authentication method
            Default: 'none'.
        authentication_enabled (bool | None | Unset): Enable authentication (deprecated - use authentication_method
            instead) Default: False.
        authentication_password (None | str | Unset): Authentication password
        saml_idp_sso_service_url (None | str | Unset): SAML IdP SSO service URL
        saml_idp_slo_service_url (None | str | Unset): SAML IdP SLO service URL
        saml_idp_cert (None | str | Unset): SAML IdP certificate
        saml_name_identifier_format (UpdateStatusPageDataAttributesSamlNameIdentifierFormat | Unset): SAML name
            identifier format
        section_order (list[UpdateStatusPageDataAttributesSectionOrderType0Item] | None | Unset): Order of sections on
            the status page
        external_domain_names (list[str] | None | Unset): External domain names attached to the status page
        website_url (None | str | Unset): Website URL
        website_privacy_url (None | str | Unset): Website Privacy URL
        website_support_url (None | str | Unset): Website Support URL
        ga_tracking_id (None | str | Unset): Google Analytics tracking ID
        time_zone (None | str | Unset): A valid IANA time zone name. Default: 'Etc/UTC'.
        public (bool | None | Unset): Make the status page accessible to the public
        service_ids (list[str] | Unset): Services attached to the status page
        functionality_ids (list[str] | Unset): Functionalities attached to the status page
        enabled (bool | None | Unset): Enabled / Disable the status page
    """

    title: str | Unset = UNSET
    public_title: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    public_description: None | str | Unset = UNSET
    header_color: None | str | Unset = UNSET
    footer_color: None | str | Unset = UNSET
    allow_search_engine_index: bool | None | Unset = UNSET
    show_uptime: bool | None | Unset = UNSET
    show_uptime_last_days: UpdateStatusPageDataAttributesShowUptimeLastDays | Unset = UNSET
    success_message: None | str | Unset = UNSET
    failure_message: None | str | Unset = UNSET
    authentication_method: UpdateStatusPageDataAttributesAuthenticationMethod | Unset = "none"
    authentication_enabled: bool | None | Unset = False
    authentication_password: None | str | Unset = UNSET
    saml_idp_sso_service_url: None | str | Unset = UNSET
    saml_idp_slo_service_url: None | str | Unset = UNSET
    saml_idp_cert: None | str | Unset = UNSET
    saml_name_identifier_format: UpdateStatusPageDataAttributesSamlNameIdentifierFormat | Unset = UNSET
    section_order: list[UpdateStatusPageDataAttributesSectionOrderType0Item] | None | Unset = UNSET
    external_domain_names: list[str] | None | Unset = UNSET
    website_url: None | str | Unset = UNSET
    website_privacy_url: None | str | Unset = UNSET
    website_support_url: None | str | Unset = UNSET
    ga_tracking_id: None | str | Unset = UNSET
    time_zone: None | str | Unset = "Etc/UTC"
    public: bool | None | Unset = UNSET
    service_ids: list[str] | Unset = UNSET
    functionality_ids: list[str] | Unset = UNSET
    enabled: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        public_title: None | str | Unset
        if isinstance(self.public_title, Unset):
            public_title = UNSET
        else:
            public_title = self.public_title

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        public_description: None | str | Unset
        if isinstance(self.public_description, Unset):
            public_description = UNSET
        else:
            public_description = self.public_description

        header_color: None | str | Unset
        if isinstance(self.header_color, Unset):
            header_color = UNSET
        else:
            header_color = self.header_color

        footer_color: None | str | Unset
        if isinstance(self.footer_color, Unset):
            footer_color = UNSET
        else:
            footer_color = self.footer_color

        allow_search_engine_index: bool | None | Unset
        if isinstance(self.allow_search_engine_index, Unset):
            allow_search_engine_index = UNSET
        else:
            allow_search_engine_index = self.allow_search_engine_index

        show_uptime: bool | None | Unset
        if isinstance(self.show_uptime, Unset):
            show_uptime = UNSET
        else:
            show_uptime = self.show_uptime

        show_uptime_last_days: int | Unset = UNSET
        if not isinstance(self.show_uptime_last_days, Unset):
            show_uptime_last_days = self.show_uptime_last_days

        success_message: None | str | Unset
        if isinstance(self.success_message, Unset):
            success_message = UNSET
        else:
            success_message = self.success_message

        failure_message: None | str | Unset
        if isinstance(self.failure_message, Unset):
            failure_message = UNSET
        else:
            failure_message = self.failure_message

        authentication_method: str | Unset = UNSET
        if not isinstance(self.authentication_method, Unset):
            authentication_method = self.authentication_method

        authentication_enabled: bool | None | Unset
        if isinstance(self.authentication_enabled, Unset):
            authentication_enabled = UNSET
        else:
            authentication_enabled = self.authentication_enabled

        authentication_password: None | str | Unset
        if isinstance(self.authentication_password, Unset):
            authentication_password = UNSET
        else:
            authentication_password = self.authentication_password

        saml_idp_sso_service_url: None | str | Unset
        if isinstance(self.saml_idp_sso_service_url, Unset):
            saml_idp_sso_service_url = UNSET
        else:
            saml_idp_sso_service_url = self.saml_idp_sso_service_url

        saml_idp_slo_service_url: None | str | Unset
        if isinstance(self.saml_idp_slo_service_url, Unset):
            saml_idp_slo_service_url = UNSET
        else:
            saml_idp_slo_service_url = self.saml_idp_slo_service_url

        saml_idp_cert: None | str | Unset
        if isinstance(self.saml_idp_cert, Unset):
            saml_idp_cert = UNSET
        else:
            saml_idp_cert = self.saml_idp_cert

        saml_name_identifier_format: str | Unset = UNSET
        if not isinstance(self.saml_name_identifier_format, Unset):
            saml_name_identifier_format = self.saml_name_identifier_format

        section_order: list[str] | None | Unset
        if isinstance(self.section_order, Unset):
            section_order = UNSET
        elif isinstance(self.section_order, list):
            section_order = []
            for section_order_type_0_item_data in self.section_order:
                section_order_type_0_item: str = section_order_type_0_item_data
                section_order.append(section_order_type_0_item)

        else:
            section_order = self.section_order

        external_domain_names: list[str] | None | Unset
        if isinstance(self.external_domain_names, Unset):
            external_domain_names = UNSET
        elif isinstance(self.external_domain_names, list):
            external_domain_names = self.external_domain_names

        else:
            external_domain_names = self.external_domain_names

        website_url: None | str | Unset
        if isinstance(self.website_url, Unset):
            website_url = UNSET
        else:
            website_url = self.website_url

        website_privacy_url: None | str | Unset
        if isinstance(self.website_privacy_url, Unset):
            website_privacy_url = UNSET
        else:
            website_privacy_url = self.website_privacy_url

        website_support_url: None | str | Unset
        if isinstance(self.website_support_url, Unset):
            website_support_url = UNSET
        else:
            website_support_url = self.website_support_url

        ga_tracking_id: None | str | Unset
        if isinstance(self.ga_tracking_id, Unset):
            ga_tracking_id = UNSET
        else:
            ga_tracking_id = self.ga_tracking_id

        time_zone: None | str | Unset
        if isinstance(self.time_zone, Unset):
            time_zone = UNSET
        else:
            time_zone = self.time_zone

        public: bool | None | Unset
        if isinstance(self.public, Unset):
            public = UNSET
        else:
            public = self.public

        service_ids: list[str] | Unset = UNSET
        if not isinstance(self.service_ids, Unset):
            service_ids = self.service_ids

        functionality_ids: list[str] | Unset = UNSET
        if not isinstance(self.functionality_ids, Unset):
            functionality_ids = self.functionality_ids

        enabled: bool | None | Unset
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if public_title is not UNSET:
            field_dict["public_title"] = public_title
        if description is not UNSET:
            field_dict["description"] = description
        if public_description is not UNSET:
            field_dict["public_description"] = public_description
        if header_color is not UNSET:
            field_dict["header_color"] = header_color
        if footer_color is not UNSET:
            field_dict["footer_color"] = footer_color
        if allow_search_engine_index is not UNSET:
            field_dict["allow_search_engine_index"] = allow_search_engine_index
        if show_uptime is not UNSET:
            field_dict["show_uptime"] = show_uptime
        if show_uptime_last_days is not UNSET:
            field_dict["show_uptime_last_days"] = show_uptime_last_days
        if success_message is not UNSET:
            field_dict["success_message"] = success_message
        if failure_message is not UNSET:
            field_dict["failure_message"] = failure_message
        if authentication_method is not UNSET:
            field_dict["authentication_method"] = authentication_method
        if authentication_enabled is not UNSET:
            field_dict["authentication_enabled"] = authentication_enabled
        if authentication_password is not UNSET:
            field_dict["authentication_password"] = authentication_password
        if saml_idp_sso_service_url is not UNSET:
            field_dict["saml_idp_sso_service_url"] = saml_idp_sso_service_url
        if saml_idp_slo_service_url is not UNSET:
            field_dict["saml_idp_slo_service_url"] = saml_idp_slo_service_url
        if saml_idp_cert is not UNSET:
            field_dict["saml_idp_cert"] = saml_idp_cert
        if saml_name_identifier_format is not UNSET:
            field_dict["saml_name_identifier_format"] = saml_name_identifier_format
        if section_order is not UNSET:
            field_dict["section_order"] = section_order
        if external_domain_names is not UNSET:
            field_dict["external_domain_names"] = external_domain_names
        if website_url is not UNSET:
            field_dict["website_url"] = website_url
        if website_privacy_url is not UNSET:
            field_dict["website_privacy_url"] = website_privacy_url
        if website_support_url is not UNSET:
            field_dict["website_support_url"] = website_support_url
        if ga_tracking_id is not UNSET:
            field_dict["ga_tracking_id"] = ga_tracking_id
        if time_zone is not UNSET:
            field_dict["time_zone"] = time_zone
        if public is not UNSET:
            field_dict["public"] = public
        if service_ids is not UNSET:
            field_dict["service_ids"] = service_ids
        if functionality_ids is not UNSET:
            field_dict["functionality_ids"] = functionality_ids
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title", UNSET)

        def _parse_public_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        public_title = _parse_public_title(d.pop("public_title", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_public_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        public_description = _parse_public_description(d.pop("public_description", UNSET))

        def _parse_header_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        header_color = _parse_header_color(d.pop("header_color", UNSET))

        def _parse_footer_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        footer_color = _parse_footer_color(d.pop("footer_color", UNSET))

        def _parse_allow_search_engine_index(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allow_search_engine_index = _parse_allow_search_engine_index(d.pop("allow_search_engine_index", UNSET))

        def _parse_show_uptime(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        show_uptime = _parse_show_uptime(d.pop("show_uptime", UNSET))

        _show_uptime_last_days = d.pop("show_uptime_last_days", UNSET)
        show_uptime_last_days: UpdateStatusPageDataAttributesShowUptimeLastDays | Unset
        if isinstance(_show_uptime_last_days, Unset):
            show_uptime_last_days = UNSET
        else:
            show_uptime_last_days = check_update_status_page_data_attributes_show_uptime_last_days(
                _show_uptime_last_days
            )

        def _parse_success_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        success_message = _parse_success_message(d.pop("success_message", UNSET))

        def _parse_failure_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        failure_message = _parse_failure_message(d.pop("failure_message", UNSET))

        _authentication_method = d.pop("authentication_method", UNSET)
        authentication_method: UpdateStatusPageDataAttributesAuthenticationMethod | Unset
        if isinstance(_authentication_method, Unset):
            authentication_method = UNSET
        else:
            authentication_method = check_update_status_page_data_attributes_authentication_method(
                _authentication_method
            )

        def _parse_authentication_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        authentication_enabled = _parse_authentication_enabled(d.pop("authentication_enabled", UNSET))

        def _parse_authentication_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        authentication_password = _parse_authentication_password(d.pop("authentication_password", UNSET))

        def _parse_saml_idp_sso_service_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        saml_idp_sso_service_url = _parse_saml_idp_sso_service_url(d.pop("saml_idp_sso_service_url", UNSET))

        def _parse_saml_idp_slo_service_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        saml_idp_slo_service_url = _parse_saml_idp_slo_service_url(d.pop("saml_idp_slo_service_url", UNSET))

        def _parse_saml_idp_cert(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        saml_idp_cert = _parse_saml_idp_cert(d.pop("saml_idp_cert", UNSET))

        _saml_name_identifier_format = d.pop("saml_name_identifier_format", UNSET)
        saml_name_identifier_format: UpdateStatusPageDataAttributesSamlNameIdentifierFormat | Unset
        if isinstance(_saml_name_identifier_format, Unset):
            saml_name_identifier_format = UNSET
        else:
            saml_name_identifier_format = check_update_status_page_data_attributes_saml_name_identifier_format(
                _saml_name_identifier_format
            )

        def _parse_section_order(
            data: object,
        ) -> list[UpdateStatusPageDataAttributesSectionOrderType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                section_order_type_0 = []
                _section_order_type_0 = data
                for section_order_type_0_item_data in _section_order_type_0:
                    section_order_type_0_item = check_update_status_page_data_attributes_section_order_type_0_item(
                        section_order_type_0_item_data
                    )

                    section_order_type_0.append(section_order_type_0_item)

                return section_order_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UpdateStatusPageDataAttributesSectionOrderType0Item] | None | Unset, data)

        section_order = _parse_section_order(d.pop("section_order", UNSET))

        def _parse_external_domain_names(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                external_domain_names_type_0 = cast(list[str], data)

                return external_domain_names_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        external_domain_names = _parse_external_domain_names(d.pop("external_domain_names", UNSET))

        def _parse_website_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website_url = _parse_website_url(d.pop("website_url", UNSET))

        def _parse_website_privacy_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website_privacy_url = _parse_website_privacy_url(d.pop("website_privacy_url", UNSET))

        def _parse_website_support_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website_support_url = _parse_website_support_url(d.pop("website_support_url", UNSET))

        def _parse_ga_tracking_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ga_tracking_id = _parse_ga_tracking_id(d.pop("ga_tracking_id", UNSET))

        def _parse_time_zone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        time_zone = _parse_time_zone(d.pop("time_zone", UNSET))

        def _parse_public(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        public = _parse_public(d.pop("public", UNSET))

        service_ids = cast(list[str], d.pop("service_ids", UNSET))

        functionality_ids = cast(list[str], d.pop("functionality_ids", UNSET))

        def _parse_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))

        update_status_page_data_attributes = cls(
            title=title,
            public_title=public_title,
            description=description,
            public_description=public_description,
            header_color=header_color,
            footer_color=footer_color,
            allow_search_engine_index=allow_search_engine_index,
            show_uptime=show_uptime,
            show_uptime_last_days=show_uptime_last_days,
            success_message=success_message,
            failure_message=failure_message,
            authentication_method=authentication_method,
            authentication_enabled=authentication_enabled,
            authentication_password=authentication_password,
            saml_idp_sso_service_url=saml_idp_sso_service_url,
            saml_idp_slo_service_url=saml_idp_slo_service_url,
            saml_idp_cert=saml_idp_cert,
            saml_name_identifier_format=saml_name_identifier_format,
            section_order=section_order,
            external_domain_names=external_domain_names,
            website_url=website_url,
            website_privacy_url=website_privacy_url,
            website_support_url=website_support_url,
            ga_tracking_id=ga_tracking_id,
            time_zone=time_zone,
            public=public,
            service_ids=service_ids,
            functionality_ids=functionality_ids,
            enabled=enabled,
        )

        return update_status_page_data_attributes
