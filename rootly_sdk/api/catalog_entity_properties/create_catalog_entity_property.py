from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.catalog_entity_property_response import CatalogEntityPropertyResponse
from ...models.errors_list import ErrorsList
from ...models.new_catalog_entity_property import NewCatalogEntityProperty
from ...types import Response


def _get_kwargs(
    catalog_entity_id: str,
    *,
    body: NewCatalogEntityProperty,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/v1/catalog_entities/{catalog_entity_id}/properties",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CatalogEntityPropertyResponse, ErrorsList]]:
    if response.status_code == 201:
        response_201 = CatalogEntityPropertyResponse.from_dict(response.json())

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
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[CatalogEntityPropertyResponse, ErrorsList]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    catalog_entity_id: str,
    *,
    client: AuthenticatedClient,
    body: NewCatalogEntityProperty,
) -> Response[Union[CatalogEntityPropertyResponse, ErrorsList]]:
    """Creates a Catalog Entity Property

     **Deprecated:** This endpoint is deprecated, please use the `fields` attribute on catalog entities
    or native catalog endpoints (teams, services, functionalities, incident_types, causes, environments)
    to set field values instead.

    Creates a new Catalog Entity Property from provided data.

    Args:
        catalog_entity_id (str):
        body (NewCatalogEntityProperty): **Deprecated:** This endpoint is deprecated, please use
            the `fields` attribute on catalog entities or native catalog endpoints (teams, services,
            functionalities, incident_types, causes, environments) to set field values instead.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CatalogEntityPropertyResponse, ErrorsList]]
    """

    kwargs = _get_kwargs(
        catalog_entity_id=catalog_entity_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    catalog_entity_id: str,
    *,
    client: AuthenticatedClient,
    body: NewCatalogEntityProperty,
) -> Optional[Union[CatalogEntityPropertyResponse, ErrorsList]]:
    """Creates a Catalog Entity Property

     **Deprecated:** This endpoint is deprecated, please use the `fields` attribute on catalog entities
    or native catalog endpoints (teams, services, functionalities, incident_types, causes, environments)
    to set field values instead.

    Creates a new Catalog Entity Property from provided data.

    Args:
        catalog_entity_id (str):
        body (NewCatalogEntityProperty): **Deprecated:** This endpoint is deprecated, please use
            the `fields` attribute on catalog entities or native catalog endpoints (teams, services,
            functionalities, incident_types, causes, environments) to set field values instead.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CatalogEntityPropertyResponse, ErrorsList]
    """

    return sync_detailed(
        catalog_entity_id=catalog_entity_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    catalog_entity_id: str,
    *,
    client: AuthenticatedClient,
    body: NewCatalogEntityProperty,
) -> Response[Union[CatalogEntityPropertyResponse, ErrorsList]]:
    """Creates a Catalog Entity Property

     **Deprecated:** This endpoint is deprecated, please use the `fields` attribute on catalog entities
    or native catalog endpoints (teams, services, functionalities, incident_types, causes, environments)
    to set field values instead.

    Creates a new Catalog Entity Property from provided data.

    Args:
        catalog_entity_id (str):
        body (NewCatalogEntityProperty): **Deprecated:** This endpoint is deprecated, please use
            the `fields` attribute on catalog entities or native catalog endpoints (teams, services,
            functionalities, incident_types, causes, environments) to set field values instead.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CatalogEntityPropertyResponse, ErrorsList]]
    """

    kwargs = _get_kwargs(
        catalog_entity_id=catalog_entity_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    catalog_entity_id: str,
    *,
    client: AuthenticatedClient,
    body: NewCatalogEntityProperty,
) -> Optional[Union[CatalogEntityPropertyResponse, ErrorsList]]:
    """Creates a Catalog Entity Property

     **Deprecated:** This endpoint is deprecated, please use the `fields` attribute on catalog entities
    or native catalog endpoints (teams, services, functionalities, incident_types, causes, environments)
    to set field values instead.

    Creates a new Catalog Entity Property from provided data.

    Args:
        catalog_entity_id (str):
        body (NewCatalogEntityProperty): **Deprecated:** This endpoint is deprecated, please use
            the `fields` attribute on catalog entities or native catalog endpoints (teams, services,
            functionalities, incident_types, causes, environments) to set field values instead.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CatalogEntityPropertyResponse, ErrorsList]
    """

    return (
        await asyncio_detailed(
            catalog_entity_id=catalog_entity_id,
            client=client,
            body=body,
        )
    ).parsed
