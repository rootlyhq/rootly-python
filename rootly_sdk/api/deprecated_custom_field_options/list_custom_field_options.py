from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.custom_field_option_list import CustomFieldOptionList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    custom_field_id: str,
    *,
    include: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtervalue: str | Unset = UNSET,
    filtercolor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["include"] = include

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize

    params["filter[value]"] = filtervalue

    params["filter[color]"] = filtercolor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/custom_fields/{custom_field_id}/options".format(
            custom_field_id=quote(str(custom_field_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CustomFieldOptionList | None:
    if response.status_code == 200:
        response_200 = CustomFieldOptionList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CustomFieldOptionList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    custom_field_id: str,
    *,
    client: AuthenticatedClient,
    include: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtervalue: str | Unset = UNSET,
    filtercolor: str | Unset = UNSET,
) -> Response[CustomFieldOptionList]:
    """[DEPRECATED] List custom field options

     [DEPRECATED] Use form field endpoints instead. List custom field options

    Args:
        custom_field_id (str):
        include (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtervalue (str | Unset):
        filtercolor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomFieldOptionList]
    """

    kwargs = _get_kwargs(
        custom_field_id=custom_field_id,
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtervalue=filtervalue,
        filtercolor=filtercolor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    custom_field_id: str,
    *,
    client: AuthenticatedClient,
    include: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtervalue: str | Unset = UNSET,
    filtercolor: str | Unset = UNSET,
) -> CustomFieldOptionList | None:
    """[DEPRECATED] List custom field options

     [DEPRECATED] Use form field endpoints instead. List custom field options

    Args:
        custom_field_id (str):
        include (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtervalue (str | Unset):
        filtercolor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomFieldOptionList
    """

    return sync_detailed(
        custom_field_id=custom_field_id,
        client=client,
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtervalue=filtervalue,
        filtercolor=filtercolor,
    ).parsed


async def asyncio_detailed(
    custom_field_id: str,
    *,
    client: AuthenticatedClient,
    include: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtervalue: str | Unset = UNSET,
    filtercolor: str | Unset = UNSET,
) -> Response[CustomFieldOptionList]:
    """[DEPRECATED] List custom field options

     [DEPRECATED] Use form field endpoints instead. List custom field options

    Args:
        custom_field_id (str):
        include (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtervalue (str | Unset):
        filtercolor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomFieldOptionList]
    """

    kwargs = _get_kwargs(
        custom_field_id=custom_field_id,
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtervalue=filtervalue,
        filtercolor=filtercolor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    custom_field_id: str,
    *,
    client: AuthenticatedClient,
    include: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtervalue: str | Unset = UNSET,
    filtercolor: str | Unset = UNSET,
) -> CustomFieldOptionList | None:
    """[DEPRECATED] List custom field options

     [DEPRECATED] Use form field endpoints instead. List custom field options

    Args:
        custom_field_id (str):
        include (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtervalue (str | Unset):
        filtercolor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomFieldOptionList
    """

    return (
        await asyncio_detailed(
            custom_field_id=custom_field_id,
            client=client,
            include=include,
            pagenumber=pagenumber,
            pagesize=pagesize,
            filtervalue=filtervalue,
            filtercolor=filtercolor,
        )
    ).parsed
