from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.catalog_property_response import CatalogPropertyResponse
from ...models.errors_list import ErrorsList
from ...models.new_catalog_property import NewCatalogProperty
from ...types import Response


def _get_kwargs(
    *,
    body: NewCatalogProperty,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/incident_types/properties",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CatalogPropertyResponse | ErrorsList | None:
    if response.status_code == 201:
        response_201 = CatalogPropertyResponse.from_dict(response.json())

        return response_201

    if response.status_code == 401:
        response_401 = ErrorsList.from_dict(response.json())

        return response_401

    if response.status_code == 422:
        response_422 = ErrorsList.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CatalogPropertyResponse | ErrorsList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: NewCatalogProperty,
) -> Response[CatalogPropertyResponse | ErrorsList]:
    """Creates a Catalog Property

     Creates a new Catalog Property from provided data

    Args:
        body (NewCatalogProperty): A catalog can have a maximum of 50 properties.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogPropertyResponse | ErrorsList]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: NewCatalogProperty,
) -> CatalogPropertyResponse | ErrorsList | None:
    """Creates a Catalog Property

     Creates a new Catalog Property from provided data

    Args:
        body (NewCatalogProperty): A catalog can have a maximum of 50 properties.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogPropertyResponse | ErrorsList
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: NewCatalogProperty,
) -> Response[CatalogPropertyResponse | ErrorsList]:
    """Creates a Catalog Property

     Creates a new Catalog Property from provided data

    Args:
        body (NewCatalogProperty): A catalog can have a maximum of 50 properties.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogPropertyResponse | ErrorsList]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: NewCatalogProperty,
) -> CatalogPropertyResponse | ErrorsList | None:
    """Creates a Catalog Property

     Creates a new Catalog Property from provided data

    Args:
        body (NewCatalogProperty): A catalog can have a maximum of 50 properties.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogPropertyResponse | ErrorsList
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
