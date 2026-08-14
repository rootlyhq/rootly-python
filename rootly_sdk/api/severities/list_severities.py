from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.severity_list import SeverityList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include: Unset | str = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filtersearch: Unset | str = UNSET,
    filterslug: Unset | str = UNSET,
    filtername: Unset | str = UNSET,
    filterseverity: Unset | str = UNSET,
    filtercolor: Unset | str = UNSET,
    filtercreated_atgt: Unset | str = UNSET,
    filtercreated_atgte: Unset | str = UNSET,
    filtercreated_atlt: Unset | str = UNSET,
    filtercreated_atlte: Unset | str = UNSET,
    filterslugeq: Unset | str = UNSET,
    filterslugnot_eq: Unset | str = UNSET,
    filterslugin: Unset | str = UNSET,
    filterslugnot_in: Unset | str = UNSET,
    filternameeq: Unset | str = UNSET,
    filternamenot_eq: Unset | str = UNSET,
    filternamein: Unset | str = UNSET,
    filternamenot_in: Unset | str = UNSET,
    filterseverityeq: Unset | str = UNSET,
    filterseveritynot_eq: Unset | str = UNSET,
    filterseverityin: Unset | str = UNSET,
    filterseveritynot_in: Unset | str = UNSET,
    filtercoloreq: Unset | str = UNSET,
    filtercolornot_eq: Unset | str = UNSET,
    filtercolorin: Unset | str = UNSET,
    filtercolornot_in: Unset | str = UNSET,
    sort: Unset | str = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["include"] = include

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize

    params["filter[search]"] = filtersearch

    params["filter[slug]"] = filterslug

    params["filter[name]"] = filtername

    params["filter[severity]"] = filterseverity

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

    params["filter[severity][eq]"] = filterseverityeq

    params["filter[severity][not_eq]"] = filterseveritynot_eq

    params["filter[severity][in]"] = filterseverityin

    params["filter[severity][not_in]"] = filterseveritynot_in

    params["filter[color][eq]"] = filtercoloreq

    params["filter[color][not_eq]"] = filtercolornot_eq

    params["filter[color][in]"] = filtercolorin

    params["filter[color][not_in]"] = filtercolornot_in

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/severities",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SeverityList | None:
    if response.status_code == 200:
        response_200 = SeverityList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SeverityList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    include: Unset | str = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filtersearch: Unset | str = UNSET,
    filterslug: Unset | str = UNSET,
    filtername: Unset | str = UNSET,
    filterseverity: Unset | str = UNSET,
    filtercolor: Unset | str = UNSET,
    filtercreated_atgt: Unset | str = UNSET,
    filtercreated_atgte: Unset | str = UNSET,
    filtercreated_atlt: Unset | str = UNSET,
    filtercreated_atlte: Unset | str = UNSET,
    filterslugeq: Unset | str = UNSET,
    filterslugnot_eq: Unset | str = UNSET,
    filterslugin: Unset | str = UNSET,
    filterslugnot_in: Unset | str = UNSET,
    filternameeq: Unset | str = UNSET,
    filternamenot_eq: Unset | str = UNSET,
    filternamein: Unset | str = UNSET,
    filternamenot_in: Unset | str = UNSET,
    filterseverityeq: Unset | str = UNSET,
    filterseveritynot_eq: Unset | str = UNSET,
    filterseverityin: Unset | str = UNSET,
    filterseveritynot_in: Unset | str = UNSET,
    filtercoloreq: Unset | str = UNSET,
    filtercolornot_eq: Unset | str = UNSET,
    filtercolorin: Unset | str = UNSET,
    filtercolornot_in: Unset | str = UNSET,
    sort: Unset | str = UNSET,
) -> Response[SeverityList]:
    """List severities

     List severities

    Args:
        include (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtersearch (Union[Unset, str]):
        filterslug (Union[Unset, str]):
        filtername (Union[Unset, str]):
        filterseverity (Union[Unset, str]):
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
        filterseverityeq (Union[Unset, str]):
        filterseveritynot_eq (Union[Unset, str]):
        filterseverityin (Union[Unset, str]):
        filterseveritynot_in (Union[Unset, str]):
        filtercoloreq (Union[Unset, str]):
        filtercolornot_eq (Union[Unset, str]):
        filtercolorin (Union[Unset, str]):
        filtercolornot_in (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SeverityList]
    """

    kwargs = _get_kwargs(
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtersearch=filtersearch,
        filterslug=filterslug,
        filtername=filtername,
        filterseverity=filterseverity,
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
        filterseverityeq=filterseverityeq,
        filterseveritynot_eq=filterseveritynot_eq,
        filterseverityin=filterseverityin,
        filterseveritynot_in=filterseveritynot_in,
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
    include: Unset | str = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filtersearch: Unset | str = UNSET,
    filterslug: Unset | str = UNSET,
    filtername: Unset | str = UNSET,
    filterseverity: Unset | str = UNSET,
    filtercolor: Unset | str = UNSET,
    filtercreated_atgt: Unset | str = UNSET,
    filtercreated_atgte: Unset | str = UNSET,
    filtercreated_atlt: Unset | str = UNSET,
    filtercreated_atlte: Unset | str = UNSET,
    filterslugeq: Unset | str = UNSET,
    filterslugnot_eq: Unset | str = UNSET,
    filterslugin: Unset | str = UNSET,
    filterslugnot_in: Unset | str = UNSET,
    filternameeq: Unset | str = UNSET,
    filternamenot_eq: Unset | str = UNSET,
    filternamein: Unset | str = UNSET,
    filternamenot_in: Unset | str = UNSET,
    filterseverityeq: Unset | str = UNSET,
    filterseveritynot_eq: Unset | str = UNSET,
    filterseverityin: Unset | str = UNSET,
    filterseveritynot_in: Unset | str = UNSET,
    filtercoloreq: Unset | str = UNSET,
    filtercolornot_eq: Unset | str = UNSET,
    filtercolorin: Unset | str = UNSET,
    filtercolornot_in: Unset | str = UNSET,
    sort: Unset | str = UNSET,
) -> SeverityList | None:
    """List severities

     List severities

    Args:
        include (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtersearch (Union[Unset, str]):
        filterslug (Union[Unset, str]):
        filtername (Union[Unset, str]):
        filterseverity (Union[Unset, str]):
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
        filterseverityeq (Union[Unset, str]):
        filterseveritynot_eq (Union[Unset, str]):
        filterseverityin (Union[Unset, str]):
        filterseveritynot_in (Union[Unset, str]):
        filtercoloreq (Union[Unset, str]):
        filtercolornot_eq (Union[Unset, str]):
        filtercolorin (Union[Unset, str]):
        filtercolornot_in (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SeverityList
    """

    return sync_detailed(
        client=client,
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtersearch=filtersearch,
        filterslug=filterslug,
        filtername=filtername,
        filterseverity=filterseverity,
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
        filterseverityeq=filterseverityeq,
        filterseveritynot_eq=filterseveritynot_eq,
        filterseverityin=filterseverityin,
        filterseveritynot_in=filterseveritynot_in,
        filtercoloreq=filtercoloreq,
        filtercolornot_eq=filtercolornot_eq,
        filtercolorin=filtercolorin,
        filtercolornot_in=filtercolornot_in,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    include: Unset | str = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filtersearch: Unset | str = UNSET,
    filterslug: Unset | str = UNSET,
    filtername: Unset | str = UNSET,
    filterseverity: Unset | str = UNSET,
    filtercolor: Unset | str = UNSET,
    filtercreated_atgt: Unset | str = UNSET,
    filtercreated_atgte: Unset | str = UNSET,
    filtercreated_atlt: Unset | str = UNSET,
    filtercreated_atlte: Unset | str = UNSET,
    filterslugeq: Unset | str = UNSET,
    filterslugnot_eq: Unset | str = UNSET,
    filterslugin: Unset | str = UNSET,
    filterslugnot_in: Unset | str = UNSET,
    filternameeq: Unset | str = UNSET,
    filternamenot_eq: Unset | str = UNSET,
    filternamein: Unset | str = UNSET,
    filternamenot_in: Unset | str = UNSET,
    filterseverityeq: Unset | str = UNSET,
    filterseveritynot_eq: Unset | str = UNSET,
    filterseverityin: Unset | str = UNSET,
    filterseveritynot_in: Unset | str = UNSET,
    filtercoloreq: Unset | str = UNSET,
    filtercolornot_eq: Unset | str = UNSET,
    filtercolorin: Unset | str = UNSET,
    filtercolornot_in: Unset | str = UNSET,
    sort: Unset | str = UNSET,
) -> Response[SeverityList]:
    """List severities

     List severities

    Args:
        include (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtersearch (Union[Unset, str]):
        filterslug (Union[Unset, str]):
        filtername (Union[Unset, str]):
        filterseverity (Union[Unset, str]):
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
        filterseverityeq (Union[Unset, str]):
        filterseveritynot_eq (Union[Unset, str]):
        filterseverityin (Union[Unset, str]):
        filterseveritynot_in (Union[Unset, str]):
        filtercoloreq (Union[Unset, str]):
        filtercolornot_eq (Union[Unset, str]):
        filtercolorin (Union[Unset, str]):
        filtercolornot_in (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SeverityList]
    """

    kwargs = _get_kwargs(
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtersearch=filtersearch,
        filterslug=filterslug,
        filtername=filtername,
        filterseverity=filterseverity,
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
        filterseverityeq=filterseverityeq,
        filterseveritynot_eq=filterseveritynot_eq,
        filterseverityin=filterseverityin,
        filterseveritynot_in=filterseveritynot_in,
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
    include: Unset | str = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filtersearch: Unset | str = UNSET,
    filterslug: Unset | str = UNSET,
    filtername: Unset | str = UNSET,
    filterseverity: Unset | str = UNSET,
    filtercolor: Unset | str = UNSET,
    filtercreated_atgt: Unset | str = UNSET,
    filtercreated_atgte: Unset | str = UNSET,
    filtercreated_atlt: Unset | str = UNSET,
    filtercreated_atlte: Unset | str = UNSET,
    filterslugeq: Unset | str = UNSET,
    filterslugnot_eq: Unset | str = UNSET,
    filterslugin: Unset | str = UNSET,
    filterslugnot_in: Unset | str = UNSET,
    filternameeq: Unset | str = UNSET,
    filternamenot_eq: Unset | str = UNSET,
    filternamein: Unset | str = UNSET,
    filternamenot_in: Unset | str = UNSET,
    filterseverityeq: Unset | str = UNSET,
    filterseveritynot_eq: Unset | str = UNSET,
    filterseverityin: Unset | str = UNSET,
    filterseveritynot_in: Unset | str = UNSET,
    filtercoloreq: Unset | str = UNSET,
    filtercolornot_eq: Unset | str = UNSET,
    filtercolorin: Unset | str = UNSET,
    filtercolornot_in: Unset | str = UNSET,
    sort: Unset | str = UNSET,
) -> SeverityList | None:
    """List severities

     List severities

    Args:
        include (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtersearch (Union[Unset, str]):
        filterslug (Union[Unset, str]):
        filtername (Union[Unset, str]):
        filterseverity (Union[Unset, str]):
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
        filterseverityeq (Union[Unset, str]):
        filterseveritynot_eq (Union[Unset, str]):
        filterseverityin (Union[Unset, str]):
        filterseveritynot_in (Union[Unset, str]):
        filtercoloreq (Union[Unset, str]):
        filtercolornot_eq (Union[Unset, str]):
        filtercolorin (Union[Unset, str]):
        filtercolornot_in (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SeverityList
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
            filterseverity=filterseverity,
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
            filterseverityeq=filterseverityeq,
            filterseveritynot_eq=filterseveritynot_eq,
            filterseverityin=filterseverityin,
            filterseveritynot_in=filterseveritynot_in,
            filtercoloreq=filtercoloreq,
            filtercolornot_eq=filtercolornot_eq,
            filtercolorin=filtercolorin,
            filtercolornot_in=filtercolornot_in,
            sort=sort,
        )
    ).parsed
