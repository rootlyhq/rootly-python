from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alert_group_list import AlertGroupList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include: Union[Unset, str] = UNSET,
    filterslugeq: Union[Unset, str] = UNSET,
    filterslugnot_eq: Union[Unset, str] = UNSET,
    filterslugin: Union[Unset, str] = UNSET,
    filterslugnot_in: Union[Unset, str] = UNSET,
    filternameeq: Union[Unset, str] = UNSET,
    filternamenot_eq: Union[Unset, str] = UNSET,
    filternamein: Union[Unset, str] = UNSET,
    filternamenot_in: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["include"] = include

    params["filter[slug][eq]"] = filterslugeq

    params["filter[slug][not_eq]"] = filterslugnot_eq

    params["filter[slug][in]"] = filterslugin

    params["filter[slug][not_in]"] = filterslugnot_in

    params["filter[name][eq]"] = filternameeq

    params["filter[name][not_eq]"] = filternamenot_eq

    params["filter[name][in]"] = filternamein

    params["filter[name][not_in]"] = filternamenot_in

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/alert_groups",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AlertGroupList]:
    if response.status_code == 200:
        response_200 = AlertGroupList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AlertGroupList]:
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
    filterslugeq: Union[Unset, str] = UNSET,
    filterslugnot_eq: Union[Unset, str] = UNSET,
    filterslugin: Union[Unset, str] = UNSET,
    filterslugnot_in: Union[Unset, str] = UNSET,
    filternameeq: Union[Unset, str] = UNSET,
    filternamenot_eq: Union[Unset, str] = UNSET,
    filternamein: Union[Unset, str] = UNSET,
    filternamenot_in: Union[Unset, str] = UNSET,
) -> Response[AlertGroupList]:
    """List alert groups

     List alert groups

    Args:
        include (Union[Unset, str]):
        filterslugeq (Union[Unset, str]):
        filterslugnot_eq (Union[Unset, str]):
        filterslugin (Union[Unset, str]):
        filterslugnot_in (Union[Unset, str]):
        filternameeq (Union[Unset, str]):
        filternamenot_eq (Union[Unset, str]):
        filternamein (Union[Unset, str]):
        filternamenot_in (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertGroupList]
    """

    kwargs = _get_kwargs(
        include=include,
        filterslugeq=filterslugeq,
        filterslugnot_eq=filterslugnot_eq,
        filterslugin=filterslugin,
        filterslugnot_in=filterslugnot_in,
        filternameeq=filternameeq,
        filternamenot_eq=filternamenot_eq,
        filternamein=filternamein,
        filternamenot_in=filternamenot_in,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    include: Union[Unset, str] = UNSET,
    filterslugeq: Union[Unset, str] = UNSET,
    filterslugnot_eq: Union[Unset, str] = UNSET,
    filterslugin: Union[Unset, str] = UNSET,
    filterslugnot_in: Union[Unset, str] = UNSET,
    filternameeq: Union[Unset, str] = UNSET,
    filternamenot_eq: Union[Unset, str] = UNSET,
    filternamein: Union[Unset, str] = UNSET,
    filternamenot_in: Union[Unset, str] = UNSET,
) -> Optional[AlertGroupList]:
    """List alert groups

     List alert groups

    Args:
        include (Union[Unset, str]):
        filterslugeq (Union[Unset, str]):
        filterslugnot_eq (Union[Unset, str]):
        filterslugin (Union[Unset, str]):
        filterslugnot_in (Union[Unset, str]):
        filternameeq (Union[Unset, str]):
        filternamenot_eq (Union[Unset, str]):
        filternamein (Union[Unset, str]):
        filternamenot_in (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertGroupList
    """

    return sync_detailed(
        client=client,
        include=include,
        filterslugeq=filterslugeq,
        filterslugnot_eq=filterslugnot_eq,
        filterslugin=filterslugin,
        filterslugnot_in=filterslugnot_in,
        filternameeq=filternameeq,
        filternamenot_eq=filternamenot_eq,
        filternamein=filternamein,
        filternamenot_in=filternamenot_in,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    include: Union[Unset, str] = UNSET,
    filterslugeq: Union[Unset, str] = UNSET,
    filterslugnot_eq: Union[Unset, str] = UNSET,
    filterslugin: Union[Unset, str] = UNSET,
    filterslugnot_in: Union[Unset, str] = UNSET,
    filternameeq: Union[Unset, str] = UNSET,
    filternamenot_eq: Union[Unset, str] = UNSET,
    filternamein: Union[Unset, str] = UNSET,
    filternamenot_in: Union[Unset, str] = UNSET,
) -> Response[AlertGroupList]:
    """List alert groups

     List alert groups

    Args:
        include (Union[Unset, str]):
        filterslugeq (Union[Unset, str]):
        filterslugnot_eq (Union[Unset, str]):
        filterslugin (Union[Unset, str]):
        filterslugnot_in (Union[Unset, str]):
        filternameeq (Union[Unset, str]):
        filternamenot_eq (Union[Unset, str]):
        filternamein (Union[Unset, str]):
        filternamenot_in (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertGroupList]
    """

    kwargs = _get_kwargs(
        include=include,
        filterslugeq=filterslugeq,
        filterslugnot_eq=filterslugnot_eq,
        filterslugin=filterslugin,
        filterslugnot_in=filterslugnot_in,
        filternameeq=filternameeq,
        filternamenot_eq=filternamenot_eq,
        filternamein=filternamein,
        filternamenot_in=filternamenot_in,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    include: Union[Unset, str] = UNSET,
    filterslugeq: Union[Unset, str] = UNSET,
    filterslugnot_eq: Union[Unset, str] = UNSET,
    filterslugin: Union[Unset, str] = UNSET,
    filterslugnot_in: Union[Unset, str] = UNSET,
    filternameeq: Union[Unset, str] = UNSET,
    filternamenot_eq: Union[Unset, str] = UNSET,
    filternamein: Union[Unset, str] = UNSET,
    filternamenot_in: Union[Unset, str] = UNSET,
) -> Optional[AlertGroupList]:
    """List alert groups

     List alert groups

    Args:
        include (Union[Unset, str]):
        filterslugeq (Union[Unset, str]):
        filterslugnot_eq (Union[Unset, str]):
        filterslugin (Union[Unset, str]):
        filterslugnot_in (Union[Unset, str]):
        filternameeq (Union[Unset, str]):
        filternamenot_eq (Union[Unset, str]):
        filternamein (Union[Unset, str]):
        filternamenot_in (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertGroupList
    """

    return (
        await asyncio_detailed(
            client=client,
            include=include,
            filterslugeq=filterslugeq,
            filterslugnot_eq=filterslugnot_eq,
            filterslugin=filterslugin,
            filterslugnot_in=filterslugnot_in,
            filternameeq=filternameeq,
            filternamenot_eq=filternamenot_eq,
            filternamein=filternamein,
            filternamenot_in=filternamenot_in,
        )
    ).parsed
