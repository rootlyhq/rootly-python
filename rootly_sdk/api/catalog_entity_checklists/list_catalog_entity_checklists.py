from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.catalog_entity_checklist_list import CatalogEntityChecklistList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filterstatus: Union[Unset, str] = UNSET,
    filtercatalog_checklist_template_id: Union[Unset, str] = UNSET,
    filterauditable_type: Union[Unset, str] = UNSET,
    filterauditable_id: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize

    params["filter[status]"] = filterstatus

    params["filter[catalog_checklist_template_id]"] = filtercatalog_checklist_template_id

    params["filter[auditable_type]"] = filterauditable_type

    params["filter[auditable_id]"] = filterauditable_id

    params["filter[created_at][gt]"] = filtercreated_atgt

    params["filter[created_at][gte]"] = filtercreated_atgte

    params["filter[created_at][lt]"] = filtercreated_atlt

    params["filter[created_at][lte]"] = filtercreated_atlte

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/catalog_entity_checklists",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CatalogEntityChecklistList]:
    if response.status_code == 200:
        response_200 = CatalogEntityChecklistList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CatalogEntityChecklistList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filterstatus: Union[Unset, str] = UNSET,
    filtercatalog_checklist_template_id: Union[Unset, str] = UNSET,
    filterauditable_type: Union[Unset, str] = UNSET,
    filterauditable_id: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
) -> Response[CatalogEntityChecklistList]:
    """List catalog entity checklists

     List catalog entity checklists

    Args:
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filterstatus (Union[Unset, str]):
        filtercatalog_checklist_template_id (Union[Unset, str]):
        filterauditable_type (Union[Unset, str]):
        filterauditable_id (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogEntityChecklistList]
    """

    kwargs = _get_kwargs(
        pagenumber=pagenumber,
        pagesize=pagesize,
        filterstatus=filterstatus,
        filtercatalog_checklist_template_id=filtercatalog_checklist_template_id,
        filterauditable_type=filterauditable_type,
        filterauditable_id=filterauditable_id,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filterstatus: Union[Unset, str] = UNSET,
    filtercatalog_checklist_template_id: Union[Unset, str] = UNSET,
    filterauditable_type: Union[Unset, str] = UNSET,
    filterauditable_id: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
) -> Optional[CatalogEntityChecklistList]:
    """List catalog entity checklists

     List catalog entity checklists

    Args:
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filterstatus (Union[Unset, str]):
        filtercatalog_checklist_template_id (Union[Unset, str]):
        filterauditable_type (Union[Unset, str]):
        filterauditable_id (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogEntityChecklistList
    """

    return sync_detailed(
        client=client,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filterstatus=filterstatus,
        filtercatalog_checklist_template_id=filtercatalog_checklist_template_id,
        filterauditable_type=filterauditable_type,
        filterauditable_id=filterauditable_id,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filterstatus: Union[Unset, str] = UNSET,
    filtercatalog_checklist_template_id: Union[Unset, str] = UNSET,
    filterauditable_type: Union[Unset, str] = UNSET,
    filterauditable_id: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
) -> Response[CatalogEntityChecklistList]:
    """List catalog entity checklists

     List catalog entity checklists

    Args:
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filterstatus (Union[Unset, str]):
        filtercatalog_checklist_template_id (Union[Unset, str]):
        filterauditable_type (Union[Unset, str]):
        filterauditable_id (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogEntityChecklistList]
    """

    kwargs = _get_kwargs(
        pagenumber=pagenumber,
        pagesize=pagesize,
        filterstatus=filterstatus,
        filtercatalog_checklist_template_id=filtercatalog_checklist_template_id,
        filterauditable_type=filterauditable_type,
        filterauditable_id=filterauditable_id,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filterstatus: Union[Unset, str] = UNSET,
    filtercatalog_checklist_template_id: Union[Unset, str] = UNSET,
    filterauditable_type: Union[Unset, str] = UNSET,
    filterauditable_id: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
) -> Optional[CatalogEntityChecklistList]:
    """List catalog entity checklists

     List catalog entity checklists

    Args:
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filterstatus (Union[Unset, str]):
        filtercatalog_checklist_template_id (Union[Unset, str]):
        filterauditable_type (Union[Unset, str]):
        filterauditable_id (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogEntityChecklistList
    """

    return (
        await asyncio_detailed(
            client=client,
            pagenumber=pagenumber,
            pagesize=pagesize,
            filterstatus=filterstatus,
            filtercatalog_checklist_template_id=filtercatalog_checklist_template_id,
            filterauditable_type=filterauditable_type,
            filterauditable_id=filterauditable_id,
            filtercreated_atgt=filtercreated_atgt,
            filtercreated_atgte=filtercreated_atgte,
            filtercreated_atlt=filtercreated_atlt,
            filtercreated_atlte=filtercreated_atlte,
        )
    ).parsed
