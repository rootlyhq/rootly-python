from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.catalog_entity_property_response import CatalogEntityPropertyResponse
from ...models.errors_list import ErrorsList
from ...models.update_catalog_entity_property import UpdateCatalogEntityProperty
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: UpdateCatalogEntityProperty,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/v1/catalog_entity_properties/{id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
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
    body: UpdateCatalogEntityProperty,
) -> Response[Union[CatalogEntityPropertyResponse, ErrorsList]]:
    """Update a Catalog Entity Property

     **Deprecated:** This endpoint is deprecated, please use the `fields` attribute on catalog entities
    or native catalog endpoints (teams, services, functionalities, incident_types, causes, environments)
    to set field values instead.

    Update a specific Catalog Entity Property by id.

    Args:
        id (str):
        body (UpdateCatalogEntityProperty): **Deprecated:** This endpoint is deprecated, please
            use the `fields` attribute on catalog entities or native catalog endpoints (teams,
            services, functionalities, incident_types, causes, environments) to set field values
            instead.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CatalogEntityPropertyResponse, ErrorsList]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateCatalogEntityProperty,
) -> Optional[Union[CatalogEntityPropertyResponse, ErrorsList]]:
    """Update a Catalog Entity Property

     **Deprecated:** This endpoint is deprecated, please use the `fields` attribute on catalog entities
    or native catalog endpoints (teams, services, functionalities, incident_types, causes, environments)
    to set field values instead.

    Update a specific Catalog Entity Property by id.

    Args:
        id (str):
        body (UpdateCatalogEntityProperty): **Deprecated:** This endpoint is deprecated, please
            use the `fields` attribute on catalog entities or native catalog endpoints (teams,
            services, functionalities, incident_types, causes, environments) to set field values
            instead.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CatalogEntityPropertyResponse, ErrorsList]
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateCatalogEntityProperty,
) -> Response[Union[CatalogEntityPropertyResponse, ErrorsList]]:
    """Update a Catalog Entity Property

     **Deprecated:** This endpoint is deprecated, please use the `fields` attribute on catalog entities
    or native catalog endpoints (teams, services, functionalities, incident_types, causes, environments)
    to set field values instead.

    Update a specific Catalog Entity Property by id.

    Args:
        id (str):
        body (UpdateCatalogEntityProperty): **Deprecated:** This endpoint is deprecated, please
            use the `fields` attribute on catalog entities or native catalog endpoints (teams,
            services, functionalities, incident_types, causes, environments) to set field values
            instead.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CatalogEntityPropertyResponse, ErrorsList]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateCatalogEntityProperty,
) -> Optional[Union[CatalogEntityPropertyResponse, ErrorsList]]:
    """Update a Catalog Entity Property

     **Deprecated:** This endpoint is deprecated, please use the `fields` attribute on catalog entities
    or native catalog endpoints (teams, services, functionalities, incident_types, causes, environments)
    to set field values instead.

    Update a specific Catalog Entity Property by id.

    Args:
        id (str):
        body (UpdateCatalogEntityProperty): **Deprecated:** This endpoint is deprecated, please
            use the `fields` attribute on catalog entities or native catalog endpoints (teams,
            services, functionalities, incident_types, causes, environments) to set field values
            instead.

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
            body=body,
        )
    ).parsed
