from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.resend_verification_user_phone_number_response_200 import ResendVerificationUserPhoneNumberResponse200
from ...models.resend_verification_user_phone_number_response_429 import ResendVerificationUserPhoneNumberResponse429
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/phone_numbers/{id}/resend_verification".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ResendVerificationUserPhoneNumberResponse200 | ResendVerificationUserPhoneNumberResponse429 | None:
    if response.status_code == 200:
        response_200 = ResendVerificationUserPhoneNumberResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = ResendVerificationUserPhoneNumberResponse429.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ResendVerificationUserPhoneNumberResponse200 | ResendVerificationUserPhoneNumberResponse429]:
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
) -> Response[ResendVerificationUserPhoneNumberResponse200 | ResendVerificationUserPhoneNumberResponse429]:
    """Resend verification code

     Resends a verification code to the phone number. SMS sends are limited per recipient to 3 per hour
    and 5 per day. An application rate-limit 429 response includes Retry-After with the remaining wait
    in seconds.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResendVerificationUserPhoneNumberResponse200 | ResendVerificationUserPhoneNumberResponse429]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
) -> ResendVerificationUserPhoneNumberResponse200 | ResendVerificationUserPhoneNumberResponse429 | None:
    """Resend verification code

     Resends a verification code to the phone number. SMS sends are limited per recipient to 3 per hour
    and 5 per day. An application rate-limit 429 response includes Retry-After with the remaining wait
    in seconds.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResendVerificationUserPhoneNumberResponse200 | ResendVerificationUserPhoneNumberResponse429
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ResendVerificationUserPhoneNumberResponse200 | ResendVerificationUserPhoneNumberResponse429]:
    """Resend verification code

     Resends a verification code to the phone number. SMS sends are limited per recipient to 3 per hour
    and 5 per day. An application rate-limit 429 response includes Retry-After with the remaining wait
    in seconds.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResendVerificationUserPhoneNumberResponse200 | ResendVerificationUserPhoneNumberResponse429]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
) -> ResendVerificationUserPhoneNumberResponse200 | ResendVerificationUserPhoneNumberResponse429 | None:
    """Resend verification code

     Resends a verification code to the phone number. SMS sends are limited per recipient to 3 per hour
    and 5 per day. An application rate-limit 429 response includes Retry-After with the remaining wait
    in seconds.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResendVerificationUserPhoneNumberResponse200 | ResendVerificationUserPhoneNumberResponse429
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
