from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_teams_include import ListTeamsInclude
from ...models.team_list import TeamList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include: ListTeamsInclude | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtersearch: str | Unset = UNSET,
    filterslug: str | Unset = UNSET,
    filtername: str | Unset = UNSET,
    filterbackstage_id: str | Unset = UNSET,
    filtercortex_id: str | Unset = UNSET,
    filteropslevel_id: str | Unset = UNSET,
    filterexternal_id: str | Unset = UNSET,
    filtercolor: str | Unset = UNSET,
    filteralert_broadcast_enabled: bool | Unset = UNSET,
    filterincident_broadcast_enabled: bool | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_include: str | Unset = UNSET
    if not isinstance(include, Unset):
        json_include = include

    params["include"] = json_include

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize

    params["filter[search]"] = filtersearch

    params["filter[slug]"] = filterslug

    params["filter[name]"] = filtername

    params["filter[backstage_id]"] = filterbackstage_id

    params["filter[cortex_id]"] = filtercortex_id

    params["filter[opslevel_id]"] = filteropslevel_id

    params["filter[external_id]"] = filterexternal_id

    params["filter[color]"] = filtercolor

    params["filter[alert_broadcast_enabled]"] = filteralert_broadcast_enabled

    params["filter[incident_broadcast_enabled]"] = filterincident_broadcast_enabled

    params["filter[created_at][gt]"] = filtercreated_atgt

    params["filter[created_at][gte]"] = filtercreated_atgte

    params["filter[created_at][lt]"] = filtercreated_atlt

    params["filter[created_at][lte]"] = filtercreated_atlte

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/teams",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> TeamList | None:
    if response.status_code == 200:
        response_200 = TeamList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[TeamList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    include: ListTeamsInclude | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtersearch: str | Unset = UNSET,
    filterslug: str | Unset = UNSET,
    filtername: str | Unset = UNSET,
    filterbackstage_id: str | Unset = UNSET,
    filtercortex_id: str | Unset = UNSET,
    filteropslevel_id: str | Unset = UNSET,
    filterexternal_id: str | Unset = UNSET,
    filtercolor: str | Unset = UNSET,
    filteralert_broadcast_enabled: bool | Unset = UNSET,
    filterincident_broadcast_enabled: bool | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Response[TeamList]:
    """List teams

     List teams

    Args:
        include (ListTeamsInclude | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtersearch (str | Unset):
        filterslug (str | Unset):
        filtername (str | Unset):
        filterbackstage_id (str | Unset):
        filtercortex_id (str | Unset):
        filteropslevel_id (str | Unset):
        filterexternal_id (str | Unset):
        filtercolor (str | Unset):
        filteralert_broadcast_enabled (bool | Unset):
        filterincident_broadcast_enabled (bool | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TeamList]
    """

    kwargs = _get_kwargs(
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtersearch=filtersearch,
        filterslug=filterslug,
        filtername=filtername,
        filterbackstage_id=filterbackstage_id,
        filtercortex_id=filtercortex_id,
        filteropslevel_id=filteropslevel_id,
        filterexternal_id=filterexternal_id,
        filtercolor=filtercolor,
        filteralert_broadcast_enabled=filteralert_broadcast_enabled,
        filterincident_broadcast_enabled=filterincident_broadcast_enabled,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    include: ListTeamsInclude | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtersearch: str | Unset = UNSET,
    filterslug: str | Unset = UNSET,
    filtername: str | Unset = UNSET,
    filterbackstage_id: str | Unset = UNSET,
    filtercortex_id: str | Unset = UNSET,
    filteropslevel_id: str | Unset = UNSET,
    filterexternal_id: str | Unset = UNSET,
    filtercolor: str | Unset = UNSET,
    filteralert_broadcast_enabled: bool | Unset = UNSET,
    filterincident_broadcast_enabled: bool | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> TeamList | None:
    """List teams

     List teams

    Args:
        include (ListTeamsInclude | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtersearch (str | Unset):
        filterslug (str | Unset):
        filtername (str | Unset):
        filterbackstage_id (str | Unset):
        filtercortex_id (str | Unset):
        filteropslevel_id (str | Unset):
        filterexternal_id (str | Unset):
        filtercolor (str | Unset):
        filteralert_broadcast_enabled (bool | Unset):
        filterincident_broadcast_enabled (bool | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TeamList
    """

    return sync_detailed(
        client=client,
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtersearch=filtersearch,
        filterslug=filterslug,
        filtername=filtername,
        filterbackstage_id=filterbackstage_id,
        filtercortex_id=filtercortex_id,
        filteropslevel_id=filteropslevel_id,
        filterexternal_id=filterexternal_id,
        filtercolor=filtercolor,
        filteralert_broadcast_enabled=filteralert_broadcast_enabled,
        filterincident_broadcast_enabled=filterincident_broadcast_enabled,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    include: ListTeamsInclude | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtersearch: str | Unset = UNSET,
    filterslug: str | Unset = UNSET,
    filtername: str | Unset = UNSET,
    filterbackstage_id: str | Unset = UNSET,
    filtercortex_id: str | Unset = UNSET,
    filteropslevel_id: str | Unset = UNSET,
    filterexternal_id: str | Unset = UNSET,
    filtercolor: str | Unset = UNSET,
    filteralert_broadcast_enabled: bool | Unset = UNSET,
    filterincident_broadcast_enabled: bool | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Response[TeamList]:
    """List teams

     List teams

    Args:
        include (ListTeamsInclude | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtersearch (str | Unset):
        filterslug (str | Unset):
        filtername (str | Unset):
        filterbackstage_id (str | Unset):
        filtercortex_id (str | Unset):
        filteropslevel_id (str | Unset):
        filterexternal_id (str | Unset):
        filtercolor (str | Unset):
        filteralert_broadcast_enabled (bool | Unset):
        filterincident_broadcast_enabled (bool | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TeamList]
    """

    kwargs = _get_kwargs(
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtersearch=filtersearch,
        filterslug=filterslug,
        filtername=filtername,
        filterbackstage_id=filterbackstage_id,
        filtercortex_id=filtercortex_id,
        filteropslevel_id=filteropslevel_id,
        filterexternal_id=filterexternal_id,
        filtercolor=filtercolor,
        filteralert_broadcast_enabled=filteralert_broadcast_enabled,
        filterincident_broadcast_enabled=filterincident_broadcast_enabled,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    include: ListTeamsInclude | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtersearch: str | Unset = UNSET,
    filterslug: str | Unset = UNSET,
    filtername: str | Unset = UNSET,
    filterbackstage_id: str | Unset = UNSET,
    filtercortex_id: str | Unset = UNSET,
    filteropslevel_id: str | Unset = UNSET,
    filterexternal_id: str | Unset = UNSET,
    filtercolor: str | Unset = UNSET,
    filteralert_broadcast_enabled: bool | Unset = UNSET,
    filterincident_broadcast_enabled: bool | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> TeamList | None:
    """List teams

     List teams

    Args:
        include (ListTeamsInclude | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtersearch (str | Unset):
        filterslug (str | Unset):
        filtername (str | Unset):
        filterbackstage_id (str | Unset):
        filtercortex_id (str | Unset):
        filteropslevel_id (str | Unset):
        filterexternal_id (str | Unset):
        filtercolor (str | Unset):
        filteralert_broadcast_enabled (bool | Unset):
        filterincident_broadcast_enabled (bool | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TeamList
    """

    return (
        await asyncio_detailed(
            client=client,
            include=include,
            pagenumber=pagenumber,
            pagesize=pagesize,
            filtersearch=filtersearch,
            filterslug=filterslug,
            filtername=filtername,
            filterbackstage_id=filterbackstage_id,
            filtercortex_id=filtercortex_id,
            filteropslevel_id=filteropslevel_id,
            filterexternal_id=filterexternal_id,
            filtercolor=filtercolor,
            filteralert_broadcast_enabled=filteralert_broadcast_enabled,
            filterincident_broadcast_enabled=filterincident_broadcast_enabled,
            filtercreated_atgt=filtercreated_atgt,
            filtercreated_atgte=filtercreated_atgte,
            filtercreated_atlt=filtercreated_atlt,
            filtercreated_atlte=filtercreated_atlte,
            sort=sort,
        )
    ).parsed
