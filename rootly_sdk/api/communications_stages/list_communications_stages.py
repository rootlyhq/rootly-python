from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.communications_stages_response import CommunicationsStagesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filtersearch: Unset | str = UNSET,
    filtername: Unset | str = UNSET,
    filterslug: Unset | str = UNSET,
    filtercreated_atgt: Unset | str = UNSET,
    filtercreated_atgte: Unset | str = UNSET,
    filtercreated_atlt: Unset | str = UNSET,
    filtercreated_atlte: Unset | str = UNSET,
    sort: Unset | str = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize

    params["filter[search]"] = filtersearch

    params["filter[name]"] = filtername

    params["filter[slug]"] = filterslug

    params["filter[created_at][gt]"] = filtercreated_atgt

    params["filter[created_at][gte]"] = filtercreated_atgte

    params["filter[created_at][lt]"] = filtercreated_atlt

    params["filter[created_at][lte]"] = filtercreated_atlte

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/communications/stages",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CommunicationsStagesResponse | None:
    if response.status_code == 200:
        response_200 = CommunicationsStagesResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CommunicationsStagesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filtersearch: Unset | str = UNSET,
    filtername: Unset | str = UNSET,
    filterslug: Unset | str = UNSET,
    filtercreated_atgt: Unset | str = UNSET,
    filtercreated_atgte: Unset | str = UNSET,
    filtercreated_atlt: Unset | str = UNSET,
    filtercreated_atlte: Unset | str = UNSET,
    sort: Unset | str = UNSET,
) -> Response[CommunicationsStagesResponse]:
    """Lists communications stages

     Lists communications stages

    Args:
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtersearch (Union[Unset, str]):
        filtername (Union[Unset, str]):
        filterslug (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CommunicationsStagesResponse]
    """

    kwargs = _get_kwargs(
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtersearch=filtersearch,
        filtername=filtername,
        filterslug=filterslug,
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
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filtersearch: Unset | str = UNSET,
    filtername: Unset | str = UNSET,
    filterslug: Unset | str = UNSET,
    filtercreated_atgt: Unset | str = UNSET,
    filtercreated_atgte: Unset | str = UNSET,
    filtercreated_atlt: Unset | str = UNSET,
    filtercreated_atlte: Unset | str = UNSET,
    sort: Unset | str = UNSET,
) -> CommunicationsStagesResponse | None:
    """Lists communications stages

     Lists communications stages

    Args:
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtersearch (Union[Unset, str]):
        filtername (Union[Unset, str]):
        filterslug (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CommunicationsStagesResponse
    """

    return sync_detailed(
        client=client,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtersearch=filtersearch,
        filtername=filtername,
        filterslug=filterslug,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filtersearch: Unset | str = UNSET,
    filtername: Unset | str = UNSET,
    filterslug: Unset | str = UNSET,
    filtercreated_atgt: Unset | str = UNSET,
    filtercreated_atgte: Unset | str = UNSET,
    filtercreated_atlt: Unset | str = UNSET,
    filtercreated_atlte: Unset | str = UNSET,
    sort: Unset | str = UNSET,
) -> Response[CommunicationsStagesResponse]:
    """Lists communications stages

     Lists communications stages

    Args:
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtersearch (Union[Unset, str]):
        filtername (Union[Unset, str]):
        filterslug (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CommunicationsStagesResponse]
    """

    kwargs = _get_kwargs(
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtersearch=filtersearch,
        filtername=filtername,
        filterslug=filterslug,
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
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filtersearch: Unset | str = UNSET,
    filtername: Unset | str = UNSET,
    filterslug: Unset | str = UNSET,
    filtercreated_atgt: Unset | str = UNSET,
    filtercreated_atgte: Unset | str = UNSET,
    filtercreated_atlt: Unset | str = UNSET,
    filtercreated_atlte: Unset | str = UNSET,
    sort: Unset | str = UNSET,
) -> CommunicationsStagesResponse | None:
    """Lists communications stages

     Lists communications stages

    Args:
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtersearch (Union[Unset, str]):
        filtername (Union[Unset, str]):
        filterslug (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CommunicationsStagesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            pagenumber=pagenumber,
            pagesize=pagesize,
            filtersearch=filtersearch,
            filtername=filtername,
            filterslug=filterslug,
            filtercreated_atgt=filtercreated_atgt,
            filtercreated_atgte=filtercreated_atgte,
            filtercreated_atlt=filtercreated_atlt,
            filtercreated_atlte=filtercreated_atlte,
            sort=sort,
        )
    ).parsed
