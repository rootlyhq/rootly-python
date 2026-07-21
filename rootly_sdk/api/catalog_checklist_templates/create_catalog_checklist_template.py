from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.catalog_checklist_template_response import CatalogChecklistTemplateResponse
from ...models.errors_list import ErrorsList
from ...models.new_catalog_checklist_template import NewCatalogChecklistTemplate
from ...types import Response


def _get_kwargs(
    *,
    body: NewCatalogChecklistTemplate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/catalog_checklist_templates",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CatalogChecklistTemplateResponse | ErrorsList | None:
    if response.status_code == 201:
        response_201 = CatalogChecklistTemplateResponse.from_dict(response.json())

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
) -> Response[CatalogChecklistTemplateResponse | ErrorsList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: NewCatalogChecklistTemplate,
) -> Response[CatalogChecklistTemplateResponse | ErrorsList]:
    """Creates a catalog checklist template

     Creates a new catalog checklist template

    Args:
        body (NewCatalogChecklistTemplate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogChecklistTemplateResponse | ErrorsList]
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
    body: NewCatalogChecklistTemplate,
) -> CatalogChecklistTemplateResponse | ErrorsList | None:
    """Creates a catalog checklist template

     Creates a new catalog checklist template

    Args:
        body (NewCatalogChecklistTemplate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogChecklistTemplateResponse | ErrorsList
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: NewCatalogChecklistTemplate,
) -> Response[CatalogChecklistTemplateResponse | ErrorsList]:
    """Creates a catalog checklist template

     Creates a new catalog checklist template

    Args:
        body (NewCatalogChecklistTemplate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogChecklistTemplateResponse | ErrorsList]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: NewCatalogChecklistTemplate,
) -> CatalogChecklistTemplateResponse | ErrorsList | None:
    """Creates a catalog checklist template

     Creates a new catalog checklist template

    Args:
        body (NewCatalogChecklistTemplate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogChecklistTemplateResponse | ErrorsList
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
