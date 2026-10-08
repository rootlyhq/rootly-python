from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.form_field_option_list import FormFieldOptionList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    form_field_id: str,
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
        "url": "/v1/form_fields/{form_field_id}/options".format(
            form_field_id=quote(str(form_field_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> FormFieldOptionList | None:
    if response.status_code == 200:
        response_200 = FormFieldOptionList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[FormFieldOptionList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    form_field_id: str,
    *,
    client: AuthenticatedClient,
    include: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtervalue: str | Unset = UNSET,
    filtercolor: str | Unset = UNSET,
) -> Response[FormFieldOptionList]:
    """List FormField Options

     List form_field_options

    Args:
        form_field_id (str):
        include (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtervalue (str | Unset):
        filtercolor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FormFieldOptionList]
    """

    kwargs = _get_kwargs(
        form_field_id=form_field_id,
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
    form_field_id: str,
    *,
    client: AuthenticatedClient,
    include: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtervalue: str | Unset = UNSET,
    filtercolor: str | Unset = UNSET,
) -> FormFieldOptionList | None:
    """List FormField Options

     List form_field_options

    Args:
        form_field_id (str):
        include (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtervalue (str | Unset):
        filtercolor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FormFieldOptionList
    """

    return sync_detailed(
        form_field_id=form_field_id,
        client=client,
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtervalue=filtervalue,
        filtercolor=filtercolor,
    ).parsed


async def asyncio_detailed(
    form_field_id: str,
    *,
    client: AuthenticatedClient,
    include: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtervalue: str | Unset = UNSET,
    filtercolor: str | Unset = UNSET,
) -> Response[FormFieldOptionList]:
    """List FormField Options

     List form_field_options

    Args:
        form_field_id (str):
        include (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtervalue (str | Unset):
        filtercolor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FormFieldOptionList]
    """

    kwargs = _get_kwargs(
        form_field_id=form_field_id,
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtervalue=filtervalue,
        filtercolor=filtercolor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    form_field_id: str,
    *,
    client: AuthenticatedClient,
    include: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtervalue: str | Unset = UNSET,
    filtercolor: str | Unset = UNSET,
) -> FormFieldOptionList | None:
    """List FormField Options

     List form_field_options

    Args:
        form_field_id (str):
        include (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtervalue (str | Unset):
        filtercolor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FormFieldOptionList
    """

    return (
        await asyncio_detailed(
            form_field_id=form_field_id,
            client=client,
            include=include,
            pagenumber=pagenumber,
            pagesize=pagesize,
            filtervalue=filtervalue,
            filtercolor=filtercolor,
        )
    ).parsed
