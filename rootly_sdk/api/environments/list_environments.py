from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.environment_list import EnvironmentList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include: Union[Unset, str] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filtersearch: Union[Unset, str] = UNSET,
    filterslug: Union[Unset, str] = UNSET,
    filtername: Union[Unset, str] = UNSET,
    filtercolor: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
    filterslugeq: Union[Unset, str] = UNSET,
    filterslugnot_eq: Union[Unset, str] = UNSET,
    filterslugin: Union[Unset, str] = UNSET,
    filterslugnot_in: Union[Unset, str] = UNSET,
    filternameeq: Union[Unset, str] = UNSET,
    filternamenot_eq: Union[Unset, str] = UNSET,
    filternamein: Union[Unset, str] = UNSET,
    filternamenot_in: Union[Unset, str] = UNSET,
    filtercoloreq: Union[Unset, str] = UNSET,
    filtercolornot_eq: Union[Unset, str] = UNSET,
    filtercolorin: Union[Unset, str] = UNSET,
    filtercolornot_in: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["include"] = include

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize

    params["filter[search]"] = filtersearch

    params["filter[slug]"] = filterslug

    params["filter[name]"] = filtername

    params["filter[color]"] = filtercolor

    params["filter[created_at][gt]"] = filtercreated_atgt

    params["filter[created_at][gte]"] = filtercreated_atgte

    params["filter[created_at][lt]"] = filtercreated_atlt

    params["filter[created_at][lte]"] = filtercreated_atlte

    params["filter[slug][eq]"] = filterslugeq

    params["filter[slug][not_eq]"] = filterslugnot_eq

    params["filter[slug][in]"] = filterslugin

    params["filter[slug][not_in]"] = filterslugnot_in

    params["filter[name][eq]"] = filternameeq

    params["filter[name][not_eq]"] = filternamenot_eq

    params["filter[name][in]"] = filternamein

    params["filter[name][not_in]"] = filternamenot_in

    params["filter[color][eq]"] = filtercoloreq

    params["filter[color][not_eq]"] = filtercolornot_eq

    params["filter[color][in]"] = filtercolorin

    params["filter[color][not_in]"] = filtercolornot_in

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/environments",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[EnvironmentList]:
    if response.status_code == 200:
        response_200 = EnvironmentList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[EnvironmentList]:
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
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filtersearch: Union[Unset, str] = UNSET,
    filterslug: Union[Unset, str] = UNSET,
    filtername: Union[Unset, str] = UNSET,
    filtercolor: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
    filterslugeq: Union[Unset, str] = UNSET,
    filterslugnot_eq: Union[Unset, str] = UNSET,
    filterslugin: Union[Unset, str] = UNSET,
    filterslugnot_in: Union[Unset, str] = UNSET,
    filternameeq: Union[Unset, str] = UNSET,
    filternamenot_eq: Union[Unset, str] = UNSET,
    filternamein: Union[Unset, str] = UNSET,
    filternamenot_in: Union[Unset, str] = UNSET,
    filtercoloreq: Union[Unset, str] = UNSET,
    filtercolornot_eq: Union[Unset, str] = UNSET,
    filtercolorin: Union[Unset, str] = UNSET,
    filtercolornot_in: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Response[EnvironmentList]:
    """List environments

     List environments

    Args:
        include (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtersearch (Union[Unset, str]):
        filterslug (Union[Unset, str]):
        filtername (Union[Unset, str]):
        filtercolor (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        filterslugeq (Union[Unset, str]):
        filterslugnot_eq (Union[Unset, str]):
        filterslugin (Union[Unset, str]):
        filterslugnot_in (Union[Unset, str]):
        filternameeq (Union[Unset, str]):
        filternamenot_eq (Union[Unset, str]):
        filternamein (Union[Unset, str]):
        filternamenot_in (Union[Unset, str]):
        filtercoloreq (Union[Unset, str]):
        filtercolornot_eq (Union[Unset, str]):
        filtercolorin (Union[Unset, str]):
        filtercolornot_in (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EnvironmentList]
    """

    kwargs = _get_kwargs(
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtersearch=filtersearch,
        filterslug=filterslug,
        filtername=filtername,
        filtercolor=filtercolor,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        filterslugeq=filterslugeq,
        filterslugnot_eq=filterslugnot_eq,
        filterslugin=filterslugin,
        filterslugnot_in=filterslugnot_in,
        filternameeq=filternameeq,
        filternamenot_eq=filternamenot_eq,
        filternamein=filternamein,
        filternamenot_in=filternamenot_in,
        filtercoloreq=filtercoloreq,
        filtercolornot_eq=filtercolornot_eq,
        filtercolorin=filtercolorin,
        filtercolornot_in=filtercolornot_in,
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    include: Union[Unset, str] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filtersearch: Union[Unset, str] = UNSET,
    filterslug: Union[Unset, str] = UNSET,
    filtername: Union[Unset, str] = UNSET,
    filtercolor: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
    filterslugeq: Union[Unset, str] = UNSET,
    filterslugnot_eq: Union[Unset, str] = UNSET,
    filterslugin: Union[Unset, str] = UNSET,
    filterslugnot_in: Union[Unset, str] = UNSET,
    filternameeq: Union[Unset, str] = UNSET,
    filternamenot_eq: Union[Unset, str] = UNSET,
    filternamein: Union[Unset, str] = UNSET,
    filternamenot_in: Union[Unset, str] = UNSET,
    filtercoloreq: Union[Unset, str] = UNSET,
    filtercolornot_eq: Union[Unset, str] = UNSET,
    filtercolorin: Union[Unset, str] = UNSET,
    filtercolornot_in: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Optional[EnvironmentList]:
    """List environments

     List environments

    Args:
        include (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtersearch (Union[Unset, str]):
        filterslug (Union[Unset, str]):
        filtername (Union[Unset, str]):
        filtercolor (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        filterslugeq (Union[Unset, str]):
        filterslugnot_eq (Union[Unset, str]):
        filterslugin (Union[Unset, str]):
        filterslugnot_in (Union[Unset, str]):
        filternameeq (Union[Unset, str]):
        filternamenot_eq (Union[Unset, str]):
        filternamein (Union[Unset, str]):
        filternamenot_in (Union[Unset, str]):
        filtercoloreq (Union[Unset, str]):
        filtercolornot_eq (Union[Unset, str]):
        filtercolorin (Union[Unset, str]):
        filtercolornot_in (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EnvironmentList
    """

    return sync_detailed(
        client=client,
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtersearch=filtersearch,
        filterslug=filterslug,
        filtername=filtername,
        filtercolor=filtercolor,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        filterslugeq=filterslugeq,
        filterslugnot_eq=filterslugnot_eq,
        filterslugin=filterslugin,
        filterslugnot_in=filterslugnot_in,
        filternameeq=filternameeq,
        filternamenot_eq=filternamenot_eq,
        filternamein=filternamein,
        filternamenot_in=filternamenot_in,
        filtercoloreq=filtercoloreq,
        filtercolornot_eq=filtercolornot_eq,
        filtercolorin=filtercolorin,
        filtercolornot_in=filtercolornot_in,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    include: Union[Unset, str] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filtersearch: Union[Unset, str] = UNSET,
    filterslug: Union[Unset, str] = UNSET,
    filtername: Union[Unset, str] = UNSET,
    filtercolor: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
    filterslugeq: Union[Unset, str] = UNSET,
    filterslugnot_eq: Union[Unset, str] = UNSET,
    filterslugin: Union[Unset, str] = UNSET,
    filterslugnot_in: Union[Unset, str] = UNSET,
    filternameeq: Union[Unset, str] = UNSET,
    filternamenot_eq: Union[Unset, str] = UNSET,
    filternamein: Union[Unset, str] = UNSET,
    filternamenot_in: Union[Unset, str] = UNSET,
    filtercoloreq: Union[Unset, str] = UNSET,
    filtercolornot_eq: Union[Unset, str] = UNSET,
    filtercolorin: Union[Unset, str] = UNSET,
    filtercolornot_in: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Response[EnvironmentList]:
    """List environments

     List environments

    Args:
        include (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtersearch (Union[Unset, str]):
        filterslug (Union[Unset, str]):
        filtername (Union[Unset, str]):
        filtercolor (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        filterslugeq (Union[Unset, str]):
        filterslugnot_eq (Union[Unset, str]):
        filterslugin (Union[Unset, str]):
        filterslugnot_in (Union[Unset, str]):
        filternameeq (Union[Unset, str]):
        filternamenot_eq (Union[Unset, str]):
        filternamein (Union[Unset, str]):
        filternamenot_in (Union[Unset, str]):
        filtercoloreq (Union[Unset, str]):
        filtercolornot_eq (Union[Unset, str]):
        filtercolorin (Union[Unset, str]):
        filtercolornot_in (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EnvironmentList]
    """

    kwargs = _get_kwargs(
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtersearch=filtersearch,
        filterslug=filterslug,
        filtername=filtername,
        filtercolor=filtercolor,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        filterslugeq=filterslugeq,
        filterslugnot_eq=filterslugnot_eq,
        filterslugin=filterslugin,
        filterslugnot_in=filterslugnot_in,
        filternameeq=filternameeq,
        filternamenot_eq=filternamenot_eq,
        filternamein=filternamein,
        filternamenot_in=filternamenot_in,
        filtercoloreq=filtercoloreq,
        filtercolornot_eq=filtercolornot_eq,
        filtercolorin=filtercolorin,
        filtercolornot_in=filtercolornot_in,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    include: Union[Unset, str] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filtersearch: Union[Unset, str] = UNSET,
    filterslug: Union[Unset, str] = UNSET,
    filtername: Union[Unset, str] = UNSET,
    filtercolor: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
    filterslugeq: Union[Unset, str] = UNSET,
    filterslugnot_eq: Union[Unset, str] = UNSET,
    filterslugin: Union[Unset, str] = UNSET,
    filterslugnot_in: Union[Unset, str] = UNSET,
    filternameeq: Union[Unset, str] = UNSET,
    filternamenot_eq: Union[Unset, str] = UNSET,
    filternamein: Union[Unset, str] = UNSET,
    filternamenot_in: Union[Unset, str] = UNSET,
    filtercoloreq: Union[Unset, str] = UNSET,
    filtercolornot_eq: Union[Unset, str] = UNSET,
    filtercolorin: Union[Unset, str] = UNSET,
    filtercolornot_in: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Optional[EnvironmentList]:
    """List environments

     List environments

    Args:
        include (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtersearch (Union[Unset, str]):
        filterslug (Union[Unset, str]):
        filtername (Union[Unset, str]):
        filtercolor (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        filterslugeq (Union[Unset, str]):
        filterslugnot_eq (Union[Unset, str]):
        filterslugin (Union[Unset, str]):
        filterslugnot_in (Union[Unset, str]):
        filternameeq (Union[Unset, str]):
        filternamenot_eq (Union[Unset, str]):
        filternamein (Union[Unset, str]):
        filternamenot_in (Union[Unset, str]):
        filtercoloreq (Union[Unset, str]):
        filtercolornot_eq (Union[Unset, str]):
        filtercolorin (Union[Unset, str]):
        filtercolornot_in (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EnvironmentList
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
            filtercolor=filtercolor,
            filtercreated_atgt=filtercreated_atgt,
            filtercreated_atgte=filtercreated_atgte,
            filtercreated_atlt=filtercreated_atlt,
            filtercreated_atlte=filtercreated_atlte,
            filterslugeq=filterslugeq,
            filterslugnot_eq=filterslugnot_eq,
            filterslugin=filterslugin,
            filterslugnot_in=filterslugnot_in,
            filternameeq=filternameeq,
            filternamenot_eq=filternamenot_eq,
            filternamein=filternamein,
            filternamenot_in=filternamenot_in,
            filtercoloreq=filtercoloreq,
            filtercolornot_eq=filtercolornot_eq,
            filtercolorin=filtercolorin,
            filtercolornot_in=filtercolornot_in,
            sort=sort,
        )
    ).parsed
