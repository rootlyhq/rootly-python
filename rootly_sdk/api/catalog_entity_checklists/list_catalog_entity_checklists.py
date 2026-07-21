from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.catalog_entity_checklist_list import CatalogEntityChecklistList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filterstatus: str | Unset = UNSET,
    filtercatalog_checklist_template_id: str | Unset = UNSET,
    filterauditable_type: str | Unset = UNSET,
    filterauditable_id: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
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
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CatalogEntityChecklistList | None:
    if response.status_code == 200:
        response_200 = CatalogEntityChecklistList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
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
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filterstatus: str | Unset = UNSET,
    filtercatalog_checklist_template_id: str | Unset = UNSET,
    filterauditable_type: str | Unset = UNSET,
    filterauditable_id: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
) -> Response[CatalogEntityChecklistList]:
    """List catalog entity checklists

     List catalog entity checklists

    Args:
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filterstatus (str | Unset):
        filtercatalog_checklist_template_id (str | Unset):
        filterauditable_type (str | Unset):
        filterauditable_id (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):

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
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filterstatus: str | Unset = UNSET,
    filtercatalog_checklist_template_id: str | Unset = UNSET,
    filterauditable_type: str | Unset = UNSET,
    filterauditable_id: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
) -> CatalogEntityChecklistList | None:
    """List catalog entity checklists

     List catalog entity checklists

    Args:
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filterstatus (str | Unset):
        filtercatalog_checklist_template_id (str | Unset):
        filterauditable_type (str | Unset):
        filterauditable_id (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):

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
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filterstatus: str | Unset = UNSET,
    filtercatalog_checklist_template_id: str | Unset = UNSET,
    filterauditable_type: str | Unset = UNSET,
    filterauditable_id: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
) -> Response[CatalogEntityChecklistList]:
    """List catalog entity checklists

     List catalog entity checklists

    Args:
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filterstatus (str | Unset):
        filtercatalog_checklist_template_id (str | Unset):
        filterauditable_type (str | Unset):
        filterauditable_id (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):

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
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filterstatus: str | Unset = UNSET,
    filtercatalog_checklist_template_id: str | Unset = UNSET,
    filterauditable_type: str | Unset = UNSET,
    filterauditable_id: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
) -> CatalogEntityChecklistList | None:
    """List catalog entity checklists

     List catalog entity checklists

    Args:
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filterstatus (str | Unset):
        filtercatalog_checklist_template_id (str | Unset):
        filterauditable_type (str | Unset):
        filterauditable_id (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):

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
