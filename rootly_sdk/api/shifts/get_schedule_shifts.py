from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors_list import ErrorsList
from ...models.shift_list import ShiftList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    to: Union[Unset, str] = UNSET,
    from_: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["to"] = to

    params["from"] = from_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/schedules/{id}/shifts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorsList, ShiftList]]:
    if response.status_code == 200:
        response_200 = ShiftList.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = ErrorsList.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorsList, ShiftList]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    to: Union[Unset, str] = UNSET,
    from_: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorsList, ShiftList]]:
    """Retrieves a schedule shifts

     Retrieves schedule shifts

    Args:
        id (str):
        to (Union[Unset, str]):
        from_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, ShiftList]]
    """

    kwargs = _get_kwargs(
        id=id,
        to=to,
        from_=from_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    to: Union[Unset, str] = UNSET,
    from_: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorsList, ShiftList]]:
    """Retrieves a schedule shifts

     Retrieves schedule shifts

    Args:
        id (str):
        to (Union[Unset, str]):
        from_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, ShiftList]
    """

    return sync_detailed(
        id=id,
        client=client,
        to=to,
        from_=from_,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    to: Union[Unset, str] = UNSET,
    from_: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorsList, ShiftList]]:
    """Retrieves a schedule shifts

     Retrieves schedule shifts

    Args:
        id (str):
        to (Union[Unset, str]):
        from_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, ShiftList]]
    """

    kwargs = _get_kwargs(
        id=id,
        to=to,
        from_=from_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    to: Union[Unset, str] = UNSET,
    from_: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorsList, ShiftList]]:
    """Retrieves a schedule shifts

     Retrieves schedule shifts

    Args:
        id (str):
        to (Union[Unset, str]):
        from_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, ShiftList]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            to=to,
            from_=from_,
        )
    ).parsed
