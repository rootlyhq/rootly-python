from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.custom_field_response import CustomFieldResponse
from ...models.errors_list import ErrorsList
from ...models.get_custom_field_include import GetCustomFieldInclude
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    include: Unset | GetCustomFieldInclude = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_include: Unset | str = UNSET
    if not isinstance(include, Unset):
        json_include = include

    params["include"] = json_include

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/custom_fields/{id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CustomFieldResponse | ErrorsList | None:
    if response.status_code == 200:
        response_200 = CustomFieldResponse.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = ErrorsList.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CustomFieldResponse | ErrorsList]:
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
    include: Unset | GetCustomFieldInclude = UNSET,
) -> Response[CustomFieldResponse | ErrorsList]:
    """[DEPRECATED] Retrieves a Custom Field

     Retrieves a specific custom_field by id

    Args:
        id (str):
        include (Union[Unset, GetCustomFieldInclude]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CustomFieldResponse, ErrorsList]]
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
    include: Unset | GetCustomFieldInclude = UNSET,
) -> CustomFieldResponse | ErrorsList | None:
    """[DEPRECATED] Retrieves a Custom Field

     Retrieves a specific custom_field by id

    Args:
        id (str):
        include (Union[Unset, GetCustomFieldInclude]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CustomFieldResponse, ErrorsList]
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
    include: Unset | GetCustomFieldInclude = UNSET,
) -> Response[CustomFieldResponse | ErrorsList]:
    """[DEPRECATED] Retrieves a Custom Field

     Retrieves a specific custom_field by id

    Args:
        id (str):
        include (Union[Unset, GetCustomFieldInclude]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CustomFieldResponse, ErrorsList]]
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
    include: Unset | GetCustomFieldInclude = UNSET,
) -> CustomFieldResponse | ErrorsList | None:
    """[DEPRECATED] Retrieves a Custom Field

     Retrieves a specific custom_field by id

    Args:
        id (str):
        include (Union[Unset, GetCustomFieldInclude]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CustomFieldResponse, ErrorsList]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            include=include,
        )
    ).parsed
