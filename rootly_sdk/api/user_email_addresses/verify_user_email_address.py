from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors_list import ErrorsList
from ...models.user_email_address_response import UserEmailAddressResponse
from ...types import UNSET, Response


def _get_kwargs(
    id: str,
    *,
    token: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["token"] = token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/v1/email_addresses/{id}/verify",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorsList | UserEmailAddressResponse | None:
    if response.status_code == 200:
        response_200 = UserEmailAddressResponse.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = ErrorsList.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = ErrorsList.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorsList | UserEmailAddressResponse]:
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
    token: str,
) -> Response[ErrorsList | UserEmailAddressResponse]:
    """Verifies an email address with token

     Verifies an email address using a verification token

    Args:
        id (str):
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, UserEmailAddressResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        token=token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    token: str,
) -> ErrorsList | UserEmailAddressResponse | None:
    """Verifies an email address with token

     Verifies an email address using a verification token

    Args:
        id (str):
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, UserEmailAddressResponse]
    """

    return sync_detailed(
        id=id,
        client=client,
        token=token,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    token: str,
) -> Response[ErrorsList | UserEmailAddressResponse]:
    """Verifies an email address with token

     Verifies an email address using a verification token

    Args:
        id (str):
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, UserEmailAddressResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        token=token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    token: str,
) -> ErrorsList | UserEmailAddressResponse | None:
    """Verifies an email address with token

     Verifies an email address using a verification token

    Args:
        id (str):
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, UserEmailAddressResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            token=token,
        )
    ).parsed
