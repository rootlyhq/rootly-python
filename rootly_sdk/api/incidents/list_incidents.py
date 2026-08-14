from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors_list import ErrorsList
from ...models.incident_list import IncidentList
from ...models.list_incidents_include import ListIncidentsInclude
from ...models.list_incidents_sort import ListIncidentsSort
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    pageafter: Union[Unset, str] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filtersearch: Union[Unset, str] = UNSET,
    filterkind: Union[Unset, str] = UNSET,
    filterstatus: Union[Unset, str] = UNSET,
    filterprivate: Union[Unset, str] = UNSET,
    filteruser_id: Union[Unset, int] = UNSET,
    filterseverity: Union[Unset, str] = UNSET,
    filterseverity_id: Union[Unset, str] = UNSET,
    filterlabels: Union[Unset, str] = UNSET,
    filtertypes: Union[Unset, str] = UNSET,
    filtertype_ids: Union[Unset, str] = UNSET,
    filterenvironments: Union[Unset, str] = UNSET,
    filterenvironment_ids: Union[Unset, str] = UNSET,
    filterfunctionalities: Union[Unset, str] = UNSET,
    filterfunctionality_ids: Union[Unset, str] = UNSET,
    filterfunctionality_names: Union[Unset, str] = UNSET,
    filterservices: Union[Unset, str] = UNSET,
    filterservice_ids: Union[Unset, str] = UNSET,
    filterservice_names: Union[Unset, str] = UNSET,
    filterteams: Union[Unset, str] = UNSET,
    filterteam_ids: Union[Unset, str] = UNSET,
    filterteam_names: Union[Unset, str] = UNSET,
    filtercause: Union[Unset, str] = UNSET,
    filtercause_ids: Union[Unset, str] = UNSET,
    filtercustom_field_selected_option_ids: Union[Unset, str] = UNSET,
    filterslack_channel_id: Union[Unset, str] = UNSET,
    filtersequential_id: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
    filterupdated_atgt: Union[Unset, str] = UNSET,
    filterupdated_atgte: Union[Unset, str] = UNSET,
    filterupdated_atlt: Union[Unset, str] = UNSET,
    filterupdated_atlte: Union[Unset, str] = UNSET,
    filterstarted_atgt: Union[Unset, str] = UNSET,
    filterstarted_atgte: Union[Unset, str] = UNSET,
    filterstarted_atlt: Union[Unset, str] = UNSET,
    filterstarted_atlte: Union[Unset, str] = UNSET,
    filterdetected_atgt: Union[Unset, str] = UNSET,
    filterdetected_atgte: Union[Unset, str] = UNSET,
    filterdetected_atlt: Union[Unset, str] = UNSET,
    filterdetected_atlte: Union[Unset, str] = UNSET,
    filteracknowledged_atgt: Union[Unset, str] = UNSET,
    filteracknowledged_atgte: Union[Unset, str] = UNSET,
    filteracknowledged_atlt: Union[Unset, str] = UNSET,
    filteracknowledged_atlte: Union[Unset, str] = UNSET,
    filtermitigated_atgt: Union[Unset, str] = UNSET,
    filtermitigated_atgte: Union[Unset, str] = UNSET,
    filtermitigated_atlt: Union[Unset, str] = UNSET,
    filtermitigated_atlte: Union[Unset, str] = UNSET,
    filterresolved_atgt: Union[Unset, str] = UNSET,
    filterresolved_atgte: Union[Unset, str] = UNSET,
    filterresolved_atlt: Union[Unset, str] = UNSET,
    filterresolved_atlte: Union[Unset, str] = UNSET,
    filterclosed_atgt: Union[Unset, str] = UNSET,
    filterclosed_atgte: Union[Unset, str] = UNSET,
    filterclosed_atlt: Union[Unset, str] = UNSET,
    filterclosed_atlte: Union[Unset, str] = UNSET,
    filterin_triage_atgt: Union[Unset, str] = UNSET,
    filterin_triage_atgte: Union[Unset, str] = UNSET,
    filterin_triage_atlt: Union[Unset, str] = UNSET,
    filterin_triage_atlte: Union[Unset, str] = UNSET,
    filterkindeq: Union[Unset, str] = UNSET,
    filterkindnot_eq: Union[Unset, str] = UNSET,
    filterkindin: Union[Unset, str] = UNSET,
    filterkindnot_in: Union[Unset, str] = UNSET,
    filterstatuseq: Union[Unset, str] = UNSET,
    filterstatusnot_eq: Union[Unset, str] = UNSET,
    filterstatusin: Union[Unset, str] = UNSET,
    filterstatusnot_in: Union[Unset, str] = UNSET,
    filterprivateeq: Union[Unset, str] = UNSET,
    filterprivatenot_eq: Union[Unset, str] = UNSET,
    filterprivatein: Union[Unset, str] = UNSET,
    filterprivatenot_in: Union[Unset, str] = UNSET,
    filteruser_ideq: Union[Unset, str] = UNSET,
    filteruser_idnot_eq: Union[Unset, str] = UNSET,
    filteruser_idin: Union[Unset, str] = UNSET,
    filteruser_idnot_in: Union[Unset, str] = UNSET,
    filterseverityeq: Union[Unset, str] = UNSET,
    filterseveritynot_eq: Union[Unset, str] = UNSET,
    filterseverityin: Union[Unset, str] = UNSET,
    filterseveritynot_in: Union[Unset, str] = UNSET,
    filterseverity_ideq: Union[Unset, str] = UNSET,
    filterseverity_idnot_eq: Union[Unset, str] = UNSET,
    filterseverity_idin: Union[Unset, str] = UNSET,
    filterseverity_idnot_in: Union[Unset, str] = UNSET,
    filterlabelseq: Union[Unset, str] = UNSET,
    filterlabelsnot_eq: Union[Unset, str] = UNSET,
    filterlabelsin: Union[Unset, str] = UNSET,
    filterlabelsnot_in: Union[Unset, str] = UNSET,
    filterzendesk_ticket_ideq: Union[Unset, str] = UNSET,
    filterzendesk_ticket_idnot_eq: Union[Unset, str] = UNSET,
    filterzendesk_ticket_idin: Union[Unset, str] = UNSET,
    filterzendesk_ticket_idnot_in: Union[Unset, str] = UNSET,
    filtersequential_ideq: Union[Unset, str] = UNSET,
    filtersequential_idnot_eq: Union[Unset, str] = UNSET,
    filtersequential_idin: Union[Unset, str] = UNSET,
    filtersequential_idnot_in: Union[Unset, str] = UNSET,
    filtertypeseq: Union[Unset, str] = UNSET,
    filtertypesnot_eq: Union[Unset, str] = UNSET,
    filtertypesin: Union[Unset, str] = UNSET,
    filtertypesnot_in: Union[Unset, str] = UNSET,
    filtertype_idseq: Union[Unset, str] = UNSET,
    filtertype_idsnot_eq: Union[Unset, str] = UNSET,
    filtertype_idsin: Union[Unset, str] = UNSET,
    filtertype_idsnot_in: Union[Unset, str] = UNSET,
    filterenvironmentseq: Union[Unset, str] = UNSET,
    filterenvironmentsnot_eq: Union[Unset, str] = UNSET,
    filterenvironmentsin: Union[Unset, str] = UNSET,
    filterenvironmentsnot_in: Union[Unset, str] = UNSET,
    filterenvironment_idseq: Union[Unset, str] = UNSET,
    filterenvironment_idsnot_eq: Union[Unset, str] = UNSET,
    filterenvironment_idsin: Union[Unset, str] = UNSET,
    filterenvironment_idsnot_in: Union[Unset, str] = UNSET,
    filterserviceseq: Union[Unset, str] = UNSET,
    filterservicesnot_eq: Union[Unset, str] = UNSET,
    filterservicesin: Union[Unset, str] = UNSET,
    filterservicesnot_in: Union[Unset, str] = UNSET,
    filterservice_idseq: Union[Unset, str] = UNSET,
    filterservice_idsnot_eq: Union[Unset, str] = UNSET,
    filterservice_idsin: Union[Unset, str] = UNSET,
    filterservice_idsnot_in: Union[Unset, str] = UNSET,
    filterservice_nameseq: Union[Unset, str] = UNSET,
    filterservice_namesnot_eq: Union[Unset, str] = UNSET,
    filterservice_namesin: Union[Unset, str] = UNSET,
    filterservice_namesnot_in: Union[Unset, str] = UNSET,
    filterfunctionalitieseq: Union[Unset, str] = UNSET,
    filterfunctionalitiesnot_eq: Union[Unset, str] = UNSET,
    filterfunctionalitiesin: Union[Unset, str] = UNSET,
    filterfunctionalitiesnot_in: Union[Unset, str] = UNSET,
    filterfunctionality_idseq: Union[Unset, str] = UNSET,
    filterfunctionality_idsnot_eq: Union[Unset, str] = UNSET,
    filterfunctionality_idsin: Union[Unset, str] = UNSET,
    filterfunctionality_idsnot_in: Union[Unset, str] = UNSET,
    filterfunctionality_nameseq: Union[Unset, str] = UNSET,
    filterfunctionality_namesnot_eq: Union[Unset, str] = UNSET,
    filterfunctionality_namesin: Union[Unset, str] = UNSET,
    filterfunctionality_namesnot_in: Union[Unset, str] = UNSET,
    filtercauseseq: Union[Unset, str] = UNSET,
    filtercausesnot_eq: Union[Unset, str] = UNSET,
    filtercausesin: Union[Unset, str] = UNSET,
    filtercausesnot_in: Union[Unset, str] = UNSET,
    filtercause_idseq: Union[Unset, str] = UNSET,
    filtercause_idsnot_eq: Union[Unset, str] = UNSET,
    filtercause_idsin: Union[Unset, str] = UNSET,
    filtercause_idsnot_in: Union[Unset, str] = UNSET,
    filterteamseq: Union[Unset, str] = UNSET,
    filterteamsnot_eq: Union[Unset, str] = UNSET,
    filterteamsin: Union[Unset, str] = UNSET,
    filterteamsnot_in: Union[Unset, str] = UNSET,
    filterteam_idseq: Union[Unset, str] = UNSET,
    filterteam_idsnot_eq: Union[Unset, str] = UNSET,
    filterteam_idsin: Union[Unset, str] = UNSET,
    filterteam_idsnot_in: Union[Unset, str] = UNSET,
    filterteam_nameseq: Union[Unset, str] = UNSET,
    filterteam_namesnot_eq: Union[Unset, str] = UNSET,
    filterteam_namesin: Union[Unset, str] = UNSET,
    filterteam_namesnot_in: Union[Unset, str] = UNSET,
    sort: Union[Unset, ListIncidentsSort] = UNSET,
    include: Union[Unset, ListIncidentsInclude] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page[after]"] = pageafter

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize

    params["filter[search]"] = filtersearch

    params["filter[kind]"] = filterkind

    params["filter[status]"] = filterstatus

    params["filter[private]"] = filterprivate

    params["filter[user_id]"] = filteruser_id

    params["filter[severity]"] = filterseverity

    params["filter[severity_id]"] = filterseverity_id

    params["filter[labels]"] = filterlabels

    params["filter[types]"] = filtertypes

    params["filter[type_ids]"] = filtertype_ids

    params["filter[environments]"] = filterenvironments

    params["filter[environment_ids]"] = filterenvironment_ids

    params["filter[functionalities]"] = filterfunctionalities

    params["filter[functionality_ids]"] = filterfunctionality_ids

    params["filter[functionality_names]"] = filterfunctionality_names

    params["filter[services]"] = filterservices

    params["filter[service_ids]"] = filterservice_ids

    params["filter[service_names]"] = filterservice_names

    params["filter[teams]"] = filterteams

    params["filter[team_ids]"] = filterteam_ids

    params["filter[team_names]"] = filterteam_names

    params["filter[cause]"] = filtercause

    params["filter[cause_ids]"] = filtercause_ids

    params["filter[custom_field_selected_option_ids]"] = filtercustom_field_selected_option_ids

    params["filter[slack_channel_id]"] = filterslack_channel_id

    params["filter[sequential_id]"] = filtersequential_id

    params["filter[created_at][gt]"] = filtercreated_atgt

    params["filter[created_at][gte]"] = filtercreated_atgte

    params["filter[created_at][lt]"] = filtercreated_atlt

    params["filter[created_at][lte]"] = filtercreated_atlte

    params["filter[updated_at][gt]"] = filterupdated_atgt

    params["filter[updated_at][gte]"] = filterupdated_atgte

    params["filter[updated_at][lt]"] = filterupdated_atlt

    params["filter[updated_at][lte]"] = filterupdated_atlte

    params["filter[started_at][gt]"] = filterstarted_atgt

    params["filter[started_at][gte]"] = filterstarted_atgte

    params["filter[started_at][lt]"] = filterstarted_atlt

    params["filter[started_at][lte]"] = filterstarted_atlte

    params["filter[detected_at][gt]"] = filterdetected_atgt

    params["filter[detected_at][gte]"] = filterdetected_atgte

    params["filter[detected_at][lt]"] = filterdetected_atlt

    params["filter[detected_at][lte]"] = filterdetected_atlte

    params["filter[acknowledged_at][gt]"] = filteracknowledged_atgt

    params["filter[acknowledged_at][gte]"] = filteracknowledged_atgte

    params["filter[acknowledged_at][lt]"] = filteracknowledged_atlt

    params["filter[acknowledged_at][lte]"] = filteracknowledged_atlte

    params["filter[mitigated_at][gt]"] = filtermitigated_atgt

    params["filter[mitigated_at][gte]"] = filtermitigated_atgte

    params["filter[mitigated_at][lt]"] = filtermitigated_atlt

    params["filter[mitigated_at][lte]"] = filtermitigated_atlte

    params["filter[resolved_at][gt]"] = filterresolved_atgt

    params["filter[resolved_at][gte]"] = filterresolved_atgte

    params["filter[resolved_at][lt]"] = filterresolved_atlt

    params["filter[resolved_at][lte]"] = filterresolved_atlte

    params["filter[closed_at][gt]"] = filterclosed_atgt

    params["filter[closed_at][gte]"] = filterclosed_atgte

    params["filter[closed_at][lt]"] = filterclosed_atlt

    params["filter[closed_at][lte]"] = filterclosed_atlte

    params["filter[in_triage_at][gt]"] = filterin_triage_atgt

    params["filter[in_triage_at][gte]"] = filterin_triage_atgte

    params["filter[in_triage_at][lt]"] = filterin_triage_atlt

    params["filter[in_triage_at][lte]"] = filterin_triage_atlte

    params["filter[kind][eq]"] = filterkindeq

    params["filter[kind][not_eq]"] = filterkindnot_eq

    params["filter[kind][in]"] = filterkindin

    params["filter[kind][not_in]"] = filterkindnot_in

    params["filter[status][eq]"] = filterstatuseq

    params["filter[status][not_eq]"] = filterstatusnot_eq

    params["filter[status][in]"] = filterstatusin

    params["filter[status][not_in]"] = filterstatusnot_in

    params["filter[private][eq]"] = filterprivateeq

    params["filter[private][not_eq]"] = filterprivatenot_eq

    params["filter[private][in]"] = filterprivatein

    params["filter[private][not_in]"] = filterprivatenot_in

    params["filter[user_id][eq]"] = filteruser_ideq

    params["filter[user_id][not_eq]"] = filteruser_idnot_eq

    params["filter[user_id][in]"] = filteruser_idin

    params["filter[user_id][not_in]"] = filteruser_idnot_in

    params["filter[severity][eq]"] = filterseverityeq

    params["filter[severity][not_eq]"] = filterseveritynot_eq

    params["filter[severity][in]"] = filterseverityin

    params["filter[severity][not_in]"] = filterseveritynot_in

    params["filter[severity_id][eq]"] = filterseverity_ideq

    params["filter[severity_id][not_eq]"] = filterseverity_idnot_eq

    params["filter[severity_id][in]"] = filterseverity_idin

    params["filter[severity_id][not_in]"] = filterseverity_idnot_in

    params["filter[labels][eq]"] = filterlabelseq

    params["filter[labels][not_eq]"] = filterlabelsnot_eq

    params["filter[labels][in]"] = filterlabelsin

    params["filter[labels][not_in]"] = filterlabelsnot_in

    params["filter[zendesk_ticket_id][eq]"] = filterzendesk_ticket_ideq

    params["filter[zendesk_ticket_id][not_eq]"] = filterzendesk_ticket_idnot_eq

    params["filter[zendesk_ticket_id][in]"] = filterzendesk_ticket_idin

    params["filter[zendesk_ticket_id][not_in]"] = filterzendesk_ticket_idnot_in

    params["filter[sequential_id][eq]"] = filtersequential_ideq

    params["filter[sequential_id][not_eq]"] = filtersequential_idnot_eq

    params["filter[sequential_id][in]"] = filtersequential_idin

    params["filter[sequential_id][not_in]"] = filtersequential_idnot_in

    params["filter[types][eq]"] = filtertypeseq

    params["filter[types][not_eq]"] = filtertypesnot_eq

    params["filter[types][in]"] = filtertypesin

    params["filter[types][not_in]"] = filtertypesnot_in

    params["filter[type_ids][eq]"] = filtertype_idseq

    params["filter[type_ids][not_eq]"] = filtertype_idsnot_eq

    params["filter[type_ids][in]"] = filtertype_idsin

    params["filter[type_ids][not_in]"] = filtertype_idsnot_in

    params["filter[environments][eq]"] = filterenvironmentseq

    params["filter[environments][not_eq]"] = filterenvironmentsnot_eq

    params["filter[environments][in]"] = filterenvironmentsin

    params["filter[environments][not_in]"] = filterenvironmentsnot_in

    params["filter[environment_ids][eq]"] = filterenvironment_idseq

    params["filter[environment_ids][not_eq]"] = filterenvironment_idsnot_eq

    params["filter[environment_ids][in]"] = filterenvironment_idsin

    params["filter[environment_ids][not_in]"] = filterenvironment_idsnot_in

    params["filter[services][eq]"] = filterserviceseq

    params["filter[services][not_eq]"] = filterservicesnot_eq

    params["filter[services][in]"] = filterservicesin

    params["filter[services][not_in]"] = filterservicesnot_in

    params["filter[service_ids][eq]"] = filterservice_idseq

    params["filter[service_ids][not_eq]"] = filterservice_idsnot_eq

    params["filter[service_ids][in]"] = filterservice_idsin

    params["filter[service_ids][not_in]"] = filterservice_idsnot_in

    params["filter[service_names][eq]"] = filterservice_nameseq

    params["filter[service_names][not_eq]"] = filterservice_namesnot_eq

    params["filter[service_names][in]"] = filterservice_namesin

    params["filter[service_names][not_in]"] = filterservice_namesnot_in

    params["filter[functionalities][eq]"] = filterfunctionalitieseq

    params["filter[functionalities][not_eq]"] = filterfunctionalitiesnot_eq

    params["filter[functionalities][in]"] = filterfunctionalitiesin

    params["filter[functionalities][not_in]"] = filterfunctionalitiesnot_in

    params["filter[functionality_ids][eq]"] = filterfunctionality_idseq

    params["filter[functionality_ids][not_eq]"] = filterfunctionality_idsnot_eq

    params["filter[functionality_ids][in]"] = filterfunctionality_idsin

    params["filter[functionality_ids][not_in]"] = filterfunctionality_idsnot_in

    params["filter[functionality_names][eq]"] = filterfunctionality_nameseq

    params["filter[functionality_names][not_eq]"] = filterfunctionality_namesnot_eq

    params["filter[functionality_names][in]"] = filterfunctionality_namesin

    params["filter[functionality_names][not_in]"] = filterfunctionality_namesnot_in

    params["filter[causes][eq]"] = filtercauseseq

    params["filter[causes][not_eq]"] = filtercausesnot_eq

    params["filter[causes][in]"] = filtercausesin

    params["filter[causes][not_in]"] = filtercausesnot_in

    params["filter[cause_ids][eq]"] = filtercause_idseq

    params["filter[cause_ids][not_eq]"] = filtercause_idsnot_eq

    params["filter[cause_ids][in]"] = filtercause_idsin

    params["filter[cause_ids][not_in]"] = filtercause_idsnot_in

    params["filter[teams][eq]"] = filterteamseq

    params["filter[teams][not_eq]"] = filterteamsnot_eq

    params["filter[teams][in]"] = filterteamsin

    params["filter[teams][not_in]"] = filterteamsnot_in

    params["filter[team_ids][eq]"] = filterteam_idseq

    params["filter[team_ids][not_eq]"] = filterteam_idsnot_eq

    params["filter[team_ids][in]"] = filterteam_idsin

    params["filter[team_ids][not_in]"] = filterteam_idsnot_in

    params["filter[team_names][eq]"] = filterteam_nameseq

    params["filter[team_names][not_eq]"] = filterteam_namesnot_eq

    params["filter[team_names][in]"] = filterteam_namesin

    params["filter[team_names][not_in]"] = filterteam_namesnot_in

    json_sort: Union[Unset, str] = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort

    params["sort"] = json_sort

    json_include: Union[Unset, str] = UNSET
    if not isinstance(include, Unset):
        json_include = include

    params["include"] = json_include

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/incidents",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorsList, IncidentList]]:
    if response.status_code == 200:
        response_200 = IncidentList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorsList.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorsList, IncidentList]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    pageafter: Union[Unset, str] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filtersearch: Union[Unset, str] = UNSET,
    filterkind: Union[Unset, str] = UNSET,
    filterstatus: Union[Unset, str] = UNSET,
    filterprivate: Union[Unset, str] = UNSET,
    filteruser_id: Union[Unset, int] = UNSET,
    filterseverity: Union[Unset, str] = UNSET,
    filterseverity_id: Union[Unset, str] = UNSET,
    filterlabels: Union[Unset, str] = UNSET,
    filtertypes: Union[Unset, str] = UNSET,
    filtertype_ids: Union[Unset, str] = UNSET,
    filterenvironments: Union[Unset, str] = UNSET,
    filterenvironment_ids: Union[Unset, str] = UNSET,
    filterfunctionalities: Union[Unset, str] = UNSET,
    filterfunctionality_ids: Union[Unset, str] = UNSET,
    filterfunctionality_names: Union[Unset, str] = UNSET,
    filterservices: Union[Unset, str] = UNSET,
    filterservice_ids: Union[Unset, str] = UNSET,
    filterservice_names: Union[Unset, str] = UNSET,
    filterteams: Union[Unset, str] = UNSET,
    filterteam_ids: Union[Unset, str] = UNSET,
    filterteam_names: Union[Unset, str] = UNSET,
    filtercause: Union[Unset, str] = UNSET,
    filtercause_ids: Union[Unset, str] = UNSET,
    filtercustom_field_selected_option_ids: Union[Unset, str] = UNSET,
    filterslack_channel_id: Union[Unset, str] = UNSET,
    filtersequential_id: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
    filterupdated_atgt: Union[Unset, str] = UNSET,
    filterupdated_atgte: Union[Unset, str] = UNSET,
    filterupdated_atlt: Union[Unset, str] = UNSET,
    filterupdated_atlte: Union[Unset, str] = UNSET,
    filterstarted_atgt: Union[Unset, str] = UNSET,
    filterstarted_atgte: Union[Unset, str] = UNSET,
    filterstarted_atlt: Union[Unset, str] = UNSET,
    filterstarted_atlte: Union[Unset, str] = UNSET,
    filterdetected_atgt: Union[Unset, str] = UNSET,
    filterdetected_atgte: Union[Unset, str] = UNSET,
    filterdetected_atlt: Union[Unset, str] = UNSET,
    filterdetected_atlte: Union[Unset, str] = UNSET,
    filteracknowledged_atgt: Union[Unset, str] = UNSET,
    filteracknowledged_atgte: Union[Unset, str] = UNSET,
    filteracknowledged_atlt: Union[Unset, str] = UNSET,
    filteracknowledged_atlte: Union[Unset, str] = UNSET,
    filtermitigated_atgt: Union[Unset, str] = UNSET,
    filtermitigated_atgte: Union[Unset, str] = UNSET,
    filtermitigated_atlt: Union[Unset, str] = UNSET,
    filtermitigated_atlte: Union[Unset, str] = UNSET,
    filterresolved_atgt: Union[Unset, str] = UNSET,
    filterresolved_atgte: Union[Unset, str] = UNSET,
    filterresolved_atlt: Union[Unset, str] = UNSET,
    filterresolved_atlte: Union[Unset, str] = UNSET,
    filterclosed_atgt: Union[Unset, str] = UNSET,
    filterclosed_atgte: Union[Unset, str] = UNSET,
    filterclosed_atlt: Union[Unset, str] = UNSET,
    filterclosed_atlte: Union[Unset, str] = UNSET,
    filterin_triage_atgt: Union[Unset, str] = UNSET,
    filterin_triage_atgte: Union[Unset, str] = UNSET,
    filterin_triage_atlt: Union[Unset, str] = UNSET,
    filterin_triage_atlte: Union[Unset, str] = UNSET,
    filterkindeq: Union[Unset, str] = UNSET,
    filterkindnot_eq: Union[Unset, str] = UNSET,
    filterkindin: Union[Unset, str] = UNSET,
    filterkindnot_in: Union[Unset, str] = UNSET,
    filterstatuseq: Union[Unset, str] = UNSET,
    filterstatusnot_eq: Union[Unset, str] = UNSET,
    filterstatusin: Union[Unset, str] = UNSET,
    filterstatusnot_in: Union[Unset, str] = UNSET,
    filterprivateeq: Union[Unset, str] = UNSET,
    filterprivatenot_eq: Union[Unset, str] = UNSET,
    filterprivatein: Union[Unset, str] = UNSET,
    filterprivatenot_in: Union[Unset, str] = UNSET,
    filteruser_ideq: Union[Unset, str] = UNSET,
    filteruser_idnot_eq: Union[Unset, str] = UNSET,
    filteruser_idin: Union[Unset, str] = UNSET,
    filteruser_idnot_in: Union[Unset, str] = UNSET,
    filterseverityeq: Union[Unset, str] = UNSET,
    filterseveritynot_eq: Union[Unset, str] = UNSET,
    filterseverityin: Union[Unset, str] = UNSET,
    filterseveritynot_in: Union[Unset, str] = UNSET,
    filterseverity_ideq: Union[Unset, str] = UNSET,
    filterseverity_idnot_eq: Union[Unset, str] = UNSET,
    filterseverity_idin: Union[Unset, str] = UNSET,
    filterseverity_idnot_in: Union[Unset, str] = UNSET,
    filterlabelseq: Union[Unset, str] = UNSET,
    filterlabelsnot_eq: Union[Unset, str] = UNSET,
    filterlabelsin: Union[Unset, str] = UNSET,
    filterlabelsnot_in: Union[Unset, str] = UNSET,
    filterzendesk_ticket_ideq: Union[Unset, str] = UNSET,
    filterzendesk_ticket_idnot_eq: Union[Unset, str] = UNSET,
    filterzendesk_ticket_idin: Union[Unset, str] = UNSET,
    filterzendesk_ticket_idnot_in: Union[Unset, str] = UNSET,
    filtersequential_ideq: Union[Unset, str] = UNSET,
    filtersequential_idnot_eq: Union[Unset, str] = UNSET,
    filtersequential_idin: Union[Unset, str] = UNSET,
    filtersequential_idnot_in: Union[Unset, str] = UNSET,
    filtertypeseq: Union[Unset, str] = UNSET,
    filtertypesnot_eq: Union[Unset, str] = UNSET,
    filtertypesin: Union[Unset, str] = UNSET,
    filtertypesnot_in: Union[Unset, str] = UNSET,
    filtertype_idseq: Union[Unset, str] = UNSET,
    filtertype_idsnot_eq: Union[Unset, str] = UNSET,
    filtertype_idsin: Union[Unset, str] = UNSET,
    filtertype_idsnot_in: Union[Unset, str] = UNSET,
    filterenvironmentseq: Union[Unset, str] = UNSET,
    filterenvironmentsnot_eq: Union[Unset, str] = UNSET,
    filterenvironmentsin: Union[Unset, str] = UNSET,
    filterenvironmentsnot_in: Union[Unset, str] = UNSET,
    filterenvironment_idseq: Union[Unset, str] = UNSET,
    filterenvironment_idsnot_eq: Union[Unset, str] = UNSET,
    filterenvironment_idsin: Union[Unset, str] = UNSET,
    filterenvironment_idsnot_in: Union[Unset, str] = UNSET,
    filterserviceseq: Union[Unset, str] = UNSET,
    filterservicesnot_eq: Union[Unset, str] = UNSET,
    filterservicesin: Union[Unset, str] = UNSET,
    filterservicesnot_in: Union[Unset, str] = UNSET,
    filterservice_idseq: Union[Unset, str] = UNSET,
    filterservice_idsnot_eq: Union[Unset, str] = UNSET,
    filterservice_idsin: Union[Unset, str] = UNSET,
    filterservice_idsnot_in: Union[Unset, str] = UNSET,
    filterservice_nameseq: Union[Unset, str] = UNSET,
    filterservice_namesnot_eq: Union[Unset, str] = UNSET,
    filterservice_namesin: Union[Unset, str] = UNSET,
    filterservice_namesnot_in: Union[Unset, str] = UNSET,
    filterfunctionalitieseq: Union[Unset, str] = UNSET,
    filterfunctionalitiesnot_eq: Union[Unset, str] = UNSET,
    filterfunctionalitiesin: Union[Unset, str] = UNSET,
    filterfunctionalitiesnot_in: Union[Unset, str] = UNSET,
    filterfunctionality_idseq: Union[Unset, str] = UNSET,
    filterfunctionality_idsnot_eq: Union[Unset, str] = UNSET,
    filterfunctionality_idsin: Union[Unset, str] = UNSET,
    filterfunctionality_idsnot_in: Union[Unset, str] = UNSET,
    filterfunctionality_nameseq: Union[Unset, str] = UNSET,
    filterfunctionality_namesnot_eq: Union[Unset, str] = UNSET,
    filterfunctionality_namesin: Union[Unset, str] = UNSET,
    filterfunctionality_namesnot_in: Union[Unset, str] = UNSET,
    filtercauseseq: Union[Unset, str] = UNSET,
    filtercausesnot_eq: Union[Unset, str] = UNSET,
    filtercausesin: Union[Unset, str] = UNSET,
    filtercausesnot_in: Union[Unset, str] = UNSET,
    filtercause_idseq: Union[Unset, str] = UNSET,
    filtercause_idsnot_eq: Union[Unset, str] = UNSET,
    filtercause_idsin: Union[Unset, str] = UNSET,
    filtercause_idsnot_in: Union[Unset, str] = UNSET,
    filterteamseq: Union[Unset, str] = UNSET,
    filterteamsnot_eq: Union[Unset, str] = UNSET,
    filterteamsin: Union[Unset, str] = UNSET,
    filterteamsnot_in: Union[Unset, str] = UNSET,
    filterteam_idseq: Union[Unset, str] = UNSET,
    filterteam_idsnot_eq: Union[Unset, str] = UNSET,
    filterteam_idsin: Union[Unset, str] = UNSET,
    filterteam_idsnot_in: Union[Unset, str] = UNSET,
    filterteam_nameseq: Union[Unset, str] = UNSET,
    filterteam_namesnot_eq: Union[Unset, str] = UNSET,
    filterteam_namesin: Union[Unset, str] = UNSET,
    filterteam_namesnot_in: Union[Unset, str] = UNSET,
    sort: Union[Unset, ListIncidentsSort] = UNSET,
    include: Union[Unset, ListIncidentsInclude] = UNSET,
) -> Response[Union[ErrorsList, IncidentList]]:
    """List incidents

     List incidents

    Args:
        pageafter (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtersearch (Union[Unset, str]):
        filterkind (Union[Unset, str]):
        filterstatus (Union[Unset, str]):
        filterprivate (Union[Unset, str]):
        filteruser_id (Union[Unset, int]):
        filterseverity (Union[Unset, str]):
        filterseverity_id (Union[Unset, str]):
        filterlabels (Union[Unset, str]):
        filtertypes (Union[Unset, str]):
        filtertype_ids (Union[Unset, str]):
        filterenvironments (Union[Unset, str]):
        filterenvironment_ids (Union[Unset, str]):
        filterfunctionalities (Union[Unset, str]):
        filterfunctionality_ids (Union[Unset, str]):
        filterfunctionality_names (Union[Unset, str]):
        filterservices (Union[Unset, str]):
        filterservice_ids (Union[Unset, str]):
        filterservice_names (Union[Unset, str]):
        filterteams (Union[Unset, str]):
        filterteam_ids (Union[Unset, str]):
        filterteam_names (Union[Unset, str]):
        filtercause (Union[Unset, str]):
        filtercause_ids (Union[Unset, str]):
        filtercustom_field_selected_option_ids (Union[Unset, str]):
        filterslack_channel_id (Union[Unset, str]):
        filtersequential_id (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        filterupdated_atgt (Union[Unset, str]):
        filterupdated_atgte (Union[Unset, str]):
        filterupdated_atlt (Union[Unset, str]):
        filterupdated_atlte (Union[Unset, str]):
        filterstarted_atgt (Union[Unset, str]):
        filterstarted_atgte (Union[Unset, str]):
        filterstarted_atlt (Union[Unset, str]):
        filterstarted_atlte (Union[Unset, str]):
        filterdetected_atgt (Union[Unset, str]):
        filterdetected_atgte (Union[Unset, str]):
        filterdetected_atlt (Union[Unset, str]):
        filterdetected_atlte (Union[Unset, str]):
        filteracknowledged_atgt (Union[Unset, str]):
        filteracknowledged_atgte (Union[Unset, str]):
        filteracknowledged_atlt (Union[Unset, str]):
        filteracknowledged_atlte (Union[Unset, str]):
        filtermitigated_atgt (Union[Unset, str]):
        filtermitigated_atgte (Union[Unset, str]):
        filtermitigated_atlt (Union[Unset, str]):
        filtermitigated_atlte (Union[Unset, str]):
        filterresolved_atgt (Union[Unset, str]):
        filterresolved_atgte (Union[Unset, str]):
        filterresolved_atlt (Union[Unset, str]):
        filterresolved_atlte (Union[Unset, str]):
        filterclosed_atgt (Union[Unset, str]):
        filterclosed_atgte (Union[Unset, str]):
        filterclosed_atlt (Union[Unset, str]):
        filterclosed_atlte (Union[Unset, str]):
        filterin_triage_atgt (Union[Unset, str]):
        filterin_triage_atgte (Union[Unset, str]):
        filterin_triage_atlt (Union[Unset, str]):
        filterin_triage_atlte (Union[Unset, str]):
        filterkindeq (Union[Unset, str]):
        filterkindnot_eq (Union[Unset, str]):
        filterkindin (Union[Unset, str]):
        filterkindnot_in (Union[Unset, str]):
        filterstatuseq (Union[Unset, str]):
        filterstatusnot_eq (Union[Unset, str]):
        filterstatusin (Union[Unset, str]):
        filterstatusnot_in (Union[Unset, str]):
        filterprivateeq (Union[Unset, str]):
        filterprivatenot_eq (Union[Unset, str]):
        filterprivatein (Union[Unset, str]):
        filterprivatenot_in (Union[Unset, str]):
        filteruser_ideq (Union[Unset, str]):
        filteruser_idnot_eq (Union[Unset, str]):
        filteruser_idin (Union[Unset, str]):
        filteruser_idnot_in (Union[Unset, str]):
        filterseverityeq (Union[Unset, str]):
        filterseveritynot_eq (Union[Unset, str]):
        filterseverityin (Union[Unset, str]):
        filterseveritynot_in (Union[Unset, str]):
        filterseverity_ideq (Union[Unset, str]):
        filterseverity_idnot_eq (Union[Unset, str]):
        filterseverity_idin (Union[Unset, str]):
        filterseverity_idnot_in (Union[Unset, str]):
        filterlabelseq (Union[Unset, str]):
        filterlabelsnot_eq (Union[Unset, str]):
        filterlabelsin (Union[Unset, str]):
        filterlabelsnot_in (Union[Unset, str]):
        filterzendesk_ticket_ideq (Union[Unset, str]):
        filterzendesk_ticket_idnot_eq (Union[Unset, str]):
        filterzendesk_ticket_idin (Union[Unset, str]):
        filterzendesk_ticket_idnot_in (Union[Unset, str]):
        filtersequential_ideq (Union[Unset, str]):
        filtersequential_idnot_eq (Union[Unset, str]):
        filtersequential_idin (Union[Unset, str]):
        filtersequential_idnot_in (Union[Unset, str]):
        filtertypeseq (Union[Unset, str]):
        filtertypesnot_eq (Union[Unset, str]):
        filtertypesin (Union[Unset, str]):
        filtertypesnot_in (Union[Unset, str]):
        filtertype_idseq (Union[Unset, str]):
        filtertype_idsnot_eq (Union[Unset, str]):
        filtertype_idsin (Union[Unset, str]):
        filtertype_idsnot_in (Union[Unset, str]):
        filterenvironmentseq (Union[Unset, str]):
        filterenvironmentsnot_eq (Union[Unset, str]):
        filterenvironmentsin (Union[Unset, str]):
        filterenvironmentsnot_in (Union[Unset, str]):
        filterenvironment_idseq (Union[Unset, str]):
        filterenvironment_idsnot_eq (Union[Unset, str]):
        filterenvironment_idsin (Union[Unset, str]):
        filterenvironment_idsnot_in (Union[Unset, str]):
        filterserviceseq (Union[Unset, str]):
        filterservicesnot_eq (Union[Unset, str]):
        filterservicesin (Union[Unset, str]):
        filterservicesnot_in (Union[Unset, str]):
        filterservice_idseq (Union[Unset, str]):
        filterservice_idsnot_eq (Union[Unset, str]):
        filterservice_idsin (Union[Unset, str]):
        filterservice_idsnot_in (Union[Unset, str]):
        filterservice_nameseq (Union[Unset, str]):
        filterservice_namesnot_eq (Union[Unset, str]):
        filterservice_namesin (Union[Unset, str]):
        filterservice_namesnot_in (Union[Unset, str]):
        filterfunctionalitieseq (Union[Unset, str]):
        filterfunctionalitiesnot_eq (Union[Unset, str]):
        filterfunctionalitiesin (Union[Unset, str]):
        filterfunctionalitiesnot_in (Union[Unset, str]):
        filterfunctionality_idseq (Union[Unset, str]):
        filterfunctionality_idsnot_eq (Union[Unset, str]):
        filterfunctionality_idsin (Union[Unset, str]):
        filterfunctionality_idsnot_in (Union[Unset, str]):
        filterfunctionality_nameseq (Union[Unset, str]):
        filterfunctionality_namesnot_eq (Union[Unset, str]):
        filterfunctionality_namesin (Union[Unset, str]):
        filterfunctionality_namesnot_in (Union[Unset, str]):
        filtercauseseq (Union[Unset, str]):
        filtercausesnot_eq (Union[Unset, str]):
        filtercausesin (Union[Unset, str]):
        filtercausesnot_in (Union[Unset, str]):
        filtercause_idseq (Union[Unset, str]):
        filtercause_idsnot_eq (Union[Unset, str]):
        filtercause_idsin (Union[Unset, str]):
        filtercause_idsnot_in (Union[Unset, str]):
        filterteamseq (Union[Unset, str]):
        filterteamsnot_eq (Union[Unset, str]):
        filterteamsin (Union[Unset, str]):
        filterteamsnot_in (Union[Unset, str]):
        filterteam_idseq (Union[Unset, str]):
        filterteam_idsnot_eq (Union[Unset, str]):
        filterteam_idsin (Union[Unset, str]):
        filterteam_idsnot_in (Union[Unset, str]):
        filterteam_nameseq (Union[Unset, str]):
        filterteam_namesnot_eq (Union[Unset, str]):
        filterteam_namesin (Union[Unset, str]):
        filterteam_namesnot_in (Union[Unset, str]):
        sort (Union[Unset, ListIncidentsSort]):
        include (Union[Unset, ListIncidentsInclude]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, IncidentList]]
    """

    kwargs = _get_kwargs(
        pageafter=pageafter,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtersearch=filtersearch,
        filterkind=filterkind,
        filterstatus=filterstatus,
        filterprivate=filterprivate,
        filteruser_id=filteruser_id,
        filterseverity=filterseverity,
        filterseverity_id=filterseverity_id,
        filterlabels=filterlabels,
        filtertypes=filtertypes,
        filtertype_ids=filtertype_ids,
        filterenvironments=filterenvironments,
        filterenvironment_ids=filterenvironment_ids,
        filterfunctionalities=filterfunctionalities,
        filterfunctionality_ids=filterfunctionality_ids,
        filterfunctionality_names=filterfunctionality_names,
        filterservices=filterservices,
        filterservice_ids=filterservice_ids,
        filterservice_names=filterservice_names,
        filterteams=filterteams,
        filterteam_ids=filterteam_ids,
        filterteam_names=filterteam_names,
        filtercause=filtercause,
        filtercause_ids=filtercause_ids,
        filtercustom_field_selected_option_ids=filtercustom_field_selected_option_ids,
        filterslack_channel_id=filterslack_channel_id,
        filtersequential_id=filtersequential_id,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        filterupdated_atgt=filterupdated_atgt,
        filterupdated_atgte=filterupdated_atgte,
        filterupdated_atlt=filterupdated_atlt,
        filterupdated_atlte=filterupdated_atlte,
        filterstarted_atgt=filterstarted_atgt,
        filterstarted_atgte=filterstarted_atgte,
        filterstarted_atlt=filterstarted_atlt,
        filterstarted_atlte=filterstarted_atlte,
        filterdetected_atgt=filterdetected_atgt,
        filterdetected_atgte=filterdetected_atgte,
        filterdetected_atlt=filterdetected_atlt,
        filterdetected_atlte=filterdetected_atlte,
        filteracknowledged_atgt=filteracknowledged_atgt,
        filteracknowledged_atgte=filteracknowledged_atgte,
        filteracknowledged_atlt=filteracknowledged_atlt,
        filteracknowledged_atlte=filteracknowledged_atlte,
        filtermitigated_atgt=filtermitigated_atgt,
        filtermitigated_atgte=filtermitigated_atgte,
        filtermitigated_atlt=filtermitigated_atlt,
        filtermitigated_atlte=filtermitigated_atlte,
        filterresolved_atgt=filterresolved_atgt,
        filterresolved_atgte=filterresolved_atgte,
        filterresolved_atlt=filterresolved_atlt,
        filterresolved_atlte=filterresolved_atlte,
        filterclosed_atgt=filterclosed_atgt,
        filterclosed_atgte=filterclosed_atgte,
        filterclosed_atlt=filterclosed_atlt,
        filterclosed_atlte=filterclosed_atlte,
        filterin_triage_atgt=filterin_triage_atgt,
        filterin_triage_atgte=filterin_triage_atgte,
        filterin_triage_atlt=filterin_triage_atlt,
        filterin_triage_atlte=filterin_triage_atlte,
        filterkindeq=filterkindeq,
        filterkindnot_eq=filterkindnot_eq,
        filterkindin=filterkindin,
        filterkindnot_in=filterkindnot_in,
        filterstatuseq=filterstatuseq,
        filterstatusnot_eq=filterstatusnot_eq,
        filterstatusin=filterstatusin,
        filterstatusnot_in=filterstatusnot_in,
        filterprivateeq=filterprivateeq,
        filterprivatenot_eq=filterprivatenot_eq,
        filterprivatein=filterprivatein,
        filterprivatenot_in=filterprivatenot_in,
        filteruser_ideq=filteruser_ideq,
        filteruser_idnot_eq=filteruser_idnot_eq,
        filteruser_idin=filteruser_idin,
        filteruser_idnot_in=filteruser_idnot_in,
        filterseverityeq=filterseverityeq,
        filterseveritynot_eq=filterseveritynot_eq,
        filterseverityin=filterseverityin,
        filterseveritynot_in=filterseveritynot_in,
        filterseverity_ideq=filterseverity_ideq,
        filterseverity_idnot_eq=filterseverity_idnot_eq,
        filterseverity_idin=filterseverity_idin,
        filterseverity_idnot_in=filterseverity_idnot_in,
        filterlabelseq=filterlabelseq,
        filterlabelsnot_eq=filterlabelsnot_eq,
        filterlabelsin=filterlabelsin,
        filterlabelsnot_in=filterlabelsnot_in,
        filterzendesk_ticket_ideq=filterzendesk_ticket_ideq,
        filterzendesk_ticket_idnot_eq=filterzendesk_ticket_idnot_eq,
        filterzendesk_ticket_idin=filterzendesk_ticket_idin,
        filterzendesk_ticket_idnot_in=filterzendesk_ticket_idnot_in,
        filtersequential_ideq=filtersequential_ideq,
        filtersequential_idnot_eq=filtersequential_idnot_eq,
        filtersequential_idin=filtersequential_idin,
        filtersequential_idnot_in=filtersequential_idnot_in,
        filtertypeseq=filtertypeseq,
        filtertypesnot_eq=filtertypesnot_eq,
        filtertypesin=filtertypesin,
        filtertypesnot_in=filtertypesnot_in,
        filtertype_idseq=filtertype_idseq,
        filtertype_idsnot_eq=filtertype_idsnot_eq,
        filtertype_idsin=filtertype_idsin,
        filtertype_idsnot_in=filtertype_idsnot_in,
        filterenvironmentseq=filterenvironmentseq,
        filterenvironmentsnot_eq=filterenvironmentsnot_eq,
        filterenvironmentsin=filterenvironmentsin,
        filterenvironmentsnot_in=filterenvironmentsnot_in,
        filterenvironment_idseq=filterenvironment_idseq,
        filterenvironment_idsnot_eq=filterenvironment_idsnot_eq,
        filterenvironment_idsin=filterenvironment_idsin,
        filterenvironment_idsnot_in=filterenvironment_idsnot_in,
        filterserviceseq=filterserviceseq,
        filterservicesnot_eq=filterservicesnot_eq,
        filterservicesin=filterservicesin,
        filterservicesnot_in=filterservicesnot_in,
        filterservice_idseq=filterservice_idseq,
        filterservice_idsnot_eq=filterservice_idsnot_eq,
        filterservice_idsin=filterservice_idsin,
        filterservice_idsnot_in=filterservice_idsnot_in,
        filterservice_nameseq=filterservice_nameseq,
        filterservice_namesnot_eq=filterservice_namesnot_eq,
        filterservice_namesin=filterservice_namesin,
        filterservice_namesnot_in=filterservice_namesnot_in,
        filterfunctionalitieseq=filterfunctionalitieseq,
        filterfunctionalitiesnot_eq=filterfunctionalitiesnot_eq,
        filterfunctionalitiesin=filterfunctionalitiesin,
        filterfunctionalitiesnot_in=filterfunctionalitiesnot_in,
        filterfunctionality_idseq=filterfunctionality_idseq,
        filterfunctionality_idsnot_eq=filterfunctionality_idsnot_eq,
        filterfunctionality_idsin=filterfunctionality_idsin,
        filterfunctionality_idsnot_in=filterfunctionality_idsnot_in,
        filterfunctionality_nameseq=filterfunctionality_nameseq,
        filterfunctionality_namesnot_eq=filterfunctionality_namesnot_eq,
        filterfunctionality_namesin=filterfunctionality_namesin,
        filterfunctionality_namesnot_in=filterfunctionality_namesnot_in,
        filtercauseseq=filtercauseseq,
        filtercausesnot_eq=filtercausesnot_eq,
        filtercausesin=filtercausesin,
        filtercausesnot_in=filtercausesnot_in,
        filtercause_idseq=filtercause_idseq,
        filtercause_idsnot_eq=filtercause_idsnot_eq,
        filtercause_idsin=filtercause_idsin,
        filtercause_idsnot_in=filtercause_idsnot_in,
        filterteamseq=filterteamseq,
        filterteamsnot_eq=filterteamsnot_eq,
        filterteamsin=filterteamsin,
        filterteamsnot_in=filterteamsnot_in,
        filterteam_idseq=filterteam_idseq,
        filterteam_idsnot_eq=filterteam_idsnot_eq,
        filterteam_idsin=filterteam_idsin,
        filterteam_idsnot_in=filterteam_idsnot_in,
        filterteam_nameseq=filterteam_nameseq,
        filterteam_namesnot_eq=filterteam_namesnot_eq,
        filterteam_namesin=filterteam_namesin,
        filterteam_namesnot_in=filterteam_namesnot_in,
        sort=sort,
        include=include,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    pageafter: Union[Unset, str] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filtersearch: Union[Unset, str] = UNSET,
    filterkind: Union[Unset, str] = UNSET,
    filterstatus: Union[Unset, str] = UNSET,
    filterprivate: Union[Unset, str] = UNSET,
    filteruser_id: Union[Unset, int] = UNSET,
    filterseverity: Union[Unset, str] = UNSET,
    filterseverity_id: Union[Unset, str] = UNSET,
    filterlabels: Union[Unset, str] = UNSET,
    filtertypes: Union[Unset, str] = UNSET,
    filtertype_ids: Union[Unset, str] = UNSET,
    filterenvironments: Union[Unset, str] = UNSET,
    filterenvironment_ids: Union[Unset, str] = UNSET,
    filterfunctionalities: Union[Unset, str] = UNSET,
    filterfunctionality_ids: Union[Unset, str] = UNSET,
    filterfunctionality_names: Union[Unset, str] = UNSET,
    filterservices: Union[Unset, str] = UNSET,
    filterservice_ids: Union[Unset, str] = UNSET,
    filterservice_names: Union[Unset, str] = UNSET,
    filterteams: Union[Unset, str] = UNSET,
    filterteam_ids: Union[Unset, str] = UNSET,
    filterteam_names: Union[Unset, str] = UNSET,
    filtercause: Union[Unset, str] = UNSET,
    filtercause_ids: Union[Unset, str] = UNSET,
    filtercustom_field_selected_option_ids: Union[Unset, str] = UNSET,
    filterslack_channel_id: Union[Unset, str] = UNSET,
    filtersequential_id: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
    filterupdated_atgt: Union[Unset, str] = UNSET,
    filterupdated_atgte: Union[Unset, str] = UNSET,
    filterupdated_atlt: Union[Unset, str] = UNSET,
    filterupdated_atlte: Union[Unset, str] = UNSET,
    filterstarted_atgt: Union[Unset, str] = UNSET,
    filterstarted_atgte: Union[Unset, str] = UNSET,
    filterstarted_atlt: Union[Unset, str] = UNSET,
    filterstarted_atlte: Union[Unset, str] = UNSET,
    filterdetected_atgt: Union[Unset, str] = UNSET,
    filterdetected_atgte: Union[Unset, str] = UNSET,
    filterdetected_atlt: Union[Unset, str] = UNSET,
    filterdetected_atlte: Union[Unset, str] = UNSET,
    filteracknowledged_atgt: Union[Unset, str] = UNSET,
    filteracknowledged_atgte: Union[Unset, str] = UNSET,
    filteracknowledged_atlt: Union[Unset, str] = UNSET,
    filteracknowledged_atlte: Union[Unset, str] = UNSET,
    filtermitigated_atgt: Union[Unset, str] = UNSET,
    filtermitigated_atgte: Union[Unset, str] = UNSET,
    filtermitigated_atlt: Union[Unset, str] = UNSET,
    filtermitigated_atlte: Union[Unset, str] = UNSET,
    filterresolved_atgt: Union[Unset, str] = UNSET,
    filterresolved_atgte: Union[Unset, str] = UNSET,
    filterresolved_atlt: Union[Unset, str] = UNSET,
    filterresolved_atlte: Union[Unset, str] = UNSET,
    filterclosed_atgt: Union[Unset, str] = UNSET,
    filterclosed_atgte: Union[Unset, str] = UNSET,
    filterclosed_atlt: Union[Unset, str] = UNSET,
    filterclosed_atlte: Union[Unset, str] = UNSET,
    filterin_triage_atgt: Union[Unset, str] = UNSET,
    filterin_triage_atgte: Union[Unset, str] = UNSET,
    filterin_triage_atlt: Union[Unset, str] = UNSET,
    filterin_triage_atlte: Union[Unset, str] = UNSET,
    filterkindeq: Union[Unset, str] = UNSET,
    filterkindnot_eq: Union[Unset, str] = UNSET,
    filterkindin: Union[Unset, str] = UNSET,
    filterkindnot_in: Union[Unset, str] = UNSET,
    filterstatuseq: Union[Unset, str] = UNSET,
    filterstatusnot_eq: Union[Unset, str] = UNSET,
    filterstatusin: Union[Unset, str] = UNSET,
    filterstatusnot_in: Union[Unset, str] = UNSET,
    filterprivateeq: Union[Unset, str] = UNSET,
    filterprivatenot_eq: Union[Unset, str] = UNSET,
    filterprivatein: Union[Unset, str] = UNSET,
    filterprivatenot_in: Union[Unset, str] = UNSET,
    filteruser_ideq: Union[Unset, str] = UNSET,
    filteruser_idnot_eq: Union[Unset, str] = UNSET,
    filteruser_idin: Union[Unset, str] = UNSET,
    filteruser_idnot_in: Union[Unset, str] = UNSET,
    filterseverityeq: Union[Unset, str] = UNSET,
    filterseveritynot_eq: Union[Unset, str] = UNSET,
    filterseverityin: Union[Unset, str] = UNSET,
    filterseveritynot_in: Union[Unset, str] = UNSET,
    filterseverity_ideq: Union[Unset, str] = UNSET,
    filterseverity_idnot_eq: Union[Unset, str] = UNSET,
    filterseverity_idin: Union[Unset, str] = UNSET,
    filterseverity_idnot_in: Union[Unset, str] = UNSET,
    filterlabelseq: Union[Unset, str] = UNSET,
    filterlabelsnot_eq: Union[Unset, str] = UNSET,
    filterlabelsin: Union[Unset, str] = UNSET,
    filterlabelsnot_in: Union[Unset, str] = UNSET,
    filterzendesk_ticket_ideq: Union[Unset, str] = UNSET,
    filterzendesk_ticket_idnot_eq: Union[Unset, str] = UNSET,
    filterzendesk_ticket_idin: Union[Unset, str] = UNSET,
    filterzendesk_ticket_idnot_in: Union[Unset, str] = UNSET,
    filtersequential_ideq: Union[Unset, str] = UNSET,
    filtersequential_idnot_eq: Union[Unset, str] = UNSET,
    filtersequential_idin: Union[Unset, str] = UNSET,
    filtersequential_idnot_in: Union[Unset, str] = UNSET,
    filtertypeseq: Union[Unset, str] = UNSET,
    filtertypesnot_eq: Union[Unset, str] = UNSET,
    filtertypesin: Union[Unset, str] = UNSET,
    filtertypesnot_in: Union[Unset, str] = UNSET,
    filtertype_idseq: Union[Unset, str] = UNSET,
    filtertype_idsnot_eq: Union[Unset, str] = UNSET,
    filtertype_idsin: Union[Unset, str] = UNSET,
    filtertype_idsnot_in: Union[Unset, str] = UNSET,
    filterenvironmentseq: Union[Unset, str] = UNSET,
    filterenvironmentsnot_eq: Union[Unset, str] = UNSET,
    filterenvironmentsin: Union[Unset, str] = UNSET,
    filterenvironmentsnot_in: Union[Unset, str] = UNSET,
    filterenvironment_idseq: Union[Unset, str] = UNSET,
    filterenvironment_idsnot_eq: Union[Unset, str] = UNSET,
    filterenvironment_idsin: Union[Unset, str] = UNSET,
    filterenvironment_idsnot_in: Union[Unset, str] = UNSET,
    filterserviceseq: Union[Unset, str] = UNSET,
    filterservicesnot_eq: Union[Unset, str] = UNSET,
    filterservicesin: Union[Unset, str] = UNSET,
    filterservicesnot_in: Union[Unset, str] = UNSET,
    filterservice_idseq: Union[Unset, str] = UNSET,
    filterservice_idsnot_eq: Union[Unset, str] = UNSET,
    filterservice_idsin: Union[Unset, str] = UNSET,
    filterservice_idsnot_in: Union[Unset, str] = UNSET,
    filterservice_nameseq: Union[Unset, str] = UNSET,
    filterservice_namesnot_eq: Union[Unset, str] = UNSET,
    filterservice_namesin: Union[Unset, str] = UNSET,
    filterservice_namesnot_in: Union[Unset, str] = UNSET,
    filterfunctionalitieseq: Union[Unset, str] = UNSET,
    filterfunctionalitiesnot_eq: Union[Unset, str] = UNSET,
    filterfunctionalitiesin: Union[Unset, str] = UNSET,
    filterfunctionalitiesnot_in: Union[Unset, str] = UNSET,
    filterfunctionality_idseq: Union[Unset, str] = UNSET,
    filterfunctionality_idsnot_eq: Union[Unset, str] = UNSET,
    filterfunctionality_idsin: Union[Unset, str] = UNSET,
    filterfunctionality_idsnot_in: Union[Unset, str] = UNSET,
    filterfunctionality_nameseq: Union[Unset, str] = UNSET,
    filterfunctionality_namesnot_eq: Union[Unset, str] = UNSET,
    filterfunctionality_namesin: Union[Unset, str] = UNSET,
    filterfunctionality_namesnot_in: Union[Unset, str] = UNSET,
    filtercauseseq: Union[Unset, str] = UNSET,
    filtercausesnot_eq: Union[Unset, str] = UNSET,
    filtercausesin: Union[Unset, str] = UNSET,
    filtercausesnot_in: Union[Unset, str] = UNSET,
    filtercause_idseq: Union[Unset, str] = UNSET,
    filtercause_idsnot_eq: Union[Unset, str] = UNSET,
    filtercause_idsin: Union[Unset, str] = UNSET,
    filtercause_idsnot_in: Union[Unset, str] = UNSET,
    filterteamseq: Union[Unset, str] = UNSET,
    filterteamsnot_eq: Union[Unset, str] = UNSET,
    filterteamsin: Union[Unset, str] = UNSET,
    filterteamsnot_in: Union[Unset, str] = UNSET,
    filterteam_idseq: Union[Unset, str] = UNSET,
    filterteam_idsnot_eq: Union[Unset, str] = UNSET,
    filterteam_idsin: Union[Unset, str] = UNSET,
    filterteam_idsnot_in: Union[Unset, str] = UNSET,
    filterteam_nameseq: Union[Unset, str] = UNSET,
    filterteam_namesnot_eq: Union[Unset, str] = UNSET,
    filterteam_namesin: Union[Unset, str] = UNSET,
    filterteam_namesnot_in: Union[Unset, str] = UNSET,
    sort: Union[Unset, ListIncidentsSort] = UNSET,
    include: Union[Unset, ListIncidentsInclude] = UNSET,
) -> Optional[Union[ErrorsList, IncidentList]]:
    """List incidents

     List incidents

    Args:
        pageafter (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtersearch (Union[Unset, str]):
        filterkind (Union[Unset, str]):
        filterstatus (Union[Unset, str]):
        filterprivate (Union[Unset, str]):
        filteruser_id (Union[Unset, int]):
        filterseverity (Union[Unset, str]):
        filterseverity_id (Union[Unset, str]):
        filterlabels (Union[Unset, str]):
        filtertypes (Union[Unset, str]):
        filtertype_ids (Union[Unset, str]):
        filterenvironments (Union[Unset, str]):
        filterenvironment_ids (Union[Unset, str]):
        filterfunctionalities (Union[Unset, str]):
        filterfunctionality_ids (Union[Unset, str]):
        filterfunctionality_names (Union[Unset, str]):
        filterservices (Union[Unset, str]):
        filterservice_ids (Union[Unset, str]):
        filterservice_names (Union[Unset, str]):
        filterteams (Union[Unset, str]):
        filterteam_ids (Union[Unset, str]):
        filterteam_names (Union[Unset, str]):
        filtercause (Union[Unset, str]):
        filtercause_ids (Union[Unset, str]):
        filtercustom_field_selected_option_ids (Union[Unset, str]):
        filterslack_channel_id (Union[Unset, str]):
        filtersequential_id (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        filterupdated_atgt (Union[Unset, str]):
        filterupdated_atgte (Union[Unset, str]):
        filterupdated_atlt (Union[Unset, str]):
        filterupdated_atlte (Union[Unset, str]):
        filterstarted_atgt (Union[Unset, str]):
        filterstarted_atgte (Union[Unset, str]):
        filterstarted_atlt (Union[Unset, str]):
        filterstarted_atlte (Union[Unset, str]):
        filterdetected_atgt (Union[Unset, str]):
        filterdetected_atgte (Union[Unset, str]):
        filterdetected_atlt (Union[Unset, str]):
        filterdetected_atlte (Union[Unset, str]):
        filteracknowledged_atgt (Union[Unset, str]):
        filteracknowledged_atgte (Union[Unset, str]):
        filteracknowledged_atlt (Union[Unset, str]):
        filteracknowledged_atlte (Union[Unset, str]):
        filtermitigated_atgt (Union[Unset, str]):
        filtermitigated_atgte (Union[Unset, str]):
        filtermitigated_atlt (Union[Unset, str]):
        filtermitigated_atlte (Union[Unset, str]):
        filterresolved_atgt (Union[Unset, str]):
        filterresolved_atgte (Union[Unset, str]):
        filterresolved_atlt (Union[Unset, str]):
        filterresolved_atlte (Union[Unset, str]):
        filterclosed_atgt (Union[Unset, str]):
        filterclosed_atgte (Union[Unset, str]):
        filterclosed_atlt (Union[Unset, str]):
        filterclosed_atlte (Union[Unset, str]):
        filterin_triage_atgt (Union[Unset, str]):
        filterin_triage_atgte (Union[Unset, str]):
        filterin_triage_atlt (Union[Unset, str]):
        filterin_triage_atlte (Union[Unset, str]):
        filterkindeq (Union[Unset, str]):
        filterkindnot_eq (Union[Unset, str]):
        filterkindin (Union[Unset, str]):
        filterkindnot_in (Union[Unset, str]):
        filterstatuseq (Union[Unset, str]):
        filterstatusnot_eq (Union[Unset, str]):
        filterstatusin (Union[Unset, str]):
        filterstatusnot_in (Union[Unset, str]):
        filterprivateeq (Union[Unset, str]):
        filterprivatenot_eq (Union[Unset, str]):
        filterprivatein (Union[Unset, str]):
        filterprivatenot_in (Union[Unset, str]):
        filteruser_ideq (Union[Unset, str]):
        filteruser_idnot_eq (Union[Unset, str]):
        filteruser_idin (Union[Unset, str]):
        filteruser_idnot_in (Union[Unset, str]):
        filterseverityeq (Union[Unset, str]):
        filterseveritynot_eq (Union[Unset, str]):
        filterseverityin (Union[Unset, str]):
        filterseveritynot_in (Union[Unset, str]):
        filterseverity_ideq (Union[Unset, str]):
        filterseverity_idnot_eq (Union[Unset, str]):
        filterseverity_idin (Union[Unset, str]):
        filterseverity_idnot_in (Union[Unset, str]):
        filterlabelseq (Union[Unset, str]):
        filterlabelsnot_eq (Union[Unset, str]):
        filterlabelsin (Union[Unset, str]):
        filterlabelsnot_in (Union[Unset, str]):
        filterzendesk_ticket_ideq (Union[Unset, str]):
        filterzendesk_ticket_idnot_eq (Union[Unset, str]):
        filterzendesk_ticket_idin (Union[Unset, str]):
        filterzendesk_ticket_idnot_in (Union[Unset, str]):
        filtersequential_ideq (Union[Unset, str]):
        filtersequential_idnot_eq (Union[Unset, str]):
        filtersequential_idin (Union[Unset, str]):
        filtersequential_idnot_in (Union[Unset, str]):
        filtertypeseq (Union[Unset, str]):
        filtertypesnot_eq (Union[Unset, str]):
        filtertypesin (Union[Unset, str]):
        filtertypesnot_in (Union[Unset, str]):
        filtertype_idseq (Union[Unset, str]):
        filtertype_idsnot_eq (Union[Unset, str]):
        filtertype_idsin (Union[Unset, str]):
        filtertype_idsnot_in (Union[Unset, str]):
        filterenvironmentseq (Union[Unset, str]):
        filterenvironmentsnot_eq (Union[Unset, str]):
        filterenvironmentsin (Union[Unset, str]):
        filterenvironmentsnot_in (Union[Unset, str]):
        filterenvironment_idseq (Union[Unset, str]):
        filterenvironment_idsnot_eq (Union[Unset, str]):
        filterenvironment_idsin (Union[Unset, str]):
        filterenvironment_idsnot_in (Union[Unset, str]):
        filterserviceseq (Union[Unset, str]):
        filterservicesnot_eq (Union[Unset, str]):
        filterservicesin (Union[Unset, str]):
        filterservicesnot_in (Union[Unset, str]):
        filterservice_idseq (Union[Unset, str]):
        filterservice_idsnot_eq (Union[Unset, str]):
        filterservice_idsin (Union[Unset, str]):
        filterservice_idsnot_in (Union[Unset, str]):
        filterservice_nameseq (Union[Unset, str]):
        filterservice_namesnot_eq (Union[Unset, str]):
        filterservice_namesin (Union[Unset, str]):
        filterservice_namesnot_in (Union[Unset, str]):
        filterfunctionalitieseq (Union[Unset, str]):
        filterfunctionalitiesnot_eq (Union[Unset, str]):
        filterfunctionalitiesin (Union[Unset, str]):
        filterfunctionalitiesnot_in (Union[Unset, str]):
        filterfunctionality_idseq (Union[Unset, str]):
        filterfunctionality_idsnot_eq (Union[Unset, str]):
        filterfunctionality_idsin (Union[Unset, str]):
        filterfunctionality_idsnot_in (Union[Unset, str]):
        filterfunctionality_nameseq (Union[Unset, str]):
        filterfunctionality_namesnot_eq (Union[Unset, str]):
        filterfunctionality_namesin (Union[Unset, str]):
        filterfunctionality_namesnot_in (Union[Unset, str]):
        filtercauseseq (Union[Unset, str]):
        filtercausesnot_eq (Union[Unset, str]):
        filtercausesin (Union[Unset, str]):
        filtercausesnot_in (Union[Unset, str]):
        filtercause_idseq (Union[Unset, str]):
        filtercause_idsnot_eq (Union[Unset, str]):
        filtercause_idsin (Union[Unset, str]):
        filtercause_idsnot_in (Union[Unset, str]):
        filterteamseq (Union[Unset, str]):
        filterteamsnot_eq (Union[Unset, str]):
        filterteamsin (Union[Unset, str]):
        filterteamsnot_in (Union[Unset, str]):
        filterteam_idseq (Union[Unset, str]):
        filterteam_idsnot_eq (Union[Unset, str]):
        filterteam_idsin (Union[Unset, str]):
        filterteam_idsnot_in (Union[Unset, str]):
        filterteam_nameseq (Union[Unset, str]):
        filterteam_namesnot_eq (Union[Unset, str]):
        filterteam_namesin (Union[Unset, str]):
        filterteam_namesnot_in (Union[Unset, str]):
        sort (Union[Unset, ListIncidentsSort]):
        include (Union[Unset, ListIncidentsInclude]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, IncidentList]
    """

    return sync_detailed(
        client=client,
        pageafter=pageafter,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtersearch=filtersearch,
        filterkind=filterkind,
        filterstatus=filterstatus,
        filterprivate=filterprivate,
        filteruser_id=filteruser_id,
        filterseverity=filterseverity,
        filterseverity_id=filterseverity_id,
        filterlabels=filterlabels,
        filtertypes=filtertypes,
        filtertype_ids=filtertype_ids,
        filterenvironments=filterenvironments,
        filterenvironment_ids=filterenvironment_ids,
        filterfunctionalities=filterfunctionalities,
        filterfunctionality_ids=filterfunctionality_ids,
        filterfunctionality_names=filterfunctionality_names,
        filterservices=filterservices,
        filterservice_ids=filterservice_ids,
        filterservice_names=filterservice_names,
        filterteams=filterteams,
        filterteam_ids=filterteam_ids,
        filterteam_names=filterteam_names,
        filtercause=filtercause,
        filtercause_ids=filtercause_ids,
        filtercustom_field_selected_option_ids=filtercustom_field_selected_option_ids,
        filterslack_channel_id=filterslack_channel_id,
        filtersequential_id=filtersequential_id,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        filterupdated_atgt=filterupdated_atgt,
        filterupdated_atgte=filterupdated_atgte,
        filterupdated_atlt=filterupdated_atlt,
        filterupdated_atlte=filterupdated_atlte,
        filterstarted_atgt=filterstarted_atgt,
        filterstarted_atgte=filterstarted_atgte,
        filterstarted_atlt=filterstarted_atlt,
        filterstarted_atlte=filterstarted_atlte,
        filterdetected_atgt=filterdetected_atgt,
        filterdetected_atgte=filterdetected_atgte,
        filterdetected_atlt=filterdetected_atlt,
        filterdetected_atlte=filterdetected_atlte,
        filteracknowledged_atgt=filteracknowledged_atgt,
        filteracknowledged_atgte=filteracknowledged_atgte,
        filteracknowledged_atlt=filteracknowledged_atlt,
        filteracknowledged_atlte=filteracknowledged_atlte,
        filtermitigated_atgt=filtermitigated_atgt,
        filtermitigated_atgte=filtermitigated_atgte,
        filtermitigated_atlt=filtermitigated_atlt,
        filtermitigated_atlte=filtermitigated_atlte,
        filterresolved_atgt=filterresolved_atgt,
        filterresolved_atgte=filterresolved_atgte,
        filterresolved_atlt=filterresolved_atlt,
        filterresolved_atlte=filterresolved_atlte,
        filterclosed_atgt=filterclosed_atgt,
        filterclosed_atgte=filterclosed_atgte,
        filterclosed_atlt=filterclosed_atlt,
        filterclosed_atlte=filterclosed_atlte,
        filterin_triage_atgt=filterin_triage_atgt,
        filterin_triage_atgte=filterin_triage_atgte,
        filterin_triage_atlt=filterin_triage_atlt,
        filterin_triage_atlte=filterin_triage_atlte,
        filterkindeq=filterkindeq,
        filterkindnot_eq=filterkindnot_eq,
        filterkindin=filterkindin,
        filterkindnot_in=filterkindnot_in,
        filterstatuseq=filterstatuseq,
        filterstatusnot_eq=filterstatusnot_eq,
        filterstatusin=filterstatusin,
        filterstatusnot_in=filterstatusnot_in,
        filterprivateeq=filterprivateeq,
        filterprivatenot_eq=filterprivatenot_eq,
        filterprivatein=filterprivatein,
        filterprivatenot_in=filterprivatenot_in,
        filteruser_ideq=filteruser_ideq,
        filteruser_idnot_eq=filteruser_idnot_eq,
        filteruser_idin=filteruser_idin,
        filteruser_idnot_in=filteruser_idnot_in,
        filterseverityeq=filterseverityeq,
        filterseveritynot_eq=filterseveritynot_eq,
        filterseverityin=filterseverityin,
        filterseveritynot_in=filterseveritynot_in,
        filterseverity_ideq=filterseverity_ideq,
        filterseverity_idnot_eq=filterseverity_idnot_eq,
        filterseverity_idin=filterseverity_idin,
        filterseverity_idnot_in=filterseverity_idnot_in,
        filterlabelseq=filterlabelseq,
        filterlabelsnot_eq=filterlabelsnot_eq,
        filterlabelsin=filterlabelsin,
        filterlabelsnot_in=filterlabelsnot_in,
        filterzendesk_ticket_ideq=filterzendesk_ticket_ideq,
        filterzendesk_ticket_idnot_eq=filterzendesk_ticket_idnot_eq,
        filterzendesk_ticket_idin=filterzendesk_ticket_idin,
        filterzendesk_ticket_idnot_in=filterzendesk_ticket_idnot_in,
        filtersequential_ideq=filtersequential_ideq,
        filtersequential_idnot_eq=filtersequential_idnot_eq,
        filtersequential_idin=filtersequential_idin,
        filtersequential_idnot_in=filtersequential_idnot_in,
        filtertypeseq=filtertypeseq,
        filtertypesnot_eq=filtertypesnot_eq,
        filtertypesin=filtertypesin,
        filtertypesnot_in=filtertypesnot_in,
        filtertype_idseq=filtertype_idseq,
        filtertype_idsnot_eq=filtertype_idsnot_eq,
        filtertype_idsin=filtertype_idsin,
        filtertype_idsnot_in=filtertype_idsnot_in,
        filterenvironmentseq=filterenvironmentseq,
        filterenvironmentsnot_eq=filterenvironmentsnot_eq,
        filterenvironmentsin=filterenvironmentsin,
        filterenvironmentsnot_in=filterenvironmentsnot_in,
        filterenvironment_idseq=filterenvironment_idseq,
        filterenvironment_idsnot_eq=filterenvironment_idsnot_eq,
        filterenvironment_idsin=filterenvironment_idsin,
        filterenvironment_idsnot_in=filterenvironment_idsnot_in,
        filterserviceseq=filterserviceseq,
        filterservicesnot_eq=filterservicesnot_eq,
        filterservicesin=filterservicesin,
        filterservicesnot_in=filterservicesnot_in,
        filterservice_idseq=filterservice_idseq,
        filterservice_idsnot_eq=filterservice_idsnot_eq,
        filterservice_idsin=filterservice_idsin,
        filterservice_idsnot_in=filterservice_idsnot_in,
        filterservice_nameseq=filterservice_nameseq,
        filterservice_namesnot_eq=filterservice_namesnot_eq,
        filterservice_namesin=filterservice_namesin,
        filterservice_namesnot_in=filterservice_namesnot_in,
        filterfunctionalitieseq=filterfunctionalitieseq,
        filterfunctionalitiesnot_eq=filterfunctionalitiesnot_eq,
        filterfunctionalitiesin=filterfunctionalitiesin,
        filterfunctionalitiesnot_in=filterfunctionalitiesnot_in,
        filterfunctionality_idseq=filterfunctionality_idseq,
        filterfunctionality_idsnot_eq=filterfunctionality_idsnot_eq,
        filterfunctionality_idsin=filterfunctionality_idsin,
        filterfunctionality_idsnot_in=filterfunctionality_idsnot_in,
        filterfunctionality_nameseq=filterfunctionality_nameseq,
        filterfunctionality_namesnot_eq=filterfunctionality_namesnot_eq,
        filterfunctionality_namesin=filterfunctionality_namesin,
        filterfunctionality_namesnot_in=filterfunctionality_namesnot_in,
        filtercauseseq=filtercauseseq,
        filtercausesnot_eq=filtercausesnot_eq,
        filtercausesin=filtercausesin,
        filtercausesnot_in=filtercausesnot_in,
        filtercause_idseq=filtercause_idseq,
        filtercause_idsnot_eq=filtercause_idsnot_eq,
        filtercause_idsin=filtercause_idsin,
        filtercause_idsnot_in=filtercause_idsnot_in,
        filterteamseq=filterteamseq,
        filterteamsnot_eq=filterteamsnot_eq,
        filterteamsin=filterteamsin,
        filterteamsnot_in=filterteamsnot_in,
        filterteam_idseq=filterteam_idseq,
        filterteam_idsnot_eq=filterteam_idsnot_eq,
        filterteam_idsin=filterteam_idsin,
        filterteam_idsnot_in=filterteam_idsnot_in,
        filterteam_nameseq=filterteam_nameseq,
        filterteam_namesnot_eq=filterteam_namesnot_eq,
        filterteam_namesin=filterteam_namesin,
        filterteam_namesnot_in=filterteam_namesnot_in,
        sort=sort,
        include=include,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    pageafter: Union[Unset, str] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filtersearch: Union[Unset, str] = UNSET,
    filterkind: Union[Unset, str] = UNSET,
    filterstatus: Union[Unset, str] = UNSET,
    filterprivate: Union[Unset, str] = UNSET,
    filteruser_id: Union[Unset, int] = UNSET,
    filterseverity: Union[Unset, str] = UNSET,
    filterseverity_id: Union[Unset, str] = UNSET,
    filterlabels: Union[Unset, str] = UNSET,
    filtertypes: Union[Unset, str] = UNSET,
    filtertype_ids: Union[Unset, str] = UNSET,
    filterenvironments: Union[Unset, str] = UNSET,
    filterenvironment_ids: Union[Unset, str] = UNSET,
    filterfunctionalities: Union[Unset, str] = UNSET,
    filterfunctionality_ids: Union[Unset, str] = UNSET,
    filterfunctionality_names: Union[Unset, str] = UNSET,
    filterservices: Union[Unset, str] = UNSET,
    filterservice_ids: Union[Unset, str] = UNSET,
    filterservice_names: Union[Unset, str] = UNSET,
    filterteams: Union[Unset, str] = UNSET,
    filterteam_ids: Union[Unset, str] = UNSET,
    filterteam_names: Union[Unset, str] = UNSET,
    filtercause: Union[Unset, str] = UNSET,
    filtercause_ids: Union[Unset, str] = UNSET,
    filtercustom_field_selected_option_ids: Union[Unset, str] = UNSET,
    filterslack_channel_id: Union[Unset, str] = UNSET,
    filtersequential_id: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
    filterupdated_atgt: Union[Unset, str] = UNSET,
    filterupdated_atgte: Union[Unset, str] = UNSET,
    filterupdated_atlt: Union[Unset, str] = UNSET,
    filterupdated_atlte: Union[Unset, str] = UNSET,
    filterstarted_atgt: Union[Unset, str] = UNSET,
    filterstarted_atgte: Union[Unset, str] = UNSET,
    filterstarted_atlt: Union[Unset, str] = UNSET,
    filterstarted_atlte: Union[Unset, str] = UNSET,
    filterdetected_atgt: Union[Unset, str] = UNSET,
    filterdetected_atgte: Union[Unset, str] = UNSET,
    filterdetected_atlt: Union[Unset, str] = UNSET,
    filterdetected_atlte: Union[Unset, str] = UNSET,
    filteracknowledged_atgt: Union[Unset, str] = UNSET,
    filteracknowledged_atgte: Union[Unset, str] = UNSET,
    filteracknowledged_atlt: Union[Unset, str] = UNSET,
    filteracknowledged_atlte: Union[Unset, str] = UNSET,
    filtermitigated_atgt: Union[Unset, str] = UNSET,
    filtermitigated_atgte: Union[Unset, str] = UNSET,
    filtermitigated_atlt: Union[Unset, str] = UNSET,
    filtermitigated_atlte: Union[Unset, str] = UNSET,
    filterresolved_atgt: Union[Unset, str] = UNSET,
    filterresolved_atgte: Union[Unset, str] = UNSET,
    filterresolved_atlt: Union[Unset, str] = UNSET,
    filterresolved_atlte: Union[Unset, str] = UNSET,
    filterclosed_atgt: Union[Unset, str] = UNSET,
    filterclosed_atgte: Union[Unset, str] = UNSET,
    filterclosed_atlt: Union[Unset, str] = UNSET,
    filterclosed_atlte: Union[Unset, str] = UNSET,
    filterin_triage_atgt: Union[Unset, str] = UNSET,
    filterin_triage_atgte: Union[Unset, str] = UNSET,
    filterin_triage_atlt: Union[Unset, str] = UNSET,
    filterin_triage_atlte: Union[Unset, str] = UNSET,
    filterkindeq: Union[Unset, str] = UNSET,
    filterkindnot_eq: Union[Unset, str] = UNSET,
    filterkindin: Union[Unset, str] = UNSET,
    filterkindnot_in: Union[Unset, str] = UNSET,
    filterstatuseq: Union[Unset, str] = UNSET,
    filterstatusnot_eq: Union[Unset, str] = UNSET,
    filterstatusin: Union[Unset, str] = UNSET,
    filterstatusnot_in: Union[Unset, str] = UNSET,
    filterprivateeq: Union[Unset, str] = UNSET,
    filterprivatenot_eq: Union[Unset, str] = UNSET,
    filterprivatein: Union[Unset, str] = UNSET,
    filterprivatenot_in: Union[Unset, str] = UNSET,
    filteruser_ideq: Union[Unset, str] = UNSET,
    filteruser_idnot_eq: Union[Unset, str] = UNSET,
    filteruser_idin: Union[Unset, str] = UNSET,
    filteruser_idnot_in: Union[Unset, str] = UNSET,
    filterseverityeq: Union[Unset, str] = UNSET,
    filterseveritynot_eq: Union[Unset, str] = UNSET,
    filterseverityin: Union[Unset, str] = UNSET,
    filterseveritynot_in: Union[Unset, str] = UNSET,
    filterseverity_ideq: Union[Unset, str] = UNSET,
    filterseverity_idnot_eq: Union[Unset, str] = UNSET,
    filterseverity_idin: Union[Unset, str] = UNSET,
    filterseverity_idnot_in: Union[Unset, str] = UNSET,
    filterlabelseq: Union[Unset, str] = UNSET,
    filterlabelsnot_eq: Union[Unset, str] = UNSET,
    filterlabelsin: Union[Unset, str] = UNSET,
    filterlabelsnot_in: Union[Unset, str] = UNSET,
    filterzendesk_ticket_ideq: Union[Unset, str] = UNSET,
    filterzendesk_ticket_idnot_eq: Union[Unset, str] = UNSET,
    filterzendesk_ticket_idin: Union[Unset, str] = UNSET,
    filterzendesk_ticket_idnot_in: Union[Unset, str] = UNSET,
    filtersequential_ideq: Union[Unset, str] = UNSET,
    filtersequential_idnot_eq: Union[Unset, str] = UNSET,
    filtersequential_idin: Union[Unset, str] = UNSET,
    filtersequential_idnot_in: Union[Unset, str] = UNSET,
    filtertypeseq: Union[Unset, str] = UNSET,
    filtertypesnot_eq: Union[Unset, str] = UNSET,
    filtertypesin: Union[Unset, str] = UNSET,
    filtertypesnot_in: Union[Unset, str] = UNSET,
    filtertype_idseq: Union[Unset, str] = UNSET,
    filtertype_idsnot_eq: Union[Unset, str] = UNSET,
    filtertype_idsin: Union[Unset, str] = UNSET,
    filtertype_idsnot_in: Union[Unset, str] = UNSET,
    filterenvironmentseq: Union[Unset, str] = UNSET,
    filterenvironmentsnot_eq: Union[Unset, str] = UNSET,
    filterenvironmentsin: Union[Unset, str] = UNSET,
    filterenvironmentsnot_in: Union[Unset, str] = UNSET,
    filterenvironment_idseq: Union[Unset, str] = UNSET,
    filterenvironment_idsnot_eq: Union[Unset, str] = UNSET,
    filterenvironment_idsin: Union[Unset, str] = UNSET,
    filterenvironment_idsnot_in: Union[Unset, str] = UNSET,
    filterserviceseq: Union[Unset, str] = UNSET,
    filterservicesnot_eq: Union[Unset, str] = UNSET,
    filterservicesin: Union[Unset, str] = UNSET,
    filterservicesnot_in: Union[Unset, str] = UNSET,
    filterservice_idseq: Union[Unset, str] = UNSET,
    filterservice_idsnot_eq: Union[Unset, str] = UNSET,
    filterservice_idsin: Union[Unset, str] = UNSET,
    filterservice_idsnot_in: Union[Unset, str] = UNSET,
    filterservice_nameseq: Union[Unset, str] = UNSET,
    filterservice_namesnot_eq: Union[Unset, str] = UNSET,
    filterservice_namesin: Union[Unset, str] = UNSET,
    filterservice_namesnot_in: Union[Unset, str] = UNSET,
    filterfunctionalitieseq: Union[Unset, str] = UNSET,
    filterfunctionalitiesnot_eq: Union[Unset, str] = UNSET,
    filterfunctionalitiesin: Union[Unset, str] = UNSET,
    filterfunctionalitiesnot_in: Union[Unset, str] = UNSET,
    filterfunctionality_idseq: Union[Unset, str] = UNSET,
    filterfunctionality_idsnot_eq: Union[Unset, str] = UNSET,
    filterfunctionality_idsin: Union[Unset, str] = UNSET,
    filterfunctionality_idsnot_in: Union[Unset, str] = UNSET,
    filterfunctionality_nameseq: Union[Unset, str] = UNSET,
    filterfunctionality_namesnot_eq: Union[Unset, str] = UNSET,
    filterfunctionality_namesin: Union[Unset, str] = UNSET,
    filterfunctionality_namesnot_in: Union[Unset, str] = UNSET,
    filtercauseseq: Union[Unset, str] = UNSET,
    filtercausesnot_eq: Union[Unset, str] = UNSET,
    filtercausesin: Union[Unset, str] = UNSET,
    filtercausesnot_in: Union[Unset, str] = UNSET,
    filtercause_idseq: Union[Unset, str] = UNSET,
    filtercause_idsnot_eq: Union[Unset, str] = UNSET,
    filtercause_idsin: Union[Unset, str] = UNSET,
    filtercause_idsnot_in: Union[Unset, str] = UNSET,
    filterteamseq: Union[Unset, str] = UNSET,
    filterteamsnot_eq: Union[Unset, str] = UNSET,
    filterteamsin: Union[Unset, str] = UNSET,
    filterteamsnot_in: Union[Unset, str] = UNSET,
    filterteam_idseq: Union[Unset, str] = UNSET,
    filterteam_idsnot_eq: Union[Unset, str] = UNSET,
    filterteam_idsin: Union[Unset, str] = UNSET,
    filterteam_idsnot_in: Union[Unset, str] = UNSET,
    filterteam_nameseq: Union[Unset, str] = UNSET,
    filterteam_namesnot_eq: Union[Unset, str] = UNSET,
    filterteam_namesin: Union[Unset, str] = UNSET,
    filterteam_namesnot_in: Union[Unset, str] = UNSET,
    sort: Union[Unset, ListIncidentsSort] = UNSET,
    include: Union[Unset, ListIncidentsInclude] = UNSET,
) -> Response[Union[ErrorsList, IncidentList]]:
    """List incidents

     List incidents

    Args:
        pageafter (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtersearch (Union[Unset, str]):
        filterkind (Union[Unset, str]):
        filterstatus (Union[Unset, str]):
        filterprivate (Union[Unset, str]):
        filteruser_id (Union[Unset, int]):
        filterseverity (Union[Unset, str]):
        filterseverity_id (Union[Unset, str]):
        filterlabels (Union[Unset, str]):
        filtertypes (Union[Unset, str]):
        filtertype_ids (Union[Unset, str]):
        filterenvironments (Union[Unset, str]):
        filterenvironment_ids (Union[Unset, str]):
        filterfunctionalities (Union[Unset, str]):
        filterfunctionality_ids (Union[Unset, str]):
        filterfunctionality_names (Union[Unset, str]):
        filterservices (Union[Unset, str]):
        filterservice_ids (Union[Unset, str]):
        filterservice_names (Union[Unset, str]):
        filterteams (Union[Unset, str]):
        filterteam_ids (Union[Unset, str]):
        filterteam_names (Union[Unset, str]):
        filtercause (Union[Unset, str]):
        filtercause_ids (Union[Unset, str]):
        filtercustom_field_selected_option_ids (Union[Unset, str]):
        filterslack_channel_id (Union[Unset, str]):
        filtersequential_id (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        filterupdated_atgt (Union[Unset, str]):
        filterupdated_atgte (Union[Unset, str]):
        filterupdated_atlt (Union[Unset, str]):
        filterupdated_atlte (Union[Unset, str]):
        filterstarted_atgt (Union[Unset, str]):
        filterstarted_atgte (Union[Unset, str]):
        filterstarted_atlt (Union[Unset, str]):
        filterstarted_atlte (Union[Unset, str]):
        filterdetected_atgt (Union[Unset, str]):
        filterdetected_atgte (Union[Unset, str]):
        filterdetected_atlt (Union[Unset, str]):
        filterdetected_atlte (Union[Unset, str]):
        filteracknowledged_atgt (Union[Unset, str]):
        filteracknowledged_atgte (Union[Unset, str]):
        filteracknowledged_atlt (Union[Unset, str]):
        filteracknowledged_atlte (Union[Unset, str]):
        filtermitigated_atgt (Union[Unset, str]):
        filtermitigated_atgte (Union[Unset, str]):
        filtermitigated_atlt (Union[Unset, str]):
        filtermitigated_atlte (Union[Unset, str]):
        filterresolved_atgt (Union[Unset, str]):
        filterresolved_atgte (Union[Unset, str]):
        filterresolved_atlt (Union[Unset, str]):
        filterresolved_atlte (Union[Unset, str]):
        filterclosed_atgt (Union[Unset, str]):
        filterclosed_atgte (Union[Unset, str]):
        filterclosed_atlt (Union[Unset, str]):
        filterclosed_atlte (Union[Unset, str]):
        filterin_triage_atgt (Union[Unset, str]):
        filterin_triage_atgte (Union[Unset, str]):
        filterin_triage_atlt (Union[Unset, str]):
        filterin_triage_atlte (Union[Unset, str]):
        filterkindeq (Union[Unset, str]):
        filterkindnot_eq (Union[Unset, str]):
        filterkindin (Union[Unset, str]):
        filterkindnot_in (Union[Unset, str]):
        filterstatuseq (Union[Unset, str]):
        filterstatusnot_eq (Union[Unset, str]):
        filterstatusin (Union[Unset, str]):
        filterstatusnot_in (Union[Unset, str]):
        filterprivateeq (Union[Unset, str]):
        filterprivatenot_eq (Union[Unset, str]):
        filterprivatein (Union[Unset, str]):
        filterprivatenot_in (Union[Unset, str]):
        filteruser_ideq (Union[Unset, str]):
        filteruser_idnot_eq (Union[Unset, str]):
        filteruser_idin (Union[Unset, str]):
        filteruser_idnot_in (Union[Unset, str]):
        filterseverityeq (Union[Unset, str]):
        filterseveritynot_eq (Union[Unset, str]):
        filterseverityin (Union[Unset, str]):
        filterseveritynot_in (Union[Unset, str]):
        filterseverity_ideq (Union[Unset, str]):
        filterseverity_idnot_eq (Union[Unset, str]):
        filterseverity_idin (Union[Unset, str]):
        filterseverity_idnot_in (Union[Unset, str]):
        filterlabelseq (Union[Unset, str]):
        filterlabelsnot_eq (Union[Unset, str]):
        filterlabelsin (Union[Unset, str]):
        filterlabelsnot_in (Union[Unset, str]):
        filterzendesk_ticket_ideq (Union[Unset, str]):
        filterzendesk_ticket_idnot_eq (Union[Unset, str]):
        filterzendesk_ticket_idin (Union[Unset, str]):
        filterzendesk_ticket_idnot_in (Union[Unset, str]):
        filtersequential_ideq (Union[Unset, str]):
        filtersequential_idnot_eq (Union[Unset, str]):
        filtersequential_idin (Union[Unset, str]):
        filtersequential_idnot_in (Union[Unset, str]):
        filtertypeseq (Union[Unset, str]):
        filtertypesnot_eq (Union[Unset, str]):
        filtertypesin (Union[Unset, str]):
        filtertypesnot_in (Union[Unset, str]):
        filtertype_idseq (Union[Unset, str]):
        filtertype_idsnot_eq (Union[Unset, str]):
        filtertype_idsin (Union[Unset, str]):
        filtertype_idsnot_in (Union[Unset, str]):
        filterenvironmentseq (Union[Unset, str]):
        filterenvironmentsnot_eq (Union[Unset, str]):
        filterenvironmentsin (Union[Unset, str]):
        filterenvironmentsnot_in (Union[Unset, str]):
        filterenvironment_idseq (Union[Unset, str]):
        filterenvironment_idsnot_eq (Union[Unset, str]):
        filterenvironment_idsin (Union[Unset, str]):
        filterenvironment_idsnot_in (Union[Unset, str]):
        filterserviceseq (Union[Unset, str]):
        filterservicesnot_eq (Union[Unset, str]):
        filterservicesin (Union[Unset, str]):
        filterservicesnot_in (Union[Unset, str]):
        filterservice_idseq (Union[Unset, str]):
        filterservice_idsnot_eq (Union[Unset, str]):
        filterservice_idsin (Union[Unset, str]):
        filterservice_idsnot_in (Union[Unset, str]):
        filterservice_nameseq (Union[Unset, str]):
        filterservice_namesnot_eq (Union[Unset, str]):
        filterservice_namesin (Union[Unset, str]):
        filterservice_namesnot_in (Union[Unset, str]):
        filterfunctionalitieseq (Union[Unset, str]):
        filterfunctionalitiesnot_eq (Union[Unset, str]):
        filterfunctionalitiesin (Union[Unset, str]):
        filterfunctionalitiesnot_in (Union[Unset, str]):
        filterfunctionality_idseq (Union[Unset, str]):
        filterfunctionality_idsnot_eq (Union[Unset, str]):
        filterfunctionality_idsin (Union[Unset, str]):
        filterfunctionality_idsnot_in (Union[Unset, str]):
        filterfunctionality_nameseq (Union[Unset, str]):
        filterfunctionality_namesnot_eq (Union[Unset, str]):
        filterfunctionality_namesin (Union[Unset, str]):
        filterfunctionality_namesnot_in (Union[Unset, str]):
        filtercauseseq (Union[Unset, str]):
        filtercausesnot_eq (Union[Unset, str]):
        filtercausesin (Union[Unset, str]):
        filtercausesnot_in (Union[Unset, str]):
        filtercause_idseq (Union[Unset, str]):
        filtercause_idsnot_eq (Union[Unset, str]):
        filtercause_idsin (Union[Unset, str]):
        filtercause_idsnot_in (Union[Unset, str]):
        filterteamseq (Union[Unset, str]):
        filterteamsnot_eq (Union[Unset, str]):
        filterteamsin (Union[Unset, str]):
        filterteamsnot_in (Union[Unset, str]):
        filterteam_idseq (Union[Unset, str]):
        filterteam_idsnot_eq (Union[Unset, str]):
        filterteam_idsin (Union[Unset, str]):
        filterteam_idsnot_in (Union[Unset, str]):
        filterteam_nameseq (Union[Unset, str]):
        filterteam_namesnot_eq (Union[Unset, str]):
        filterteam_namesin (Union[Unset, str]):
        filterteam_namesnot_in (Union[Unset, str]):
        sort (Union[Unset, ListIncidentsSort]):
        include (Union[Unset, ListIncidentsInclude]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, IncidentList]]
    """

    kwargs = _get_kwargs(
        pageafter=pageafter,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtersearch=filtersearch,
        filterkind=filterkind,
        filterstatus=filterstatus,
        filterprivate=filterprivate,
        filteruser_id=filteruser_id,
        filterseverity=filterseverity,
        filterseverity_id=filterseverity_id,
        filterlabels=filterlabels,
        filtertypes=filtertypes,
        filtertype_ids=filtertype_ids,
        filterenvironments=filterenvironments,
        filterenvironment_ids=filterenvironment_ids,
        filterfunctionalities=filterfunctionalities,
        filterfunctionality_ids=filterfunctionality_ids,
        filterfunctionality_names=filterfunctionality_names,
        filterservices=filterservices,
        filterservice_ids=filterservice_ids,
        filterservice_names=filterservice_names,
        filterteams=filterteams,
        filterteam_ids=filterteam_ids,
        filterteam_names=filterteam_names,
        filtercause=filtercause,
        filtercause_ids=filtercause_ids,
        filtercustom_field_selected_option_ids=filtercustom_field_selected_option_ids,
        filterslack_channel_id=filterslack_channel_id,
        filtersequential_id=filtersequential_id,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        filterupdated_atgt=filterupdated_atgt,
        filterupdated_atgte=filterupdated_atgte,
        filterupdated_atlt=filterupdated_atlt,
        filterupdated_atlte=filterupdated_atlte,
        filterstarted_atgt=filterstarted_atgt,
        filterstarted_atgte=filterstarted_atgte,
        filterstarted_atlt=filterstarted_atlt,
        filterstarted_atlte=filterstarted_atlte,
        filterdetected_atgt=filterdetected_atgt,
        filterdetected_atgte=filterdetected_atgte,
        filterdetected_atlt=filterdetected_atlt,
        filterdetected_atlte=filterdetected_atlte,
        filteracknowledged_atgt=filteracknowledged_atgt,
        filteracknowledged_atgte=filteracknowledged_atgte,
        filteracknowledged_atlt=filteracknowledged_atlt,
        filteracknowledged_atlte=filteracknowledged_atlte,
        filtermitigated_atgt=filtermitigated_atgt,
        filtermitigated_atgte=filtermitigated_atgte,
        filtermitigated_atlt=filtermitigated_atlt,
        filtermitigated_atlte=filtermitigated_atlte,
        filterresolved_atgt=filterresolved_atgt,
        filterresolved_atgte=filterresolved_atgte,
        filterresolved_atlt=filterresolved_atlt,
        filterresolved_atlte=filterresolved_atlte,
        filterclosed_atgt=filterclosed_atgt,
        filterclosed_atgte=filterclosed_atgte,
        filterclosed_atlt=filterclosed_atlt,
        filterclosed_atlte=filterclosed_atlte,
        filterin_triage_atgt=filterin_triage_atgt,
        filterin_triage_atgte=filterin_triage_atgte,
        filterin_triage_atlt=filterin_triage_atlt,
        filterin_triage_atlte=filterin_triage_atlte,
        filterkindeq=filterkindeq,
        filterkindnot_eq=filterkindnot_eq,
        filterkindin=filterkindin,
        filterkindnot_in=filterkindnot_in,
        filterstatuseq=filterstatuseq,
        filterstatusnot_eq=filterstatusnot_eq,
        filterstatusin=filterstatusin,
        filterstatusnot_in=filterstatusnot_in,
        filterprivateeq=filterprivateeq,
        filterprivatenot_eq=filterprivatenot_eq,
        filterprivatein=filterprivatein,
        filterprivatenot_in=filterprivatenot_in,
        filteruser_ideq=filteruser_ideq,
        filteruser_idnot_eq=filteruser_idnot_eq,
        filteruser_idin=filteruser_idin,
        filteruser_idnot_in=filteruser_idnot_in,
        filterseverityeq=filterseverityeq,
        filterseveritynot_eq=filterseveritynot_eq,
        filterseverityin=filterseverityin,
        filterseveritynot_in=filterseveritynot_in,
        filterseverity_ideq=filterseverity_ideq,
        filterseverity_idnot_eq=filterseverity_idnot_eq,
        filterseverity_idin=filterseverity_idin,
        filterseverity_idnot_in=filterseverity_idnot_in,
        filterlabelseq=filterlabelseq,
        filterlabelsnot_eq=filterlabelsnot_eq,
        filterlabelsin=filterlabelsin,
        filterlabelsnot_in=filterlabelsnot_in,
        filterzendesk_ticket_ideq=filterzendesk_ticket_ideq,
        filterzendesk_ticket_idnot_eq=filterzendesk_ticket_idnot_eq,
        filterzendesk_ticket_idin=filterzendesk_ticket_idin,
        filterzendesk_ticket_idnot_in=filterzendesk_ticket_idnot_in,
        filtersequential_ideq=filtersequential_ideq,
        filtersequential_idnot_eq=filtersequential_idnot_eq,
        filtersequential_idin=filtersequential_idin,
        filtersequential_idnot_in=filtersequential_idnot_in,
        filtertypeseq=filtertypeseq,
        filtertypesnot_eq=filtertypesnot_eq,
        filtertypesin=filtertypesin,
        filtertypesnot_in=filtertypesnot_in,
        filtertype_idseq=filtertype_idseq,
        filtertype_idsnot_eq=filtertype_idsnot_eq,
        filtertype_idsin=filtertype_idsin,
        filtertype_idsnot_in=filtertype_idsnot_in,
        filterenvironmentseq=filterenvironmentseq,
        filterenvironmentsnot_eq=filterenvironmentsnot_eq,
        filterenvironmentsin=filterenvironmentsin,
        filterenvironmentsnot_in=filterenvironmentsnot_in,
        filterenvironment_idseq=filterenvironment_idseq,
        filterenvironment_idsnot_eq=filterenvironment_idsnot_eq,
        filterenvironment_idsin=filterenvironment_idsin,
        filterenvironment_idsnot_in=filterenvironment_idsnot_in,
        filterserviceseq=filterserviceseq,
        filterservicesnot_eq=filterservicesnot_eq,
        filterservicesin=filterservicesin,
        filterservicesnot_in=filterservicesnot_in,
        filterservice_idseq=filterservice_idseq,
        filterservice_idsnot_eq=filterservice_idsnot_eq,
        filterservice_idsin=filterservice_idsin,
        filterservice_idsnot_in=filterservice_idsnot_in,
        filterservice_nameseq=filterservice_nameseq,
        filterservice_namesnot_eq=filterservice_namesnot_eq,
        filterservice_namesin=filterservice_namesin,
        filterservice_namesnot_in=filterservice_namesnot_in,
        filterfunctionalitieseq=filterfunctionalitieseq,
        filterfunctionalitiesnot_eq=filterfunctionalitiesnot_eq,
        filterfunctionalitiesin=filterfunctionalitiesin,
        filterfunctionalitiesnot_in=filterfunctionalitiesnot_in,
        filterfunctionality_idseq=filterfunctionality_idseq,
        filterfunctionality_idsnot_eq=filterfunctionality_idsnot_eq,
        filterfunctionality_idsin=filterfunctionality_idsin,
        filterfunctionality_idsnot_in=filterfunctionality_idsnot_in,
        filterfunctionality_nameseq=filterfunctionality_nameseq,
        filterfunctionality_namesnot_eq=filterfunctionality_namesnot_eq,
        filterfunctionality_namesin=filterfunctionality_namesin,
        filterfunctionality_namesnot_in=filterfunctionality_namesnot_in,
        filtercauseseq=filtercauseseq,
        filtercausesnot_eq=filtercausesnot_eq,
        filtercausesin=filtercausesin,
        filtercausesnot_in=filtercausesnot_in,
        filtercause_idseq=filtercause_idseq,
        filtercause_idsnot_eq=filtercause_idsnot_eq,
        filtercause_idsin=filtercause_idsin,
        filtercause_idsnot_in=filtercause_idsnot_in,
        filterteamseq=filterteamseq,
        filterteamsnot_eq=filterteamsnot_eq,
        filterteamsin=filterteamsin,
        filterteamsnot_in=filterteamsnot_in,
        filterteam_idseq=filterteam_idseq,
        filterteam_idsnot_eq=filterteam_idsnot_eq,
        filterteam_idsin=filterteam_idsin,
        filterteam_idsnot_in=filterteam_idsnot_in,
        filterteam_nameseq=filterteam_nameseq,
        filterteam_namesnot_eq=filterteam_namesnot_eq,
        filterteam_namesin=filterteam_namesin,
        filterteam_namesnot_in=filterteam_namesnot_in,
        sort=sort,
        include=include,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    pageafter: Union[Unset, str] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filtersearch: Union[Unset, str] = UNSET,
    filterkind: Union[Unset, str] = UNSET,
    filterstatus: Union[Unset, str] = UNSET,
    filterprivate: Union[Unset, str] = UNSET,
    filteruser_id: Union[Unset, int] = UNSET,
    filterseverity: Union[Unset, str] = UNSET,
    filterseverity_id: Union[Unset, str] = UNSET,
    filterlabels: Union[Unset, str] = UNSET,
    filtertypes: Union[Unset, str] = UNSET,
    filtertype_ids: Union[Unset, str] = UNSET,
    filterenvironments: Union[Unset, str] = UNSET,
    filterenvironment_ids: Union[Unset, str] = UNSET,
    filterfunctionalities: Union[Unset, str] = UNSET,
    filterfunctionality_ids: Union[Unset, str] = UNSET,
    filterfunctionality_names: Union[Unset, str] = UNSET,
    filterservices: Union[Unset, str] = UNSET,
    filterservice_ids: Union[Unset, str] = UNSET,
    filterservice_names: Union[Unset, str] = UNSET,
    filterteams: Union[Unset, str] = UNSET,
    filterteam_ids: Union[Unset, str] = UNSET,
    filterteam_names: Union[Unset, str] = UNSET,
    filtercause: Union[Unset, str] = UNSET,
    filtercause_ids: Union[Unset, str] = UNSET,
    filtercustom_field_selected_option_ids: Union[Unset, str] = UNSET,
    filterslack_channel_id: Union[Unset, str] = UNSET,
    filtersequential_id: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
    filterupdated_atgt: Union[Unset, str] = UNSET,
    filterupdated_atgte: Union[Unset, str] = UNSET,
    filterupdated_atlt: Union[Unset, str] = UNSET,
    filterupdated_atlte: Union[Unset, str] = UNSET,
    filterstarted_atgt: Union[Unset, str] = UNSET,
    filterstarted_atgte: Union[Unset, str] = UNSET,
    filterstarted_atlt: Union[Unset, str] = UNSET,
    filterstarted_atlte: Union[Unset, str] = UNSET,
    filterdetected_atgt: Union[Unset, str] = UNSET,
    filterdetected_atgte: Union[Unset, str] = UNSET,
    filterdetected_atlt: Union[Unset, str] = UNSET,
    filterdetected_atlte: Union[Unset, str] = UNSET,
    filteracknowledged_atgt: Union[Unset, str] = UNSET,
    filteracknowledged_atgte: Union[Unset, str] = UNSET,
    filteracknowledged_atlt: Union[Unset, str] = UNSET,
    filteracknowledged_atlte: Union[Unset, str] = UNSET,
    filtermitigated_atgt: Union[Unset, str] = UNSET,
    filtermitigated_atgte: Union[Unset, str] = UNSET,
    filtermitigated_atlt: Union[Unset, str] = UNSET,
    filtermitigated_atlte: Union[Unset, str] = UNSET,
    filterresolved_atgt: Union[Unset, str] = UNSET,
    filterresolved_atgte: Union[Unset, str] = UNSET,
    filterresolved_atlt: Union[Unset, str] = UNSET,
    filterresolved_atlte: Union[Unset, str] = UNSET,
    filterclosed_atgt: Union[Unset, str] = UNSET,
    filterclosed_atgte: Union[Unset, str] = UNSET,
    filterclosed_atlt: Union[Unset, str] = UNSET,
    filterclosed_atlte: Union[Unset, str] = UNSET,
    filterin_triage_atgt: Union[Unset, str] = UNSET,
    filterin_triage_atgte: Union[Unset, str] = UNSET,
    filterin_triage_atlt: Union[Unset, str] = UNSET,
    filterin_triage_atlte: Union[Unset, str] = UNSET,
    filterkindeq: Union[Unset, str] = UNSET,
    filterkindnot_eq: Union[Unset, str] = UNSET,
    filterkindin: Union[Unset, str] = UNSET,
    filterkindnot_in: Union[Unset, str] = UNSET,
    filterstatuseq: Union[Unset, str] = UNSET,
    filterstatusnot_eq: Union[Unset, str] = UNSET,
    filterstatusin: Union[Unset, str] = UNSET,
    filterstatusnot_in: Union[Unset, str] = UNSET,
    filterprivateeq: Union[Unset, str] = UNSET,
    filterprivatenot_eq: Union[Unset, str] = UNSET,
    filterprivatein: Union[Unset, str] = UNSET,
    filterprivatenot_in: Union[Unset, str] = UNSET,
    filteruser_ideq: Union[Unset, str] = UNSET,
    filteruser_idnot_eq: Union[Unset, str] = UNSET,
    filteruser_idin: Union[Unset, str] = UNSET,
    filteruser_idnot_in: Union[Unset, str] = UNSET,
    filterseverityeq: Union[Unset, str] = UNSET,
    filterseveritynot_eq: Union[Unset, str] = UNSET,
    filterseverityin: Union[Unset, str] = UNSET,
    filterseveritynot_in: Union[Unset, str] = UNSET,
    filterseverity_ideq: Union[Unset, str] = UNSET,
    filterseverity_idnot_eq: Union[Unset, str] = UNSET,
    filterseverity_idin: Union[Unset, str] = UNSET,
    filterseverity_idnot_in: Union[Unset, str] = UNSET,
    filterlabelseq: Union[Unset, str] = UNSET,
    filterlabelsnot_eq: Union[Unset, str] = UNSET,
    filterlabelsin: Union[Unset, str] = UNSET,
    filterlabelsnot_in: Union[Unset, str] = UNSET,
    filterzendesk_ticket_ideq: Union[Unset, str] = UNSET,
    filterzendesk_ticket_idnot_eq: Union[Unset, str] = UNSET,
    filterzendesk_ticket_idin: Union[Unset, str] = UNSET,
    filterzendesk_ticket_idnot_in: Union[Unset, str] = UNSET,
    filtersequential_ideq: Union[Unset, str] = UNSET,
    filtersequential_idnot_eq: Union[Unset, str] = UNSET,
    filtersequential_idin: Union[Unset, str] = UNSET,
    filtersequential_idnot_in: Union[Unset, str] = UNSET,
    filtertypeseq: Union[Unset, str] = UNSET,
    filtertypesnot_eq: Union[Unset, str] = UNSET,
    filtertypesin: Union[Unset, str] = UNSET,
    filtertypesnot_in: Union[Unset, str] = UNSET,
    filtertype_idseq: Union[Unset, str] = UNSET,
    filtertype_idsnot_eq: Union[Unset, str] = UNSET,
    filtertype_idsin: Union[Unset, str] = UNSET,
    filtertype_idsnot_in: Union[Unset, str] = UNSET,
    filterenvironmentseq: Union[Unset, str] = UNSET,
    filterenvironmentsnot_eq: Union[Unset, str] = UNSET,
    filterenvironmentsin: Union[Unset, str] = UNSET,
    filterenvironmentsnot_in: Union[Unset, str] = UNSET,
    filterenvironment_idseq: Union[Unset, str] = UNSET,
    filterenvironment_idsnot_eq: Union[Unset, str] = UNSET,
    filterenvironment_idsin: Union[Unset, str] = UNSET,
    filterenvironment_idsnot_in: Union[Unset, str] = UNSET,
    filterserviceseq: Union[Unset, str] = UNSET,
    filterservicesnot_eq: Union[Unset, str] = UNSET,
    filterservicesin: Union[Unset, str] = UNSET,
    filterservicesnot_in: Union[Unset, str] = UNSET,
    filterservice_idseq: Union[Unset, str] = UNSET,
    filterservice_idsnot_eq: Union[Unset, str] = UNSET,
    filterservice_idsin: Union[Unset, str] = UNSET,
    filterservice_idsnot_in: Union[Unset, str] = UNSET,
    filterservice_nameseq: Union[Unset, str] = UNSET,
    filterservice_namesnot_eq: Union[Unset, str] = UNSET,
    filterservice_namesin: Union[Unset, str] = UNSET,
    filterservice_namesnot_in: Union[Unset, str] = UNSET,
    filterfunctionalitieseq: Union[Unset, str] = UNSET,
    filterfunctionalitiesnot_eq: Union[Unset, str] = UNSET,
    filterfunctionalitiesin: Union[Unset, str] = UNSET,
    filterfunctionalitiesnot_in: Union[Unset, str] = UNSET,
    filterfunctionality_idseq: Union[Unset, str] = UNSET,
    filterfunctionality_idsnot_eq: Union[Unset, str] = UNSET,
    filterfunctionality_idsin: Union[Unset, str] = UNSET,
    filterfunctionality_idsnot_in: Union[Unset, str] = UNSET,
    filterfunctionality_nameseq: Union[Unset, str] = UNSET,
    filterfunctionality_namesnot_eq: Union[Unset, str] = UNSET,
    filterfunctionality_namesin: Union[Unset, str] = UNSET,
    filterfunctionality_namesnot_in: Union[Unset, str] = UNSET,
    filtercauseseq: Union[Unset, str] = UNSET,
    filtercausesnot_eq: Union[Unset, str] = UNSET,
    filtercausesin: Union[Unset, str] = UNSET,
    filtercausesnot_in: Union[Unset, str] = UNSET,
    filtercause_idseq: Union[Unset, str] = UNSET,
    filtercause_idsnot_eq: Union[Unset, str] = UNSET,
    filtercause_idsin: Union[Unset, str] = UNSET,
    filtercause_idsnot_in: Union[Unset, str] = UNSET,
    filterteamseq: Union[Unset, str] = UNSET,
    filterteamsnot_eq: Union[Unset, str] = UNSET,
    filterteamsin: Union[Unset, str] = UNSET,
    filterteamsnot_in: Union[Unset, str] = UNSET,
    filterteam_idseq: Union[Unset, str] = UNSET,
    filterteam_idsnot_eq: Union[Unset, str] = UNSET,
    filterteam_idsin: Union[Unset, str] = UNSET,
    filterteam_idsnot_in: Union[Unset, str] = UNSET,
    filterteam_nameseq: Union[Unset, str] = UNSET,
    filterteam_namesnot_eq: Union[Unset, str] = UNSET,
    filterteam_namesin: Union[Unset, str] = UNSET,
    filterteam_namesnot_in: Union[Unset, str] = UNSET,
    sort: Union[Unset, ListIncidentsSort] = UNSET,
    include: Union[Unset, ListIncidentsInclude] = UNSET,
) -> Optional[Union[ErrorsList, IncidentList]]:
    """List incidents

     List incidents

    Args:
        pageafter (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtersearch (Union[Unset, str]):
        filterkind (Union[Unset, str]):
        filterstatus (Union[Unset, str]):
        filterprivate (Union[Unset, str]):
        filteruser_id (Union[Unset, int]):
        filterseverity (Union[Unset, str]):
        filterseverity_id (Union[Unset, str]):
        filterlabels (Union[Unset, str]):
        filtertypes (Union[Unset, str]):
        filtertype_ids (Union[Unset, str]):
        filterenvironments (Union[Unset, str]):
        filterenvironment_ids (Union[Unset, str]):
        filterfunctionalities (Union[Unset, str]):
        filterfunctionality_ids (Union[Unset, str]):
        filterfunctionality_names (Union[Unset, str]):
        filterservices (Union[Unset, str]):
        filterservice_ids (Union[Unset, str]):
        filterservice_names (Union[Unset, str]):
        filterteams (Union[Unset, str]):
        filterteam_ids (Union[Unset, str]):
        filterteam_names (Union[Unset, str]):
        filtercause (Union[Unset, str]):
        filtercause_ids (Union[Unset, str]):
        filtercustom_field_selected_option_ids (Union[Unset, str]):
        filterslack_channel_id (Union[Unset, str]):
        filtersequential_id (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        filterupdated_atgt (Union[Unset, str]):
        filterupdated_atgte (Union[Unset, str]):
        filterupdated_atlt (Union[Unset, str]):
        filterupdated_atlte (Union[Unset, str]):
        filterstarted_atgt (Union[Unset, str]):
        filterstarted_atgte (Union[Unset, str]):
        filterstarted_atlt (Union[Unset, str]):
        filterstarted_atlte (Union[Unset, str]):
        filterdetected_atgt (Union[Unset, str]):
        filterdetected_atgte (Union[Unset, str]):
        filterdetected_atlt (Union[Unset, str]):
        filterdetected_atlte (Union[Unset, str]):
        filteracknowledged_atgt (Union[Unset, str]):
        filteracknowledged_atgte (Union[Unset, str]):
        filteracknowledged_atlt (Union[Unset, str]):
        filteracknowledged_atlte (Union[Unset, str]):
        filtermitigated_atgt (Union[Unset, str]):
        filtermitigated_atgte (Union[Unset, str]):
        filtermitigated_atlt (Union[Unset, str]):
        filtermitigated_atlte (Union[Unset, str]):
        filterresolved_atgt (Union[Unset, str]):
        filterresolved_atgte (Union[Unset, str]):
        filterresolved_atlt (Union[Unset, str]):
        filterresolved_atlte (Union[Unset, str]):
        filterclosed_atgt (Union[Unset, str]):
        filterclosed_atgte (Union[Unset, str]):
        filterclosed_atlt (Union[Unset, str]):
        filterclosed_atlte (Union[Unset, str]):
        filterin_triage_atgt (Union[Unset, str]):
        filterin_triage_atgte (Union[Unset, str]):
        filterin_triage_atlt (Union[Unset, str]):
        filterin_triage_atlte (Union[Unset, str]):
        filterkindeq (Union[Unset, str]):
        filterkindnot_eq (Union[Unset, str]):
        filterkindin (Union[Unset, str]):
        filterkindnot_in (Union[Unset, str]):
        filterstatuseq (Union[Unset, str]):
        filterstatusnot_eq (Union[Unset, str]):
        filterstatusin (Union[Unset, str]):
        filterstatusnot_in (Union[Unset, str]):
        filterprivateeq (Union[Unset, str]):
        filterprivatenot_eq (Union[Unset, str]):
        filterprivatein (Union[Unset, str]):
        filterprivatenot_in (Union[Unset, str]):
        filteruser_ideq (Union[Unset, str]):
        filteruser_idnot_eq (Union[Unset, str]):
        filteruser_idin (Union[Unset, str]):
        filteruser_idnot_in (Union[Unset, str]):
        filterseverityeq (Union[Unset, str]):
        filterseveritynot_eq (Union[Unset, str]):
        filterseverityin (Union[Unset, str]):
        filterseveritynot_in (Union[Unset, str]):
        filterseverity_ideq (Union[Unset, str]):
        filterseverity_idnot_eq (Union[Unset, str]):
        filterseverity_idin (Union[Unset, str]):
        filterseverity_idnot_in (Union[Unset, str]):
        filterlabelseq (Union[Unset, str]):
        filterlabelsnot_eq (Union[Unset, str]):
        filterlabelsin (Union[Unset, str]):
        filterlabelsnot_in (Union[Unset, str]):
        filterzendesk_ticket_ideq (Union[Unset, str]):
        filterzendesk_ticket_idnot_eq (Union[Unset, str]):
        filterzendesk_ticket_idin (Union[Unset, str]):
        filterzendesk_ticket_idnot_in (Union[Unset, str]):
        filtersequential_ideq (Union[Unset, str]):
        filtersequential_idnot_eq (Union[Unset, str]):
        filtersequential_idin (Union[Unset, str]):
        filtersequential_idnot_in (Union[Unset, str]):
        filtertypeseq (Union[Unset, str]):
        filtertypesnot_eq (Union[Unset, str]):
        filtertypesin (Union[Unset, str]):
        filtertypesnot_in (Union[Unset, str]):
        filtertype_idseq (Union[Unset, str]):
        filtertype_idsnot_eq (Union[Unset, str]):
        filtertype_idsin (Union[Unset, str]):
        filtertype_idsnot_in (Union[Unset, str]):
        filterenvironmentseq (Union[Unset, str]):
        filterenvironmentsnot_eq (Union[Unset, str]):
        filterenvironmentsin (Union[Unset, str]):
        filterenvironmentsnot_in (Union[Unset, str]):
        filterenvironment_idseq (Union[Unset, str]):
        filterenvironment_idsnot_eq (Union[Unset, str]):
        filterenvironment_idsin (Union[Unset, str]):
        filterenvironment_idsnot_in (Union[Unset, str]):
        filterserviceseq (Union[Unset, str]):
        filterservicesnot_eq (Union[Unset, str]):
        filterservicesin (Union[Unset, str]):
        filterservicesnot_in (Union[Unset, str]):
        filterservice_idseq (Union[Unset, str]):
        filterservice_idsnot_eq (Union[Unset, str]):
        filterservice_idsin (Union[Unset, str]):
        filterservice_idsnot_in (Union[Unset, str]):
        filterservice_nameseq (Union[Unset, str]):
        filterservice_namesnot_eq (Union[Unset, str]):
        filterservice_namesin (Union[Unset, str]):
        filterservice_namesnot_in (Union[Unset, str]):
        filterfunctionalitieseq (Union[Unset, str]):
        filterfunctionalitiesnot_eq (Union[Unset, str]):
        filterfunctionalitiesin (Union[Unset, str]):
        filterfunctionalitiesnot_in (Union[Unset, str]):
        filterfunctionality_idseq (Union[Unset, str]):
        filterfunctionality_idsnot_eq (Union[Unset, str]):
        filterfunctionality_idsin (Union[Unset, str]):
        filterfunctionality_idsnot_in (Union[Unset, str]):
        filterfunctionality_nameseq (Union[Unset, str]):
        filterfunctionality_namesnot_eq (Union[Unset, str]):
        filterfunctionality_namesin (Union[Unset, str]):
        filterfunctionality_namesnot_in (Union[Unset, str]):
        filtercauseseq (Union[Unset, str]):
        filtercausesnot_eq (Union[Unset, str]):
        filtercausesin (Union[Unset, str]):
        filtercausesnot_in (Union[Unset, str]):
        filtercause_idseq (Union[Unset, str]):
        filtercause_idsnot_eq (Union[Unset, str]):
        filtercause_idsin (Union[Unset, str]):
        filtercause_idsnot_in (Union[Unset, str]):
        filterteamseq (Union[Unset, str]):
        filterteamsnot_eq (Union[Unset, str]):
        filterteamsin (Union[Unset, str]):
        filterteamsnot_in (Union[Unset, str]):
        filterteam_idseq (Union[Unset, str]):
        filterteam_idsnot_eq (Union[Unset, str]):
        filterteam_idsin (Union[Unset, str]):
        filterteam_idsnot_in (Union[Unset, str]):
        filterteam_nameseq (Union[Unset, str]):
        filterteam_namesnot_eq (Union[Unset, str]):
        filterteam_namesin (Union[Unset, str]):
        filterteam_namesnot_in (Union[Unset, str]):
        sort (Union[Unset, ListIncidentsSort]):
        include (Union[Unset, ListIncidentsInclude]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, IncidentList]
    """

    return (
        await asyncio_detailed(
            client=client,
            pageafter=pageafter,
            pagenumber=pagenumber,
            pagesize=pagesize,
            filtersearch=filtersearch,
            filterkind=filterkind,
            filterstatus=filterstatus,
            filterprivate=filterprivate,
            filteruser_id=filteruser_id,
            filterseverity=filterseverity,
            filterseverity_id=filterseverity_id,
            filterlabels=filterlabels,
            filtertypes=filtertypes,
            filtertype_ids=filtertype_ids,
            filterenvironments=filterenvironments,
            filterenvironment_ids=filterenvironment_ids,
            filterfunctionalities=filterfunctionalities,
            filterfunctionality_ids=filterfunctionality_ids,
            filterfunctionality_names=filterfunctionality_names,
            filterservices=filterservices,
            filterservice_ids=filterservice_ids,
            filterservice_names=filterservice_names,
            filterteams=filterteams,
            filterteam_ids=filterteam_ids,
            filterteam_names=filterteam_names,
            filtercause=filtercause,
            filtercause_ids=filtercause_ids,
            filtercustom_field_selected_option_ids=filtercustom_field_selected_option_ids,
            filterslack_channel_id=filterslack_channel_id,
            filtersequential_id=filtersequential_id,
            filtercreated_atgt=filtercreated_atgt,
            filtercreated_atgte=filtercreated_atgte,
            filtercreated_atlt=filtercreated_atlt,
            filtercreated_atlte=filtercreated_atlte,
            filterupdated_atgt=filterupdated_atgt,
            filterupdated_atgte=filterupdated_atgte,
            filterupdated_atlt=filterupdated_atlt,
            filterupdated_atlte=filterupdated_atlte,
            filterstarted_atgt=filterstarted_atgt,
            filterstarted_atgte=filterstarted_atgte,
            filterstarted_atlt=filterstarted_atlt,
            filterstarted_atlte=filterstarted_atlte,
            filterdetected_atgt=filterdetected_atgt,
            filterdetected_atgte=filterdetected_atgte,
            filterdetected_atlt=filterdetected_atlt,
            filterdetected_atlte=filterdetected_atlte,
            filteracknowledged_atgt=filteracknowledged_atgt,
            filteracknowledged_atgte=filteracknowledged_atgte,
            filteracknowledged_atlt=filteracknowledged_atlt,
            filteracknowledged_atlte=filteracknowledged_atlte,
            filtermitigated_atgt=filtermitigated_atgt,
            filtermitigated_atgte=filtermitigated_atgte,
            filtermitigated_atlt=filtermitigated_atlt,
            filtermitigated_atlte=filtermitigated_atlte,
            filterresolved_atgt=filterresolved_atgt,
            filterresolved_atgte=filterresolved_atgte,
            filterresolved_atlt=filterresolved_atlt,
            filterresolved_atlte=filterresolved_atlte,
            filterclosed_atgt=filterclosed_atgt,
            filterclosed_atgte=filterclosed_atgte,
            filterclosed_atlt=filterclosed_atlt,
            filterclosed_atlte=filterclosed_atlte,
            filterin_triage_atgt=filterin_triage_atgt,
            filterin_triage_atgte=filterin_triage_atgte,
            filterin_triage_atlt=filterin_triage_atlt,
            filterin_triage_atlte=filterin_triage_atlte,
            filterkindeq=filterkindeq,
            filterkindnot_eq=filterkindnot_eq,
            filterkindin=filterkindin,
            filterkindnot_in=filterkindnot_in,
            filterstatuseq=filterstatuseq,
            filterstatusnot_eq=filterstatusnot_eq,
            filterstatusin=filterstatusin,
            filterstatusnot_in=filterstatusnot_in,
            filterprivateeq=filterprivateeq,
            filterprivatenot_eq=filterprivatenot_eq,
            filterprivatein=filterprivatein,
            filterprivatenot_in=filterprivatenot_in,
            filteruser_ideq=filteruser_ideq,
            filteruser_idnot_eq=filteruser_idnot_eq,
            filteruser_idin=filteruser_idin,
            filteruser_idnot_in=filteruser_idnot_in,
            filterseverityeq=filterseverityeq,
            filterseveritynot_eq=filterseveritynot_eq,
            filterseverityin=filterseverityin,
            filterseveritynot_in=filterseveritynot_in,
            filterseverity_ideq=filterseverity_ideq,
            filterseverity_idnot_eq=filterseverity_idnot_eq,
            filterseverity_idin=filterseverity_idin,
            filterseverity_idnot_in=filterseverity_idnot_in,
            filterlabelseq=filterlabelseq,
            filterlabelsnot_eq=filterlabelsnot_eq,
            filterlabelsin=filterlabelsin,
            filterlabelsnot_in=filterlabelsnot_in,
            filterzendesk_ticket_ideq=filterzendesk_ticket_ideq,
            filterzendesk_ticket_idnot_eq=filterzendesk_ticket_idnot_eq,
            filterzendesk_ticket_idin=filterzendesk_ticket_idin,
            filterzendesk_ticket_idnot_in=filterzendesk_ticket_idnot_in,
            filtersequential_ideq=filtersequential_ideq,
            filtersequential_idnot_eq=filtersequential_idnot_eq,
            filtersequential_idin=filtersequential_idin,
            filtersequential_idnot_in=filtersequential_idnot_in,
            filtertypeseq=filtertypeseq,
            filtertypesnot_eq=filtertypesnot_eq,
            filtertypesin=filtertypesin,
            filtertypesnot_in=filtertypesnot_in,
            filtertype_idseq=filtertype_idseq,
            filtertype_idsnot_eq=filtertype_idsnot_eq,
            filtertype_idsin=filtertype_idsin,
            filtertype_idsnot_in=filtertype_idsnot_in,
            filterenvironmentseq=filterenvironmentseq,
            filterenvironmentsnot_eq=filterenvironmentsnot_eq,
            filterenvironmentsin=filterenvironmentsin,
            filterenvironmentsnot_in=filterenvironmentsnot_in,
            filterenvironment_idseq=filterenvironment_idseq,
            filterenvironment_idsnot_eq=filterenvironment_idsnot_eq,
            filterenvironment_idsin=filterenvironment_idsin,
            filterenvironment_idsnot_in=filterenvironment_idsnot_in,
            filterserviceseq=filterserviceseq,
            filterservicesnot_eq=filterservicesnot_eq,
            filterservicesin=filterservicesin,
            filterservicesnot_in=filterservicesnot_in,
            filterservice_idseq=filterservice_idseq,
            filterservice_idsnot_eq=filterservice_idsnot_eq,
            filterservice_idsin=filterservice_idsin,
            filterservice_idsnot_in=filterservice_idsnot_in,
            filterservice_nameseq=filterservice_nameseq,
            filterservice_namesnot_eq=filterservice_namesnot_eq,
            filterservice_namesin=filterservice_namesin,
            filterservice_namesnot_in=filterservice_namesnot_in,
            filterfunctionalitieseq=filterfunctionalitieseq,
            filterfunctionalitiesnot_eq=filterfunctionalitiesnot_eq,
            filterfunctionalitiesin=filterfunctionalitiesin,
            filterfunctionalitiesnot_in=filterfunctionalitiesnot_in,
            filterfunctionality_idseq=filterfunctionality_idseq,
            filterfunctionality_idsnot_eq=filterfunctionality_idsnot_eq,
            filterfunctionality_idsin=filterfunctionality_idsin,
            filterfunctionality_idsnot_in=filterfunctionality_idsnot_in,
            filterfunctionality_nameseq=filterfunctionality_nameseq,
            filterfunctionality_namesnot_eq=filterfunctionality_namesnot_eq,
            filterfunctionality_namesin=filterfunctionality_namesin,
            filterfunctionality_namesnot_in=filterfunctionality_namesnot_in,
            filtercauseseq=filtercauseseq,
            filtercausesnot_eq=filtercausesnot_eq,
            filtercausesin=filtercausesin,
            filtercausesnot_in=filtercausesnot_in,
            filtercause_idseq=filtercause_idseq,
            filtercause_idsnot_eq=filtercause_idsnot_eq,
            filtercause_idsin=filtercause_idsin,
            filtercause_idsnot_in=filtercause_idsnot_in,
            filterteamseq=filterteamseq,
            filterteamsnot_eq=filterteamsnot_eq,
            filterteamsin=filterteamsin,
            filterteamsnot_in=filterteamsnot_in,
            filterteam_idseq=filterteam_idseq,
            filterteam_idsnot_eq=filterteam_idsnot_eq,
            filterteam_idsin=filterteam_idsin,
            filterteam_idsnot_in=filterteam_idsnot_in,
            filterteam_nameseq=filterteam_nameseq,
            filterteam_namesnot_eq=filterteam_namesnot_eq,
            filterteam_namesin=filterteam_namesin,
            filterteam_namesnot_in=filterteam_namesnot_in,
            sort=sort,
            include=include,
        )
    ).parsed
