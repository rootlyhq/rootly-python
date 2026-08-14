from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.schedule_list import ScheduleList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include: Union[Unset, str] = UNSET,
    filtersearch: Union[Unset, str] = UNSET,
    filtername: Union[Unset, str] = UNSET,
    filterteam_ids: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
    filternameeq: Union[Unset, str] = UNSET,
    filternamenot_eq: Union[Unset, str] = UNSET,
    filternamein: Union[Unset, str] = UNSET,
    filternamenot_in: Union[Unset, str] = UNSET,
    filterteam_idseq: Union[Unset, str] = UNSET,
    filterteam_idsnot_eq: Union[Unset, str] = UNSET,
    filterteam_idsin: Union[Unset, str] = UNSET,
    filterteam_idsnot_in: Union[Unset, str] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["include"] = include

    params["filter[search]"] = filtersearch

    params["filter[name]"] = filtername

    params["filter[team_ids]"] = filterteam_ids

    params["filter[created_at][gt]"] = filtercreated_atgt

    params["filter[created_at][gte]"] = filtercreated_atgte

    params["filter[created_at][lt]"] = filtercreated_atlt

    params["filter[created_at][lte]"] = filtercreated_atlte

    params["filter[name][eq]"] = filternameeq

    params["filter[name][not_eq]"] = filternamenot_eq

    params["filter[name][in]"] = filternamein

    params["filter[name][not_in]"] = filternamenot_in

    params["filter[team_ids][eq]"] = filterteam_idseq

    params["filter[team_ids][not_eq]"] = filterteam_idsnot_eq

    params["filter[team_ids][in]"] = filterteam_idsin

    params["filter[team_ids][not_in]"] = filterteam_idsnot_in

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/schedules",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[ScheduleList]:
    if response.status_code == 200:
        response_200 = ScheduleList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[ScheduleList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    include: Union[Unset, str] = UNSET,
    filtersearch: Union[Unset, str] = UNSET,
    filtername: Union[Unset, str] = UNSET,
    filterteam_ids: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
    filternameeq: Union[Unset, str] = UNSET,
    filternamenot_eq: Union[Unset, str] = UNSET,
    filternamein: Union[Unset, str] = UNSET,
    filternamenot_in: Union[Unset, str] = UNSET,
    filterteam_idseq: Union[Unset, str] = UNSET,
    filterteam_idsnot_eq: Union[Unset, str] = UNSET,
    filterteam_idsin: Union[Unset, str] = UNSET,
    filterteam_idsnot_in: Union[Unset, str] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
) -> Response[ScheduleList]:
    """List schedules

     List schedules

    Args:
        include (Union[Unset, str]):
        filtersearch (Union[Unset, str]):
        filtername (Union[Unset, str]):
        filterteam_ids (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        filternameeq (Union[Unset, str]):
        filternamenot_eq (Union[Unset, str]):
        filternamein (Union[Unset, str]):
        filternamenot_in (Union[Unset, str]):
        filterteam_idseq (Union[Unset, str]):
        filterteam_idsnot_eq (Union[Unset, str]):
        filterteam_idsin (Union[Unset, str]):
        filterteam_idsnot_in (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ScheduleList]
    """

    kwargs = _get_kwargs(
        include=include,
        filtersearch=filtersearch,
        filtername=filtername,
        filterteam_ids=filterteam_ids,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        filternameeq=filternameeq,
        filternamenot_eq=filternamenot_eq,
        filternamein=filternamein,
        filternamenot_in=filternamenot_in,
        filterteam_idseq=filterteam_idseq,
        filterteam_idsnot_eq=filterteam_idsnot_eq,
        filterteam_idsin=filterteam_idsin,
        filterteam_idsnot_in=filterteam_idsnot_in,
        pagenumber=pagenumber,
        pagesize=pagesize,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    include: Union[Unset, str] = UNSET,
    filtersearch: Union[Unset, str] = UNSET,
    filtername: Union[Unset, str] = UNSET,
    filterteam_ids: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
    filternameeq: Union[Unset, str] = UNSET,
    filternamenot_eq: Union[Unset, str] = UNSET,
    filternamein: Union[Unset, str] = UNSET,
    filternamenot_in: Union[Unset, str] = UNSET,
    filterteam_idseq: Union[Unset, str] = UNSET,
    filterteam_idsnot_eq: Union[Unset, str] = UNSET,
    filterteam_idsin: Union[Unset, str] = UNSET,
    filterteam_idsnot_in: Union[Unset, str] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
) -> Optional[ScheduleList]:
    """List schedules

     List schedules

    Args:
        include (Union[Unset, str]):
        filtersearch (Union[Unset, str]):
        filtername (Union[Unset, str]):
        filterteam_ids (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        filternameeq (Union[Unset, str]):
        filternamenot_eq (Union[Unset, str]):
        filternamein (Union[Unset, str]):
        filternamenot_in (Union[Unset, str]):
        filterteam_idseq (Union[Unset, str]):
        filterteam_idsnot_eq (Union[Unset, str]):
        filterteam_idsin (Union[Unset, str]):
        filterteam_idsnot_in (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ScheduleList
    """

    return sync_detailed(
        client=client,
        include=include,
        filtersearch=filtersearch,
        filtername=filtername,
        filterteam_ids=filterteam_ids,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        filternameeq=filternameeq,
        filternamenot_eq=filternamenot_eq,
        filternamein=filternamein,
        filternamenot_in=filternamenot_in,
        filterteam_idseq=filterteam_idseq,
        filterteam_idsnot_eq=filterteam_idsnot_eq,
        filterteam_idsin=filterteam_idsin,
        filterteam_idsnot_in=filterteam_idsnot_in,
        pagenumber=pagenumber,
        pagesize=pagesize,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    include: Union[Unset, str] = UNSET,
    filtersearch: Union[Unset, str] = UNSET,
    filtername: Union[Unset, str] = UNSET,
    filterteam_ids: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
    filternameeq: Union[Unset, str] = UNSET,
    filternamenot_eq: Union[Unset, str] = UNSET,
    filternamein: Union[Unset, str] = UNSET,
    filternamenot_in: Union[Unset, str] = UNSET,
    filterteam_idseq: Union[Unset, str] = UNSET,
    filterteam_idsnot_eq: Union[Unset, str] = UNSET,
    filterteam_idsin: Union[Unset, str] = UNSET,
    filterteam_idsnot_in: Union[Unset, str] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
) -> Response[ScheduleList]:
    """List schedules

     List schedules

    Args:
        include (Union[Unset, str]):
        filtersearch (Union[Unset, str]):
        filtername (Union[Unset, str]):
        filterteam_ids (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        filternameeq (Union[Unset, str]):
        filternamenot_eq (Union[Unset, str]):
        filternamein (Union[Unset, str]):
        filternamenot_in (Union[Unset, str]):
        filterteam_idseq (Union[Unset, str]):
        filterteam_idsnot_eq (Union[Unset, str]):
        filterteam_idsin (Union[Unset, str]):
        filterteam_idsnot_in (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ScheduleList]
    """

    kwargs = _get_kwargs(
        include=include,
        filtersearch=filtersearch,
        filtername=filtername,
        filterteam_ids=filterteam_ids,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        filternameeq=filternameeq,
        filternamenot_eq=filternamenot_eq,
        filternamein=filternamein,
        filternamenot_in=filternamenot_in,
        filterteam_idseq=filterteam_idseq,
        filterteam_idsnot_eq=filterteam_idsnot_eq,
        filterteam_idsin=filterteam_idsin,
        filterteam_idsnot_in=filterteam_idsnot_in,
        pagenumber=pagenumber,
        pagesize=pagesize,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    include: Union[Unset, str] = UNSET,
    filtersearch: Union[Unset, str] = UNSET,
    filtername: Union[Unset, str] = UNSET,
    filterteam_ids: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
    filternameeq: Union[Unset, str] = UNSET,
    filternamenot_eq: Union[Unset, str] = UNSET,
    filternamein: Union[Unset, str] = UNSET,
    filternamenot_in: Union[Unset, str] = UNSET,
    filterteam_idseq: Union[Unset, str] = UNSET,
    filterteam_idsnot_eq: Union[Unset, str] = UNSET,
    filterteam_idsin: Union[Unset, str] = UNSET,
    filterteam_idsnot_in: Union[Unset, str] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
) -> Optional[ScheduleList]:
    """List schedules

     List schedules

    Args:
        include (Union[Unset, str]):
        filtersearch (Union[Unset, str]):
        filtername (Union[Unset, str]):
        filterteam_ids (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        filternameeq (Union[Unset, str]):
        filternamenot_eq (Union[Unset, str]):
        filternamein (Union[Unset, str]):
        filternamenot_in (Union[Unset, str]):
        filterteam_idseq (Union[Unset, str]):
        filterteam_idsnot_eq (Union[Unset, str]):
        filterteam_idsin (Union[Unset, str]):
        filterteam_idsnot_in (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ScheduleList
    """

    return (
        await asyncio_detailed(
            client=client,
            include=include,
            filtersearch=filtersearch,
            filtername=filtername,
            filterteam_ids=filterteam_ids,
            filtercreated_atgt=filtercreated_atgt,
            filtercreated_atgte=filtercreated_atgte,
            filtercreated_atlt=filtercreated_atlt,
            filtercreated_atlte=filtercreated_atlte,
            filternameeq=filternameeq,
            filternamenot_eq=filternamenot_eq,
            filternamein=filternamein,
            filternamenot_in=filternamenot_in,
            filterteam_idseq=filterteam_idseq,
            filterteam_idsnot_eq=filterteam_idsnot_eq,
            filterteam_idsin=filterteam_idsin,
            filterteam_idsnot_in=filterteam_idsnot_in,
            pagenumber=pagenumber,
            pagesize=pagesize,
        )
    ).parsed
