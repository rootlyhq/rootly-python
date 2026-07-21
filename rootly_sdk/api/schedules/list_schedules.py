from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.schedule_list import ScheduleList
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    include: str | Unset = UNSET,
    filtersearch: str | Unset = UNSET,
    filtername: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filternameeq: str | Unset = UNSET,
    filternamenot_eq: str | Unset = UNSET,
    filternamein: str | Unset = UNSET,
    filternamenot_in: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["include"] = include

    params["filter[search]"] = filtersearch

    params["filter[name]"] = filtername

    params["filter[created_at][gt]"] = filtercreated_atgt

    params["filter[created_at][gte]"] = filtercreated_atgte

    params["filter[created_at][lt]"] = filtercreated_atlt

    params["filter[created_at][lte]"] = filtercreated_atlte

    params["filter[name][eq]"] = filternameeq

    params["filter[name][not_eq]"] = filternamenot_eq

    params["filter[name][in]"] = filternamein

    params["filter[name][not_in]"] = filternamenot_in

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/schedules",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ScheduleList | None:
    if response.status_code == 200:
        response_200 = ScheduleList.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ScheduleList]:
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
    filtersearch: str | Unset = UNSET,
    filtername: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filternameeq: str | Unset = UNSET,
    filternamenot_eq: str | Unset = UNSET,
    filternamein: str | Unset = UNSET,
    filternamenot_in: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,

) -> Response[ScheduleList]:
    """ List schedules

     List schedules

    Args:
        include (str | Unset):
        filtersearch (str | Unset):
        filtername (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        filternameeq (str | Unset):
        filternamenot_eq (str | Unset):
        filternamein (str | Unset):
        filternamenot_in (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):

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
filtercreated_atgt=filtercreated_atgt,
filtercreated_atgte=filtercreated_atgte,
filtercreated_atlt=filtercreated_atlt,
filtercreated_atlte=filtercreated_atlte,
filternameeq=filternameeq,
filternamenot_eq=filternamenot_eq,
filternamein=filternamein,
filternamenot_in=filternamenot_in,
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
    include: str | Unset = UNSET,
    filtersearch: str | Unset = UNSET,
    filtername: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filternameeq: str | Unset = UNSET,
    filternamenot_eq: str | Unset = UNSET,
    filternamein: str | Unset = UNSET,
    filternamenot_in: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,

) -> ScheduleList | None:
    """ List schedules

     List schedules

    Args:
        include (str | Unset):
        filtersearch (str | Unset):
        filtername (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        filternameeq (str | Unset):
        filternamenot_eq (str | Unset):
        filternamein (str | Unset):
        filternamenot_in (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):

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
filtercreated_atgt=filtercreated_atgt,
filtercreated_atgte=filtercreated_atgte,
filtercreated_atlt=filtercreated_atlt,
filtercreated_atlte=filtercreated_atlte,
filternameeq=filternameeq,
filternamenot_eq=filternamenot_eq,
filternamein=filternamein,
filternamenot_in=filternamenot_in,
pagenumber=pagenumber,
pagesize=pagesize,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    include: str | Unset = UNSET,
    filtersearch: str | Unset = UNSET,
    filtername: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filternameeq: str | Unset = UNSET,
    filternamenot_eq: str | Unset = UNSET,
    filternamein: str | Unset = UNSET,
    filternamenot_in: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,

) -> Response[ScheduleList]:
    """ List schedules

     List schedules

    Args:
        include (str | Unset):
        filtersearch (str | Unset):
        filtername (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        filternameeq (str | Unset):
        filternamenot_eq (str | Unset):
        filternamein (str | Unset):
        filternamenot_in (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):

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
filtercreated_atgt=filtercreated_atgt,
filtercreated_atgte=filtercreated_atgte,
filtercreated_atlt=filtercreated_atlt,
filtercreated_atlte=filtercreated_atlte,
filternameeq=filternameeq,
filternamenot_eq=filternamenot_eq,
filternamein=filternamein,
filternamenot_in=filternamenot_in,
pagenumber=pagenumber,
pagesize=pagesize,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    include: str | Unset = UNSET,
    filtersearch: str | Unset = UNSET,
    filtername: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filternameeq: str | Unset = UNSET,
    filternamenot_eq: str | Unset = UNSET,
    filternamein: str | Unset = UNSET,
    filternamenot_in: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,

) -> ScheduleList | None:
    """ List schedules

     List schedules

    Args:
        include (str | Unset):
        filtersearch (str | Unset):
        filtername (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        filternameeq (str | Unset):
        filternamenot_eq (str | Unset):
        filternamein (str | Unset):
        filternamenot_in (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ScheduleList
     """


    return (await asyncio_detailed(
        client=client,
include=include,
filtersearch=filtersearch,
filtername=filtername,
filtercreated_atgt=filtercreated_atgt,
filtercreated_atgte=filtercreated_atgte,
filtercreated_atlt=filtercreated_atlt,
filtercreated_atlte=filtercreated_atlte,
filternameeq=filternameeq,
filternamenot_eq=filternamenot_eq,
filternamein=filternamein,
filternamenot_in=filternamenot_in,
pagenumber=pagenumber,
pagesize=pagesize,

    )).parsed
