from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.catalog_entity_property_response import CatalogEntityPropertyResponse
from ...models.errors_list import ErrorsList
from ...models.get_catalog_entity_property_include import (
    GetCatalogEntityPropertyInclude,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    include: Union[Unset, GetCatalogEntityPropertyInclude] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_include: Union[Unset, str] = UNSET
    if not isinstance(include, Unset):
        json_include = include

    params["include"] = json_include

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/catalog_entity_properties/{id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CatalogEntityPropertyResponse, ErrorsList]]:
    if response.status_code == 200:
        response_200 = CatalogEntityPropertyResponse.from_dict(response.json())

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
) -> Response[Union[CatalogEntityPropertyResponse, ErrorsList]]:
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
    include: Union[Unset, GetCatalogEntityPropertyInclude] = UNSET,
) -> Response[Union[CatalogEntityPropertyResponse, ErrorsList]]:
    """Retrieves a Catalog Entity Property

     **Deprecated:** This endpoint is deprecated, please use `include=fields` on catalog entities or
    native catalog endpoints (teams, services, functionalities, incident_types, causes, environments) to
    retrieve field values instead.

    Retrieves a specific Catalog Entity Property by id.

    Args:
        id (str):
        include (Union[Unset, GetCatalogEntityPropertyInclude]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CatalogEntityPropertyResponse, ErrorsList]]
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
    include: Union[Unset, GetCatalogEntityPropertyInclude] = UNSET,
) -> Optional[Union[CatalogEntityPropertyResponse, ErrorsList]]:
    """Retrieves a Catalog Entity Property

     **Deprecated:** This endpoint is deprecated, please use `include=fields` on catalog entities or
    native catalog endpoints (teams, services, functionalities, incident_types, causes, environments) to
    retrieve field values instead.

    Retrieves a specific Catalog Entity Property by id.

    Args:
        id (str):
        include (Union[Unset, GetCatalogEntityPropertyInclude]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CatalogEntityPropertyResponse, ErrorsList]
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
    include: Union[Unset, GetCatalogEntityPropertyInclude] = UNSET,
) -> Response[Union[CatalogEntityPropertyResponse, ErrorsList]]:
    """Retrieves a Catalog Entity Property

     **Deprecated:** This endpoint is deprecated, please use `include=fields` on catalog entities or
    native catalog endpoints (teams, services, functionalities, incident_types, causes, environments) to
    retrieve field values instead.

    Retrieves a specific Catalog Entity Property by id.

    Args:
        id (str):
        include (Union[Unset, GetCatalogEntityPropertyInclude]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CatalogEntityPropertyResponse, ErrorsList]]
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
    include: Union[Unset, GetCatalogEntityPropertyInclude] = UNSET,
) -> Optional[Union[CatalogEntityPropertyResponse, ErrorsList]]:
    """Retrieves a Catalog Entity Property

     **Deprecated:** This endpoint is deprecated, please use `include=fields` on catalog entities or
    native catalog endpoints (teams, services, functionalities, incident_types, causes, environments) to
    retrieve field values instead.

    Retrieves a specific Catalog Entity Property by id.

    Args:
        id (str):
        include (Union[Unset, GetCatalogEntityPropertyInclude]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CatalogEntityPropertyResponse, ErrorsList]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            include=include,
        )
    ).parsed
