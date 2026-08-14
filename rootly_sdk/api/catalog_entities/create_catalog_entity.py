from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.catalog_entity_response import CatalogEntityResponse
from ...models.errors_list import ErrorsList
from ...models.new_catalog_entity import NewCatalogEntity
from ...types import Response


def _get_kwargs(
    catalog_id: str,
    *,
    body: NewCatalogEntity,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/v1/catalogs/{catalog_id}/entities",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CatalogEntityResponse | ErrorsList | None:
    if response.status_code == 201:
        response_201 = CatalogEntityResponse.from_dict(response.json())

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
) -> Response[CatalogEntityResponse | ErrorsList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    catalog_id: str,
    *,
    client: AuthenticatedClient,
    body: NewCatalogEntity,
) -> Response[CatalogEntityResponse | ErrorsList]:
    """Creates a Catalog Entity

     Creates a new Catalog Entity from provided data

    Args:
        catalog_id (str):
        body (NewCatalogEntity):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CatalogEntityResponse, ErrorsList]]
    """

    kwargs = _get_kwargs(
        catalog_id=catalog_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    catalog_id: str,
    *,
    client: AuthenticatedClient,
    body: NewCatalogEntity,
) -> CatalogEntityResponse | ErrorsList | None:
    """Creates a Catalog Entity

     Creates a new Catalog Entity from provided data

    Args:
        catalog_id (str):
        body (NewCatalogEntity):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CatalogEntityResponse, ErrorsList]
    """

    return sync_detailed(
        catalog_id=catalog_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    catalog_id: str,
    *,
    client: AuthenticatedClient,
    body: NewCatalogEntity,
) -> Response[CatalogEntityResponse | ErrorsList]:
    """Creates a Catalog Entity

     Creates a new Catalog Entity from provided data

    Args:
        catalog_id (str):
        body (NewCatalogEntity):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CatalogEntityResponse, ErrorsList]]
    """

    kwargs = _get_kwargs(
        catalog_id=catalog_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    catalog_id: str,
    *,
    client: AuthenticatedClient,
    body: NewCatalogEntity,
) -> CatalogEntityResponse | ErrorsList | None:
    """Creates a Catalog Entity

     Creates a new Catalog Entity from provided data

    Args:
        catalog_id (str):
        body (NewCatalogEntity):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CatalogEntityResponse, ErrorsList]
    """

    return (
        await asyncio_detailed(
            catalog_id=catalog_id,
            client=client,
            body=body,
        )
    ).parsed
