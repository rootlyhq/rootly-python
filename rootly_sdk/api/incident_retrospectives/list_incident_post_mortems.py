from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.incident_post_mortem_list import IncidentPostMortemList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtersearch: str | Unset = UNSET,
    filterstatus: str | Unset = UNSET,
    filterseverity: str | Unset = UNSET,
    filtertype: str | Unset = UNSET,
    filteruser_id: int | Unset = UNSET,
    filtertypes: str | Unset = UNSET,
    filtertype_ids: str | Unset = UNSET,
    filterenvironments: str | Unset = UNSET,
    filterenvironment_ids: str | Unset = UNSET,
    filterfunctionalities: str | Unset = UNSET,
    filterfunctionality_ids: str | Unset = UNSET,
    filterservices: str | Unset = UNSET,
    filterservice_ids: str | Unset = UNSET,
    filterteams: str | Unset = UNSET,
    filterteam_ids: str | Unset = UNSET,
    filtercauses: str | Unset = UNSET,
    filtercause_ids: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filterstarted_atgt: str | Unset = UNSET,
    filterstarted_atgte: str | Unset = UNSET,
    filterstarted_atlt: str | Unset = UNSET,
    filterstarted_atlte: str | Unset = UNSET,
    filtermitigated_atgt: str | Unset = UNSET,
    filtermitigated_atgte: str | Unset = UNSET,
    filtermitigated_atlt: str | Unset = UNSET,
    filtermitigated_atlte: str | Unset = UNSET,
    filterresolved_atgt: str | Unset = UNSET,
    filterresolved_atgte: str | Unset = UNSET,
    filterresolved_atlt: str | Unset = UNSET,
    filterresolved_atlte: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["include"] = include

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize

    params["filter[search]"] = filtersearch

    params["filter[status]"] = filterstatus

    params["filter[severity]"] = filterseverity

    params["filter[type]"] = filtertype

    params["filter[user_id]"] = filteruser_id

    params["filter[types]"] = filtertypes

    params["filter[type_ids]"] = filtertype_ids

    params["filter[environments]"] = filterenvironments

    params["filter[environment_ids]"] = filterenvironment_ids

    params["filter[functionalities]"] = filterfunctionalities

    params["filter[functionality_ids]"] = filterfunctionality_ids

    params["filter[services]"] = filterservices

    params["filter[service_ids]"] = filterservice_ids

    params["filter[teams]"] = filterteams

    params["filter[team_ids]"] = filterteam_ids

    params["filter[causes]"] = filtercauses

    params["filter[cause_ids]"] = filtercause_ids

    params["filter[created_at][gt]"] = filtercreated_atgt

    params["filter[created_at][gte]"] = filtercreated_atgte

    params["filter[created_at][lt]"] = filtercreated_atlt

    params["filter[created_at][lte]"] = filtercreated_atlte

    params["filter[started_at][gt]"] = filterstarted_atgt

    params["filter[started_at][gte]"] = filterstarted_atgte

    params["filter[started_at][lt]"] = filterstarted_atlt

    params["filter[started_at][lte]"] = filterstarted_atlte

    params["filter[mitigated_at][gt]"] = filtermitigated_atgt

    params["filter[mitigated_at][gte]"] = filtermitigated_atgte

    params["filter[mitigated_at][lt]"] = filtermitigated_atlt

    params["filter[mitigated_at][lte]"] = filtermitigated_atlte

    params["filter[resolved_at][gt]"] = filterresolved_atgt

    params["filter[resolved_at][gte]"] = filterresolved_atgte

    params["filter[resolved_at][lt]"] = filterresolved_atlt

    params["filter[resolved_at][lte]"] = filterresolved_atlte

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/post_mortems",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> IncidentPostMortemList | None:
    if response.status_code == 200:
        response_200 = IncidentPostMortemList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[IncidentPostMortemList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    include: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtersearch: str | Unset = UNSET,
    filterstatus: str | Unset = UNSET,
    filterseverity: str | Unset = UNSET,
    filtertype: str | Unset = UNSET,
    filteruser_id: int | Unset = UNSET,
    filtertypes: str | Unset = UNSET,
    filtertype_ids: str | Unset = UNSET,
    filterenvironments: str | Unset = UNSET,
    filterenvironment_ids: str | Unset = UNSET,
    filterfunctionalities: str | Unset = UNSET,
    filterfunctionality_ids: str | Unset = UNSET,
    filterservices: str | Unset = UNSET,
    filterservice_ids: str | Unset = UNSET,
    filterteams: str | Unset = UNSET,
    filterteam_ids: str | Unset = UNSET,
    filtercauses: str | Unset = UNSET,
    filtercause_ids: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filterstarted_atgt: str | Unset = UNSET,
    filterstarted_atgte: str | Unset = UNSET,
    filterstarted_atlt: str | Unset = UNSET,
    filterstarted_atlte: str | Unset = UNSET,
    filtermitigated_atgt: str | Unset = UNSET,
    filtermitigated_atgte: str | Unset = UNSET,
    filtermitigated_atlt: str | Unset = UNSET,
    filtermitigated_atlte: str | Unset = UNSET,
    filterresolved_atgt: str | Unset = UNSET,
    filterresolved_atgte: str | Unset = UNSET,
    filterresolved_atlt: str | Unset = UNSET,
    filterresolved_atlte: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Response[IncidentPostMortemList]:
    """List incident retrospectives

     List incident retrospectives

    Args:
        include (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtersearch (str | Unset):
        filterstatus (str | Unset):
        filterseverity (str | Unset):
        filtertype (str | Unset):
        filteruser_id (int | Unset):
        filtertypes (str | Unset):
        filtertype_ids (str | Unset):
        filterenvironments (str | Unset):
        filterenvironment_ids (str | Unset):
        filterfunctionalities (str | Unset):
        filterfunctionality_ids (str | Unset):
        filterservices (str | Unset):
        filterservice_ids (str | Unset):
        filterteams (str | Unset):
        filterteam_ids (str | Unset):
        filtercauses (str | Unset):
        filtercause_ids (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        filterstarted_atgt (str | Unset):
        filterstarted_atgte (str | Unset):
        filterstarted_atlt (str | Unset):
        filterstarted_atlte (str | Unset):
        filtermitigated_atgt (str | Unset):
        filtermitigated_atgte (str | Unset):
        filtermitigated_atlt (str | Unset):
        filtermitigated_atlte (str | Unset):
        filterresolved_atgt (str | Unset):
        filterresolved_atgte (str | Unset):
        filterresolved_atlt (str | Unset):
        filterresolved_atlte (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentPostMortemList]
    """

    kwargs = _get_kwargs(
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtersearch=filtersearch,
        filterstatus=filterstatus,
        filterseverity=filterseverity,
        filtertype=filtertype,
        filteruser_id=filteruser_id,
        filtertypes=filtertypes,
        filtertype_ids=filtertype_ids,
        filterenvironments=filterenvironments,
        filterenvironment_ids=filterenvironment_ids,
        filterfunctionalities=filterfunctionalities,
        filterfunctionality_ids=filterfunctionality_ids,
        filterservices=filterservices,
        filterservice_ids=filterservice_ids,
        filterteams=filterteams,
        filterteam_ids=filterteam_ids,
        filtercauses=filtercauses,
        filtercause_ids=filtercause_ids,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        filterstarted_atgt=filterstarted_atgt,
        filterstarted_atgte=filterstarted_atgte,
        filterstarted_atlt=filterstarted_atlt,
        filterstarted_atlte=filterstarted_atlte,
        filtermitigated_atgt=filtermitigated_atgt,
        filtermitigated_atgte=filtermitigated_atgte,
        filtermitigated_atlt=filtermitigated_atlt,
        filtermitigated_atlte=filtermitigated_atlte,
        filterresolved_atgt=filterresolved_atgt,
        filterresolved_atgte=filterresolved_atgte,
        filterresolved_atlt=filterresolved_atlt,
        filterresolved_atlte=filterresolved_atlte,
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    include: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtersearch: str | Unset = UNSET,
    filterstatus: str | Unset = UNSET,
    filterseverity: str | Unset = UNSET,
    filtertype: str | Unset = UNSET,
    filteruser_id: int | Unset = UNSET,
    filtertypes: str | Unset = UNSET,
    filtertype_ids: str | Unset = UNSET,
    filterenvironments: str | Unset = UNSET,
    filterenvironment_ids: str | Unset = UNSET,
    filterfunctionalities: str | Unset = UNSET,
    filterfunctionality_ids: str | Unset = UNSET,
    filterservices: str | Unset = UNSET,
    filterservice_ids: str | Unset = UNSET,
    filterteams: str | Unset = UNSET,
    filterteam_ids: str | Unset = UNSET,
    filtercauses: str | Unset = UNSET,
    filtercause_ids: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filterstarted_atgt: str | Unset = UNSET,
    filterstarted_atgte: str | Unset = UNSET,
    filterstarted_atlt: str | Unset = UNSET,
    filterstarted_atlte: str | Unset = UNSET,
    filtermitigated_atgt: str | Unset = UNSET,
    filtermitigated_atgte: str | Unset = UNSET,
    filtermitigated_atlt: str | Unset = UNSET,
    filtermitigated_atlte: str | Unset = UNSET,
    filterresolved_atgt: str | Unset = UNSET,
    filterresolved_atgte: str | Unset = UNSET,
    filterresolved_atlt: str | Unset = UNSET,
    filterresolved_atlte: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> IncidentPostMortemList | None:
    """List incident retrospectives

     List incident retrospectives

    Args:
        include (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtersearch (str | Unset):
        filterstatus (str | Unset):
        filterseverity (str | Unset):
        filtertype (str | Unset):
        filteruser_id (int | Unset):
        filtertypes (str | Unset):
        filtertype_ids (str | Unset):
        filterenvironments (str | Unset):
        filterenvironment_ids (str | Unset):
        filterfunctionalities (str | Unset):
        filterfunctionality_ids (str | Unset):
        filterservices (str | Unset):
        filterservice_ids (str | Unset):
        filterteams (str | Unset):
        filterteam_ids (str | Unset):
        filtercauses (str | Unset):
        filtercause_ids (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        filterstarted_atgt (str | Unset):
        filterstarted_atgte (str | Unset):
        filterstarted_atlt (str | Unset):
        filterstarted_atlte (str | Unset):
        filtermitigated_atgt (str | Unset):
        filtermitigated_atgte (str | Unset):
        filtermitigated_atlt (str | Unset):
        filtermitigated_atlte (str | Unset):
        filterresolved_atgt (str | Unset):
        filterresolved_atgte (str | Unset):
        filterresolved_atlt (str | Unset):
        filterresolved_atlte (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentPostMortemList
    """

    return sync_detailed(
        client=client,
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtersearch=filtersearch,
        filterstatus=filterstatus,
        filterseverity=filterseverity,
        filtertype=filtertype,
        filteruser_id=filteruser_id,
        filtertypes=filtertypes,
        filtertype_ids=filtertype_ids,
        filterenvironments=filterenvironments,
        filterenvironment_ids=filterenvironment_ids,
        filterfunctionalities=filterfunctionalities,
        filterfunctionality_ids=filterfunctionality_ids,
        filterservices=filterservices,
        filterservice_ids=filterservice_ids,
        filterteams=filterteams,
        filterteam_ids=filterteam_ids,
        filtercauses=filtercauses,
        filtercause_ids=filtercause_ids,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        filterstarted_atgt=filterstarted_atgt,
        filterstarted_atgte=filterstarted_atgte,
        filterstarted_atlt=filterstarted_atlt,
        filterstarted_atlte=filterstarted_atlte,
        filtermitigated_atgt=filtermitigated_atgt,
        filtermitigated_atgte=filtermitigated_atgte,
        filtermitigated_atlt=filtermitigated_atlt,
        filtermitigated_atlte=filtermitigated_atlte,
        filterresolved_atgt=filterresolved_atgt,
        filterresolved_atgte=filterresolved_atgte,
        filterresolved_atlt=filterresolved_atlt,
        filterresolved_atlte=filterresolved_atlte,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    include: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtersearch: str | Unset = UNSET,
    filterstatus: str | Unset = UNSET,
    filterseverity: str | Unset = UNSET,
    filtertype: str | Unset = UNSET,
    filteruser_id: int | Unset = UNSET,
    filtertypes: str | Unset = UNSET,
    filtertype_ids: str | Unset = UNSET,
    filterenvironments: str | Unset = UNSET,
    filterenvironment_ids: str | Unset = UNSET,
    filterfunctionalities: str | Unset = UNSET,
    filterfunctionality_ids: str | Unset = UNSET,
    filterservices: str | Unset = UNSET,
    filterservice_ids: str | Unset = UNSET,
    filterteams: str | Unset = UNSET,
    filterteam_ids: str | Unset = UNSET,
    filtercauses: str | Unset = UNSET,
    filtercause_ids: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filterstarted_atgt: str | Unset = UNSET,
    filterstarted_atgte: str | Unset = UNSET,
    filterstarted_atlt: str | Unset = UNSET,
    filterstarted_atlte: str | Unset = UNSET,
    filtermitigated_atgt: str | Unset = UNSET,
    filtermitigated_atgte: str | Unset = UNSET,
    filtermitigated_atlt: str | Unset = UNSET,
    filtermitigated_atlte: str | Unset = UNSET,
    filterresolved_atgt: str | Unset = UNSET,
    filterresolved_atgte: str | Unset = UNSET,
    filterresolved_atlt: str | Unset = UNSET,
    filterresolved_atlte: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Response[IncidentPostMortemList]:
    """List incident retrospectives

     List incident retrospectives

    Args:
        include (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtersearch (str | Unset):
        filterstatus (str | Unset):
        filterseverity (str | Unset):
        filtertype (str | Unset):
        filteruser_id (int | Unset):
        filtertypes (str | Unset):
        filtertype_ids (str | Unset):
        filterenvironments (str | Unset):
        filterenvironment_ids (str | Unset):
        filterfunctionalities (str | Unset):
        filterfunctionality_ids (str | Unset):
        filterservices (str | Unset):
        filterservice_ids (str | Unset):
        filterteams (str | Unset):
        filterteam_ids (str | Unset):
        filtercauses (str | Unset):
        filtercause_ids (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        filterstarted_atgt (str | Unset):
        filterstarted_atgte (str | Unset):
        filterstarted_atlt (str | Unset):
        filterstarted_atlte (str | Unset):
        filtermitigated_atgt (str | Unset):
        filtermitigated_atgte (str | Unset):
        filtermitigated_atlt (str | Unset):
        filtermitigated_atlte (str | Unset):
        filterresolved_atgt (str | Unset):
        filterresolved_atgte (str | Unset):
        filterresolved_atlt (str | Unset):
        filterresolved_atlte (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentPostMortemList]
    """

    kwargs = _get_kwargs(
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtersearch=filtersearch,
        filterstatus=filterstatus,
        filterseverity=filterseverity,
        filtertype=filtertype,
        filteruser_id=filteruser_id,
        filtertypes=filtertypes,
        filtertype_ids=filtertype_ids,
        filterenvironments=filterenvironments,
        filterenvironment_ids=filterenvironment_ids,
        filterfunctionalities=filterfunctionalities,
        filterfunctionality_ids=filterfunctionality_ids,
        filterservices=filterservices,
        filterservice_ids=filterservice_ids,
        filterteams=filterteams,
        filterteam_ids=filterteam_ids,
        filtercauses=filtercauses,
        filtercause_ids=filtercause_ids,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        filterstarted_atgt=filterstarted_atgt,
        filterstarted_atgte=filterstarted_atgte,
        filterstarted_atlt=filterstarted_atlt,
        filterstarted_atlte=filterstarted_atlte,
        filtermitigated_atgt=filtermitigated_atgt,
        filtermitigated_atgte=filtermitigated_atgte,
        filtermitigated_atlt=filtermitigated_atlt,
        filtermitigated_atlte=filtermitigated_atlte,
        filterresolved_atgt=filterresolved_atgt,
        filterresolved_atgte=filterresolved_atgte,
        filterresolved_atlt=filterresolved_atlt,
        filterresolved_atlte=filterresolved_atlte,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    include: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtersearch: str | Unset = UNSET,
    filterstatus: str | Unset = UNSET,
    filterseverity: str | Unset = UNSET,
    filtertype: str | Unset = UNSET,
    filteruser_id: int | Unset = UNSET,
    filtertypes: str | Unset = UNSET,
    filtertype_ids: str | Unset = UNSET,
    filterenvironments: str | Unset = UNSET,
    filterenvironment_ids: str | Unset = UNSET,
    filterfunctionalities: str | Unset = UNSET,
    filterfunctionality_ids: str | Unset = UNSET,
    filterservices: str | Unset = UNSET,
    filterservice_ids: str | Unset = UNSET,
    filterteams: str | Unset = UNSET,
    filterteam_ids: str | Unset = UNSET,
    filtercauses: str | Unset = UNSET,
    filtercause_ids: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filterstarted_atgt: str | Unset = UNSET,
    filterstarted_atgte: str | Unset = UNSET,
    filterstarted_atlt: str | Unset = UNSET,
    filterstarted_atlte: str | Unset = UNSET,
    filtermitigated_atgt: str | Unset = UNSET,
    filtermitigated_atgte: str | Unset = UNSET,
    filtermitigated_atlt: str | Unset = UNSET,
    filtermitigated_atlte: str | Unset = UNSET,
    filterresolved_atgt: str | Unset = UNSET,
    filterresolved_atgte: str | Unset = UNSET,
    filterresolved_atlt: str | Unset = UNSET,
    filterresolved_atlte: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> IncidentPostMortemList | None:
    """List incident retrospectives

     List incident retrospectives

    Args:
        include (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtersearch (str | Unset):
        filterstatus (str | Unset):
        filterseverity (str | Unset):
        filtertype (str | Unset):
        filteruser_id (int | Unset):
        filtertypes (str | Unset):
        filtertype_ids (str | Unset):
        filterenvironments (str | Unset):
        filterenvironment_ids (str | Unset):
        filterfunctionalities (str | Unset):
        filterfunctionality_ids (str | Unset):
        filterservices (str | Unset):
        filterservice_ids (str | Unset):
        filterteams (str | Unset):
        filterteam_ids (str | Unset):
        filtercauses (str | Unset):
        filtercause_ids (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        filterstarted_atgt (str | Unset):
        filterstarted_atgte (str | Unset):
        filterstarted_atlt (str | Unset):
        filterstarted_atlte (str | Unset):
        filtermitigated_atgt (str | Unset):
        filtermitigated_atgte (str | Unset):
        filtermitigated_atlt (str | Unset):
        filtermitigated_atlte (str | Unset):
        filterresolved_atgt (str | Unset):
        filterresolved_atgte (str | Unset):
        filterresolved_atlt (str | Unset):
        filterresolved_atlte (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentPostMortemList
    """

    return (
        await asyncio_detailed(
            client=client,
            include=include,
            pagenumber=pagenumber,
            pagesize=pagesize,
            filtersearch=filtersearch,
            filterstatus=filterstatus,
            filterseverity=filterseverity,
            filtertype=filtertype,
            filteruser_id=filteruser_id,
            filtertypes=filtertypes,
            filtertype_ids=filtertype_ids,
            filterenvironments=filterenvironments,
            filterenvironment_ids=filterenvironment_ids,
            filterfunctionalities=filterfunctionalities,
            filterfunctionality_ids=filterfunctionality_ids,
            filterservices=filterservices,
            filterservice_ids=filterservice_ids,
            filterteams=filterteams,
            filterteam_ids=filterteam_ids,
            filtercauses=filtercauses,
            filtercause_ids=filtercause_ids,
            filtercreated_atgt=filtercreated_atgt,
            filtercreated_atgte=filtercreated_atgte,
            filtercreated_atlt=filtercreated_atlt,
            filtercreated_atlte=filtercreated_atlte,
            filterstarted_atgt=filterstarted_atgt,
            filterstarted_atgte=filterstarted_atgte,
            filterstarted_atlt=filterstarted_atlt,
            filterstarted_atlte=filterstarted_atlte,
            filtermitigated_atgt=filtermitigated_atgt,
            filtermitigated_atgte=filtermitigated_atgte,
            filtermitigated_atlt=filtermitigated_atlt,
            filtermitigated_atlte=filtermitigated_atlte,
            filterresolved_atgt=filterresolved_atgt,
            filterresolved_atgte=filterresolved_atgte,
            filterresolved_atlt=filterresolved_atlt,
            filterresolved_atlte=filterresolved_atlte,
            sort=sort,
        )
    ).parsed
