from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors_list import ErrorsList
from ...models.generate_phone_number_live_call_router_country_code import (
    GeneratePhoneNumberLiveCallRouterCountryCode,
)
from ...models.generate_phone_number_live_call_router_phone_type import (
    GeneratePhoneNumberLiveCallRouterPhoneType,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    country_code: GeneratePhoneNumberLiveCallRouterCountryCode,
    phone_type: GeneratePhoneNumberLiveCallRouterPhoneType,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_country_code: str = country_code
    params["country_code"] = json_country_code

    json_phone_type: str = phone_type
    params["phone_type"] = json_phone_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/live_call_routers/generate_phone_number",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ErrorsList | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 422:
        response_422 = ErrorsList.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ErrorsList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    country_code: GeneratePhoneNumberLiveCallRouterCountryCode,
    phone_type: GeneratePhoneNumberLiveCallRouterPhoneType,
) -> Response[Any | ErrorsList]:
    """Generates a phone number for Live Call Router

     Generates a phone number for Live Call Router

    Args:
        country_code (GeneratePhoneNumberLiveCallRouterCountryCode):
        phone_type (GeneratePhoneNumberLiveCallRouterPhoneType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorsList]]
    """

    kwargs = _get_kwargs(
        country_code=country_code,
        phone_type=phone_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    country_code: GeneratePhoneNumberLiveCallRouterCountryCode,
    phone_type: GeneratePhoneNumberLiveCallRouterPhoneType,
) -> Any | ErrorsList | None:
    """Generates a phone number for Live Call Router

     Generates a phone number for Live Call Router

    Args:
        country_code (GeneratePhoneNumberLiveCallRouterCountryCode):
        phone_type (GeneratePhoneNumberLiveCallRouterPhoneType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorsList]
    """

    return sync_detailed(
        client=client,
        country_code=country_code,
        phone_type=phone_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    country_code: GeneratePhoneNumberLiveCallRouterCountryCode,
    phone_type: GeneratePhoneNumberLiveCallRouterPhoneType,
) -> Response[Any | ErrorsList]:
    """Generates a phone number for Live Call Router

     Generates a phone number for Live Call Router

    Args:
        country_code (GeneratePhoneNumberLiveCallRouterCountryCode):
        phone_type (GeneratePhoneNumberLiveCallRouterPhoneType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorsList]]
    """

    kwargs = _get_kwargs(
        country_code=country_code,
        phone_type=phone_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    country_code: GeneratePhoneNumberLiveCallRouterCountryCode,
    phone_type: GeneratePhoneNumberLiveCallRouterPhoneType,
) -> Any | ErrorsList | None:
    """Generates a phone number for Live Call Router

     Generates a phone number for Live Call Router

    Args:
        country_code (GeneratePhoneNumberLiveCallRouterCountryCode):
        phone_type (GeneratePhoneNumberLiveCallRouterPhoneType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorsList]
    """

    return (
        await asyncio_detailed(
            client=client,
            country_code=country_code,
            phone_type=phone_type,
        )
    ).parsed
