from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.alert_route_list import AlertRouteList
from ...models.errors_list import ErrorsList
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtersearch: str | Unset = UNSET,
    filtername: str | Unset = UNSET,
    filterslugeq: str | Unset = UNSET,
    filterslugnot_eq: str | Unset = UNSET,
    filterslugin: str | Unset = UNSET,
    filterslugnot_in: str | Unset = UNSET,
    filternameeq: str | Unset = UNSET,
    filternamenot_eq: str | Unset = UNSET,
    filternamein: str | Unset = UNSET,
    filternamenot_in: str | Unset = UNSET,
    sort: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize

    params["filter[search]"] = filtersearch

    params["filter[name]"] = filtername

    params["filter[slug][eq]"] = filterslugeq

    params["filter[slug][not_eq]"] = filterslugnot_eq

    params["filter[slug][in]"] = filterslugin

    params["filter[slug][not_in]"] = filterslugnot_in

    params["filter[name][eq]"] = filternameeq

    params["filter[name][not_eq]"] = filternamenot_eq

    params["filter[name][in]"] = filternamein

    params["filter[name][not_in]"] = filternamenot_in

    params["sort"] = sort


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/alert_routes",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AlertRouteList | ErrorsList | None:
    if response.status_code == 200:
        response_200 = AlertRouteList.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = ErrorsList.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AlertRouteList | ErrorsList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtersearch: str | Unset = UNSET,
    filtername: str | Unset = UNSET,
    filterslugeq: str | Unset = UNSET,
    filterslugnot_eq: str | Unset = UNSET,
    filterslugin: str | Unset = UNSET,
    filterslugnot_in: str | Unset = UNSET,
    filternameeq: str | Unset = UNSET,
    filternamenot_eq: str | Unset = UNSET,
    filternamein: str | Unset = UNSET,
    filternamenot_in: str | Unset = UNSET,
    sort: str | Unset = UNSET,

) -> Response[AlertRouteList | ErrorsList]:
    """ List alert routes

     List all alert routes for the current team with filtering and pagination. **Note: This endpoint
    requires access to Advanced Alert Routing. If you're unsure whether you have access to this feature,
    please contact Rootly customer support.**

    Args:
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtersearch (str | Unset):
        filtername (str | Unset):
        filterslugeq (str | Unset):
        filterslugnot_eq (str | Unset):
        filterslugin (str | Unset):
        filterslugnot_in (str | Unset):
        filternameeq (str | Unset):
        filternamenot_eq (str | Unset):
        filternamein (str | Unset):
        filternamenot_in (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertRouteList | ErrorsList]
     """


    kwargs = _get_kwargs(
        pagenumber=pagenumber,
pagesize=pagesize,
filtersearch=filtersearch,
filtername=filtername,
filterslugeq=filterslugeq,
filterslugnot_eq=filterslugnot_eq,
filterslugin=filterslugin,
filterslugnot_in=filterslugnot_in,
filternameeq=filternameeq,
filternamenot_eq=filternamenot_eq,
filternamein=filternamein,
filternamenot_in=filternamenot_in,
sort=sort,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtersearch: str | Unset = UNSET,
    filtername: str | Unset = UNSET,
    filterslugeq: str | Unset = UNSET,
    filterslugnot_eq: str | Unset = UNSET,
    filterslugin: str | Unset = UNSET,
    filterslugnot_in: str | Unset = UNSET,
    filternameeq: str | Unset = UNSET,
    filternamenot_eq: str | Unset = UNSET,
    filternamein: str | Unset = UNSET,
    filternamenot_in: str | Unset = UNSET,
    sort: str | Unset = UNSET,

) -> AlertRouteList | ErrorsList | None:
    """ List alert routes

     List all alert routes for the current team with filtering and pagination. **Note: This endpoint
    requires access to Advanced Alert Routing. If you're unsure whether you have access to this feature,
    please contact Rootly customer support.**

    Args:
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtersearch (str | Unset):
        filtername (str | Unset):
        filterslugeq (str | Unset):
        filterslugnot_eq (str | Unset):
        filterslugin (str | Unset):
        filterslugnot_in (str | Unset):
        filternameeq (str | Unset):
        filternamenot_eq (str | Unset):
        filternamein (str | Unset):
        filternamenot_in (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertRouteList | ErrorsList
     """


    return sync_detailed(
        client=client,
pagenumber=pagenumber,
pagesize=pagesize,
filtersearch=filtersearch,
filtername=filtername,
filterslugeq=filterslugeq,
filterslugnot_eq=filterslugnot_eq,
filterslugin=filterslugin,
filterslugnot_in=filterslugnot_in,
filternameeq=filternameeq,
filternamenot_eq=filternamenot_eq,
filternamein=filternamein,
filternamenot_in=filternamenot_in,
sort=sort,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtersearch: str | Unset = UNSET,
    filtername: str | Unset = UNSET,
    filterslugeq: str | Unset = UNSET,
    filterslugnot_eq: str | Unset = UNSET,
    filterslugin: str | Unset = UNSET,
    filterslugnot_in: str | Unset = UNSET,
    filternameeq: str | Unset = UNSET,
    filternamenot_eq: str | Unset = UNSET,
    filternamein: str | Unset = UNSET,
    filternamenot_in: str | Unset = UNSET,
    sort: str | Unset = UNSET,

) -> Response[AlertRouteList | ErrorsList]:
    """ List alert routes

     List all alert routes for the current team with filtering and pagination. **Note: This endpoint
    requires access to Advanced Alert Routing. If you're unsure whether you have access to this feature,
    please contact Rootly customer support.**

    Args:
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtersearch (str | Unset):
        filtername (str | Unset):
        filterslugeq (str | Unset):
        filterslugnot_eq (str | Unset):
        filterslugin (str | Unset):
        filterslugnot_in (str | Unset):
        filternameeq (str | Unset):
        filternamenot_eq (str | Unset):
        filternamein (str | Unset):
        filternamenot_in (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertRouteList | ErrorsList]
     """


    kwargs = _get_kwargs(
        pagenumber=pagenumber,
pagesize=pagesize,
filtersearch=filtersearch,
filtername=filtername,
filterslugeq=filterslugeq,
filterslugnot_eq=filterslugnot_eq,
filterslugin=filterslugin,
filterslugnot_in=filterslugnot_in,
filternameeq=filternameeq,
filternamenot_eq=filternamenot_eq,
filternamein=filternamein,
filternamenot_in=filternamenot_in,
sort=sort,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtersearch: str | Unset = UNSET,
    filtername: str | Unset = UNSET,
    filterslugeq: str | Unset = UNSET,
    filterslugnot_eq: str | Unset = UNSET,
    filterslugin: str | Unset = UNSET,
    filterslugnot_in: str | Unset = UNSET,
    filternameeq: str | Unset = UNSET,
    filternamenot_eq: str | Unset = UNSET,
    filternamein: str | Unset = UNSET,
    filternamenot_in: str | Unset = UNSET,
    sort: str | Unset = UNSET,

) -> AlertRouteList | ErrorsList | None:
    """ List alert routes

     List all alert routes for the current team with filtering and pagination. **Note: This endpoint
    requires access to Advanced Alert Routing. If you're unsure whether you have access to this feature,
    please contact Rootly customer support.**

    Args:
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtersearch (str | Unset):
        filtername (str | Unset):
        filterslugeq (str | Unset):
        filterslugnot_eq (str | Unset):
        filterslugin (str | Unset):
        filterslugnot_in (str | Unset):
        filternameeq (str | Unset):
        filternamenot_eq (str | Unset):
        filternamein (str | Unset):
        filternamenot_in (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertRouteList | ErrorsList
     """


    return (await asyncio_detailed(
        client=client,
pagenumber=pagenumber,
pagesize=pagesize,
filtersearch=filtersearch,
filtername=filtername,
filterslugeq=filterslugeq,
filterslugnot_eq=filterslugnot_eq,
filterslugin=filterslugin,
filterslugnot_in=filterslugnot_in,
filternameeq=filternameeq,
filternamenot_eq=filternamenot_eq,
filternamein=filternamein,
filternamenot_in=filternamenot_in,
sort=sort,

    )).parsed
