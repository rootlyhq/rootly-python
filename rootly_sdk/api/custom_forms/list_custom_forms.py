from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.custom_form_list import CustomFormList
from ...models.errors_list import ErrorsList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filtersearch: Union[Unset, str] = UNSET,
    filtername: Union[Unset, str] = UNSET,
    filterslug: Union[Unset, str] = UNSET,
    filtercommand: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize

    params["filter[search]"] = filtersearch

    params["filter[name]"] = filtername

    params["filter[slug]"] = filterslug

    params["filter[command]"] = filtercommand

    params["filter[created_at][gt]"] = filtercreated_atgt

    params["filter[created_at][gte]"] = filtercreated_atgte

    params["filter[created_at][lt]"] = filtercreated_atlt

    params["filter[created_at][lte]"] = filtercreated_atlte

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/custom_forms",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CustomFormList, ErrorsList]]:
    if response.status_code == 200:
        response_200 = CustomFormList.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorsList.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[CustomFormList, ErrorsList]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filtersearch: Union[Unset, str] = UNSET,
    filtername: Union[Unset, str] = UNSET,
    filterslug: Union[Unset, str] = UNSET,
    filtercommand: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Response[Union[CustomFormList, ErrorsList]]:
    """List custom forms

     List custom forms

    Args:
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtersearch (Union[Unset, str]):
        filtername (Union[Unset, str]):
        filterslug (Union[Unset, str]):
        filtercommand (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CustomFormList, ErrorsList]]
    """

    kwargs = _get_kwargs(
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtersearch=filtersearch,
        filtername=filtername,
        filterslug=filterslug,
        filtercommand=filtercommand,
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
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filtersearch: Union[Unset, str] = UNSET,
    filtername: Union[Unset, str] = UNSET,
    filterslug: Union[Unset, str] = UNSET,
    filtercommand: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Optional[Union[CustomFormList, ErrorsList]]:
    """List custom forms

     List custom forms

    Args:
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtersearch (Union[Unset, str]):
        filtername (Union[Unset, str]):
        filterslug (Union[Unset, str]):
        filtercommand (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CustomFormList, ErrorsList]
    """

    return sync_detailed(
        client=client,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtersearch=filtersearch,
        filtername=filtername,
        filterslug=filterslug,
        filtercommand=filtercommand,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filtersearch: Union[Unset, str] = UNSET,
    filtername: Union[Unset, str] = UNSET,
    filterslug: Union[Unset, str] = UNSET,
    filtercommand: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Response[Union[CustomFormList, ErrorsList]]:
    """List custom forms

     List custom forms

    Args:
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtersearch (Union[Unset, str]):
        filtername (Union[Unset, str]):
        filterslug (Union[Unset, str]):
        filtercommand (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CustomFormList, ErrorsList]]
    """

    kwargs = _get_kwargs(
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtersearch=filtersearch,
        filtername=filtername,
        filterslug=filterslug,
        filtercommand=filtercommand,
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
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filtersearch: Union[Unset, str] = UNSET,
    filtername: Union[Unset, str] = UNSET,
    filterslug: Union[Unset, str] = UNSET,
    filtercommand: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Optional[Union[CustomFormList, ErrorsList]]:
    """List custom forms

     List custom forms

    Args:
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtersearch (Union[Unset, str]):
        filtername (Union[Unset, str]):
        filterslug (Union[Unset, str]):
        filtercommand (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CustomFormList, ErrorsList]
    """

    return (
        await asyncio_detailed(
            client=client,
            pagenumber=pagenumber,
            pagesize=pagesize,
            filtersearch=filtersearch,
            filtername=filtername,
            filterslug=filterslug,
            filtercommand=filtercommand,
            filtercreated_atgt=filtercreated_atgt,
            filtercreated_atgte=filtercreated_atgte,
            filtercreated_atlt=filtercreated_atlt,
            filtercreated_atlte=filtercreated_atlte,
            sort=sort,
        )
    ).parsed
