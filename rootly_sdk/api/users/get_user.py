from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors_list import ErrorsList
from ...models.get_user_include import GetUserInclude
from ...models.user_response import UserResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    include: Union[Unset, GetUserInclude] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_include: Union[Unset, str] = UNSET
    if not isinstance(include, Unset):
        json_include = include.value

    params["include"] = json_include

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/users/{id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorsList, UserResponse]]:
    if response.status_code == 200:
        response_200 = UserResponse.from_dict(response.json())

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
) -> Response[Union[ErrorsList, UserResponse]]:
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
    include: Union[Unset, GetUserInclude] = UNSET,
) -> Response[Union[ErrorsList, UserResponse]]:
    """Retrieves an user

     Retrieves a specific user by id

    Args:
        id (str):
        include (Union[Unset, GetUserInclude]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, UserResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        include=include,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    include: Union[Unset, GetUserInclude] = UNSET,
) -> Optional[Union[ErrorsList, UserResponse]]:
    """Retrieves an user

     Retrieves a specific user by id

    Args:
        id (str):
        include (Union[Unset, GetUserInclude]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, UserResponse]
    """

    return sync_detailed(
        id=id,
        client=client,
        include=include,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    include: Union[Unset, GetUserInclude] = UNSET,
) -> Response[Union[ErrorsList, UserResponse]]:
    """Retrieves an user

     Retrieves a specific user by id

    Args:
        id (str):
        include (Union[Unset, GetUserInclude]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, UserResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        include=include,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    include: Union[Unset, GetUserInclude] = UNSET,
) -> Optional[Union[ErrorsList, UserResponse]]:
    """Retrieves an user

     Retrieves a specific user by id

    Args:
        id (str):
        include (Union[Unset, GetUserInclude]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, UserResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            include=include,
        )
    ).parsed
