from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bulk_destroy_catalog_entities_response import BulkDestroyCatalogEntitiesResponse
from ...models.bulk_destroy_catalog_entities_type_0 import BulkDestroyCatalogEntitiesType0
from ...models.bulk_destroy_catalog_entities_type_1 import BulkDestroyCatalogEntitiesType1
from ...models.errors_list import ErrorsList
from ...types import Response


def _get_kwargs(
    catalog_id: str,
    *,
    body: BulkDestroyCatalogEntitiesType0 | BulkDestroyCatalogEntitiesType1,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/catalogs/{catalog_id}/entities/bulk_delete".format(catalog_id=quote(str(catalog_id), safe=""),),
    }

    
    if isinstance(body, BulkDestroyCatalogEntitiesType0):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body.to_dict()



    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BulkDestroyCatalogEntitiesResponse | BulkDestroyCatalogEntitiesResponse | ErrorsList | ErrorsList | None:
    if response.status_code == 200:
        response_200 = BulkDestroyCatalogEntitiesResponse.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = ErrorsList.from_dict(response.json())



        return response_401

    if response.status_code == 422:
        def _parse_response_422(data: object) -> BulkDestroyCatalogEntitiesResponse | ErrorsList:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_0 = ErrorsList.from_dict(data)



                return response_422_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_422_type_1 = BulkDestroyCatalogEntitiesResponse.from_dict(data)



            return response_422_type_1

        response_422 = _parse_response_422(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BulkDestroyCatalogEntitiesResponse | BulkDestroyCatalogEntitiesResponse | ErrorsList | ErrorsList]:
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
    body: BulkDestroyCatalogEntitiesType0 | BulkDestroyCatalogEntitiesType1,

) -> Response[BulkDestroyCatalogEntitiesResponse | BulkDestroyCatalogEntitiesResponse | ErrorsList | ErrorsList]:
    """ Bulk delete Catalog Entities

     Delete catalog entities by external_id list, or prune by managed_by source. Two mutually exclusive
    modes.

    Args:
        catalog_id (str):
        body (BulkDestroyCatalogEntitiesType0 | BulkDestroyCatalogEntitiesType1): Two mutually
            exclusive modes. Pass exactly one of: external_ids (delete specific entities) or
            managed_by (prune all managed entities not in keep set).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkDestroyCatalogEntitiesResponse | BulkDestroyCatalogEntitiesResponse | ErrorsList | ErrorsList]
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
    body: BulkDestroyCatalogEntitiesType0 | BulkDestroyCatalogEntitiesType1,

) -> BulkDestroyCatalogEntitiesResponse | BulkDestroyCatalogEntitiesResponse | ErrorsList | ErrorsList | None:
    """ Bulk delete Catalog Entities

     Delete catalog entities by external_id list, or prune by managed_by source. Two mutually exclusive
    modes.

    Args:
        catalog_id (str):
        body (BulkDestroyCatalogEntitiesType0 | BulkDestroyCatalogEntitiesType1): Two mutually
            exclusive modes. Pass exactly one of: external_ids (delete specific entities) or
            managed_by (prune all managed entities not in keep set).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkDestroyCatalogEntitiesResponse | BulkDestroyCatalogEntitiesResponse | ErrorsList | ErrorsList
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
    body: BulkDestroyCatalogEntitiesType0 | BulkDestroyCatalogEntitiesType1,

) -> Response[BulkDestroyCatalogEntitiesResponse | BulkDestroyCatalogEntitiesResponse | ErrorsList | ErrorsList]:
    """ Bulk delete Catalog Entities

     Delete catalog entities by external_id list, or prune by managed_by source. Two mutually exclusive
    modes.

    Args:
        catalog_id (str):
        body (BulkDestroyCatalogEntitiesType0 | BulkDestroyCatalogEntitiesType1): Two mutually
            exclusive modes. Pass exactly one of: external_ids (delete specific entities) or
            managed_by (prune all managed entities not in keep set).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkDestroyCatalogEntitiesResponse | BulkDestroyCatalogEntitiesResponse | ErrorsList | ErrorsList]
     """


    kwargs = _get_kwargs(
        catalog_id=catalog_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    catalog_id: str,
    *,
    client: AuthenticatedClient,
    body: BulkDestroyCatalogEntitiesType0 | BulkDestroyCatalogEntitiesType1,

) -> BulkDestroyCatalogEntitiesResponse | BulkDestroyCatalogEntitiesResponse | ErrorsList | ErrorsList | None:
    """ Bulk delete Catalog Entities

     Delete catalog entities by external_id list, or prune by managed_by source. Two mutually exclusive
    modes.

    Args:
        catalog_id (str):
        body (BulkDestroyCatalogEntitiesType0 | BulkDestroyCatalogEntitiesType1): Two mutually
            exclusive modes. Pass exactly one of: external_ids (delete specific entities) or
            managed_by (prune all managed entities not in keep set).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkDestroyCatalogEntitiesResponse | BulkDestroyCatalogEntitiesResponse | ErrorsList | ErrorsList
     """


    return (await asyncio_detailed(
        catalog_id=catalog_id,
client=client,
body=body,

    )).parsed
