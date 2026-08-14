from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.audits_list import AuditsList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include: Unset | str = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filtercreated_atgt: Unset | str = UNSET,
    filtercreated_atgte: Unset | str = UNSET,
    filtercreated_atlt: Unset | str = UNSET,
    filtercreated_atlte: Unset | str = UNSET,
    filteruser_id: Unset | str = UNSET,
    filterapi_key_id: Unset | str = UNSET,
    filtersource: Unset | str = UNSET,
    filteritem_type: Unset | str = UNSET,
    filteruser_ideq: Unset | str = UNSET,
    filteruser_idnot_eq: Unset | str = UNSET,
    filteruser_idin: Unset | str = UNSET,
    filteruser_idnot_in: Unset | str = UNSET,
    filterapi_key_ideq: Unset | str = UNSET,
    filterapi_key_idnot_eq: Unset | str = UNSET,
    filterapi_key_idin: Unset | str = UNSET,
    filterapi_key_idnot_in: Unset | str = UNSET,
    filtersourceeq: Unset | str = UNSET,
    filtersourcenot_eq: Unset | str = UNSET,
    filtersourcein: Unset | str = UNSET,
    filtersourcenot_in: Unset | str = UNSET,
    filteritem_typeeq: Unset | str = UNSET,
    filteritem_typenot_eq: Unset | str = UNSET,
    filteritem_typein: Unset | str = UNSET,
    filteritem_typenot_in: Unset | str = UNSET,
    sort: Unset | str = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["include"] = include

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize

    params["filter[created_at][gt]"] = filtercreated_atgt

    params["filter[created_at][gte]"] = filtercreated_atgte

    params["filter[created_at][lt]"] = filtercreated_atlt

    params["filter[created_at][lte]"] = filtercreated_atlte

    params["filter[user_id]"] = filteruser_id

    params["filter[api_key_id]"] = filterapi_key_id

    params["filter[source]"] = filtersource

    params["filter[item_type]"] = filteritem_type

    params["filter[user_id][eq]"] = filteruser_ideq

    params["filter[user_id][not_eq]"] = filteruser_idnot_eq

    params["filter[user_id][in]"] = filteruser_idin

    params["filter[user_id][not_in]"] = filteruser_idnot_in

    params["filter[api_key_id][eq]"] = filterapi_key_ideq

    params["filter[api_key_id][not_eq]"] = filterapi_key_idnot_eq

    params["filter[api_key_id][in]"] = filterapi_key_idin

    params["filter[api_key_id][not_in]"] = filterapi_key_idnot_in

    params["filter[source][eq]"] = filtersourceeq

    params["filter[source][not_eq]"] = filtersourcenot_eq

    params["filter[source][in]"] = filtersourcein

    params["filter[source][not_in]"] = filtersourcenot_in

    params["filter[item_type][eq]"] = filteritem_typeeq

    params["filter[item_type][not_eq]"] = filteritem_typenot_eq

    params["filter[item_type][in]"] = filteritem_typein

    params["filter[item_type][not_in]"] = filteritem_typenot_in

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/audits",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AuditsList | None:
    if response.status_code == 200:
        response_200 = AuditsList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AuditsList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    include: Unset | str = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filtercreated_atgt: Unset | str = UNSET,
    filtercreated_atgte: Unset | str = UNSET,
    filtercreated_atlt: Unset | str = UNSET,
    filtercreated_atlte: Unset | str = UNSET,
    filteruser_id: Unset | str = UNSET,
    filterapi_key_id: Unset | str = UNSET,
    filtersource: Unset | str = UNSET,
    filteritem_type: Unset | str = UNSET,
    filteruser_ideq: Unset | str = UNSET,
    filteruser_idnot_eq: Unset | str = UNSET,
    filteruser_idin: Unset | str = UNSET,
    filteruser_idnot_in: Unset | str = UNSET,
    filterapi_key_ideq: Unset | str = UNSET,
    filterapi_key_idnot_eq: Unset | str = UNSET,
    filterapi_key_idin: Unset | str = UNSET,
    filterapi_key_idnot_in: Unset | str = UNSET,
    filtersourceeq: Unset | str = UNSET,
    filtersourcenot_eq: Unset | str = UNSET,
    filtersourcein: Unset | str = UNSET,
    filtersourcenot_in: Unset | str = UNSET,
    filteritem_typeeq: Unset | str = UNSET,
    filteritem_typenot_eq: Unset | str = UNSET,
    filteritem_typein: Unset | str = UNSET,
    filteritem_typenot_in: Unset | str = UNSET,
    sort: Unset | str = UNSET,
) -> Response[AuditsList]:
    """List audits

     List audits

    Args:
        include (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        filteruser_id (Union[Unset, str]):
        filterapi_key_id (Union[Unset, str]):
        filtersource (Union[Unset, str]):
        filteritem_type (Union[Unset, str]):
        filteruser_ideq (Union[Unset, str]):
        filteruser_idnot_eq (Union[Unset, str]):
        filteruser_idin (Union[Unset, str]):
        filteruser_idnot_in (Union[Unset, str]):
        filterapi_key_ideq (Union[Unset, str]):
        filterapi_key_idnot_eq (Union[Unset, str]):
        filterapi_key_idin (Union[Unset, str]):
        filterapi_key_idnot_in (Union[Unset, str]):
        filtersourceeq (Union[Unset, str]):
        filtersourcenot_eq (Union[Unset, str]):
        filtersourcein (Union[Unset, str]):
        filtersourcenot_in (Union[Unset, str]):
        filteritem_typeeq (Union[Unset, str]):
        filteritem_typenot_eq (Union[Unset, str]):
        filteritem_typein (Union[Unset, str]):
        filteritem_typenot_in (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditsList]
    """

    kwargs = _get_kwargs(
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        filteruser_id=filteruser_id,
        filterapi_key_id=filterapi_key_id,
        filtersource=filtersource,
        filteritem_type=filteritem_type,
        filteruser_ideq=filteruser_ideq,
        filteruser_idnot_eq=filteruser_idnot_eq,
        filteruser_idin=filteruser_idin,
        filteruser_idnot_in=filteruser_idnot_in,
        filterapi_key_ideq=filterapi_key_ideq,
        filterapi_key_idnot_eq=filterapi_key_idnot_eq,
        filterapi_key_idin=filterapi_key_idin,
        filterapi_key_idnot_in=filterapi_key_idnot_in,
        filtersourceeq=filtersourceeq,
        filtersourcenot_eq=filtersourcenot_eq,
        filtersourcein=filtersourcein,
        filtersourcenot_in=filtersourcenot_in,
        filteritem_typeeq=filteritem_typeeq,
        filteritem_typenot_eq=filteritem_typenot_eq,
        filteritem_typein=filteritem_typein,
        filteritem_typenot_in=filteritem_typenot_in,
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    include: Unset | str = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filtercreated_atgt: Unset | str = UNSET,
    filtercreated_atgte: Unset | str = UNSET,
    filtercreated_atlt: Unset | str = UNSET,
    filtercreated_atlte: Unset | str = UNSET,
    filteruser_id: Unset | str = UNSET,
    filterapi_key_id: Unset | str = UNSET,
    filtersource: Unset | str = UNSET,
    filteritem_type: Unset | str = UNSET,
    filteruser_ideq: Unset | str = UNSET,
    filteruser_idnot_eq: Unset | str = UNSET,
    filteruser_idin: Unset | str = UNSET,
    filteruser_idnot_in: Unset | str = UNSET,
    filterapi_key_ideq: Unset | str = UNSET,
    filterapi_key_idnot_eq: Unset | str = UNSET,
    filterapi_key_idin: Unset | str = UNSET,
    filterapi_key_idnot_in: Unset | str = UNSET,
    filtersourceeq: Unset | str = UNSET,
    filtersourcenot_eq: Unset | str = UNSET,
    filtersourcein: Unset | str = UNSET,
    filtersourcenot_in: Unset | str = UNSET,
    filteritem_typeeq: Unset | str = UNSET,
    filteritem_typenot_eq: Unset | str = UNSET,
    filteritem_typein: Unset | str = UNSET,
    filteritem_typenot_in: Unset | str = UNSET,
    sort: Unset | str = UNSET,
) -> AuditsList | None:
    """List audits

     List audits

    Args:
        include (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        filteruser_id (Union[Unset, str]):
        filterapi_key_id (Union[Unset, str]):
        filtersource (Union[Unset, str]):
        filteritem_type (Union[Unset, str]):
        filteruser_ideq (Union[Unset, str]):
        filteruser_idnot_eq (Union[Unset, str]):
        filteruser_idin (Union[Unset, str]):
        filteruser_idnot_in (Union[Unset, str]):
        filterapi_key_ideq (Union[Unset, str]):
        filterapi_key_idnot_eq (Union[Unset, str]):
        filterapi_key_idin (Union[Unset, str]):
        filterapi_key_idnot_in (Union[Unset, str]):
        filtersourceeq (Union[Unset, str]):
        filtersourcenot_eq (Union[Unset, str]):
        filtersourcein (Union[Unset, str]):
        filtersourcenot_in (Union[Unset, str]):
        filteritem_typeeq (Union[Unset, str]):
        filteritem_typenot_eq (Union[Unset, str]):
        filteritem_typein (Union[Unset, str]):
        filteritem_typenot_in (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditsList
    """

    return sync_detailed(
        client=client,
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        filteruser_id=filteruser_id,
        filterapi_key_id=filterapi_key_id,
        filtersource=filtersource,
        filteritem_type=filteritem_type,
        filteruser_ideq=filteruser_ideq,
        filteruser_idnot_eq=filteruser_idnot_eq,
        filteruser_idin=filteruser_idin,
        filteruser_idnot_in=filteruser_idnot_in,
        filterapi_key_ideq=filterapi_key_ideq,
        filterapi_key_idnot_eq=filterapi_key_idnot_eq,
        filterapi_key_idin=filterapi_key_idin,
        filterapi_key_idnot_in=filterapi_key_idnot_in,
        filtersourceeq=filtersourceeq,
        filtersourcenot_eq=filtersourcenot_eq,
        filtersourcein=filtersourcein,
        filtersourcenot_in=filtersourcenot_in,
        filteritem_typeeq=filteritem_typeeq,
        filteritem_typenot_eq=filteritem_typenot_eq,
        filteritem_typein=filteritem_typein,
        filteritem_typenot_in=filteritem_typenot_in,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    include: Unset | str = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filtercreated_atgt: Unset | str = UNSET,
    filtercreated_atgte: Unset | str = UNSET,
    filtercreated_atlt: Unset | str = UNSET,
    filtercreated_atlte: Unset | str = UNSET,
    filteruser_id: Unset | str = UNSET,
    filterapi_key_id: Unset | str = UNSET,
    filtersource: Unset | str = UNSET,
    filteritem_type: Unset | str = UNSET,
    filteruser_ideq: Unset | str = UNSET,
    filteruser_idnot_eq: Unset | str = UNSET,
    filteruser_idin: Unset | str = UNSET,
    filteruser_idnot_in: Unset | str = UNSET,
    filterapi_key_ideq: Unset | str = UNSET,
    filterapi_key_idnot_eq: Unset | str = UNSET,
    filterapi_key_idin: Unset | str = UNSET,
    filterapi_key_idnot_in: Unset | str = UNSET,
    filtersourceeq: Unset | str = UNSET,
    filtersourcenot_eq: Unset | str = UNSET,
    filtersourcein: Unset | str = UNSET,
    filtersourcenot_in: Unset | str = UNSET,
    filteritem_typeeq: Unset | str = UNSET,
    filteritem_typenot_eq: Unset | str = UNSET,
    filteritem_typein: Unset | str = UNSET,
    filteritem_typenot_in: Unset | str = UNSET,
    sort: Unset | str = UNSET,
) -> Response[AuditsList]:
    """List audits

     List audits

    Args:
        include (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        filteruser_id (Union[Unset, str]):
        filterapi_key_id (Union[Unset, str]):
        filtersource (Union[Unset, str]):
        filteritem_type (Union[Unset, str]):
        filteruser_ideq (Union[Unset, str]):
        filteruser_idnot_eq (Union[Unset, str]):
        filteruser_idin (Union[Unset, str]):
        filteruser_idnot_in (Union[Unset, str]):
        filterapi_key_ideq (Union[Unset, str]):
        filterapi_key_idnot_eq (Union[Unset, str]):
        filterapi_key_idin (Union[Unset, str]):
        filterapi_key_idnot_in (Union[Unset, str]):
        filtersourceeq (Union[Unset, str]):
        filtersourcenot_eq (Union[Unset, str]):
        filtersourcein (Union[Unset, str]):
        filtersourcenot_in (Union[Unset, str]):
        filteritem_typeeq (Union[Unset, str]):
        filteritem_typenot_eq (Union[Unset, str]):
        filteritem_typein (Union[Unset, str]):
        filteritem_typenot_in (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditsList]
    """

    kwargs = _get_kwargs(
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        filteruser_id=filteruser_id,
        filterapi_key_id=filterapi_key_id,
        filtersource=filtersource,
        filteritem_type=filteritem_type,
        filteruser_ideq=filteruser_ideq,
        filteruser_idnot_eq=filteruser_idnot_eq,
        filteruser_idin=filteruser_idin,
        filteruser_idnot_in=filteruser_idnot_in,
        filterapi_key_ideq=filterapi_key_ideq,
        filterapi_key_idnot_eq=filterapi_key_idnot_eq,
        filterapi_key_idin=filterapi_key_idin,
        filterapi_key_idnot_in=filterapi_key_idnot_in,
        filtersourceeq=filtersourceeq,
        filtersourcenot_eq=filtersourcenot_eq,
        filtersourcein=filtersourcein,
        filtersourcenot_in=filtersourcenot_in,
        filteritem_typeeq=filteritem_typeeq,
        filteritem_typenot_eq=filteritem_typenot_eq,
        filteritem_typein=filteritem_typein,
        filteritem_typenot_in=filteritem_typenot_in,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    include: Unset | str = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filtercreated_atgt: Unset | str = UNSET,
    filtercreated_atgte: Unset | str = UNSET,
    filtercreated_atlt: Unset | str = UNSET,
    filtercreated_atlte: Unset | str = UNSET,
    filteruser_id: Unset | str = UNSET,
    filterapi_key_id: Unset | str = UNSET,
    filtersource: Unset | str = UNSET,
    filteritem_type: Unset | str = UNSET,
    filteruser_ideq: Unset | str = UNSET,
    filteruser_idnot_eq: Unset | str = UNSET,
    filteruser_idin: Unset | str = UNSET,
    filteruser_idnot_in: Unset | str = UNSET,
    filterapi_key_ideq: Unset | str = UNSET,
    filterapi_key_idnot_eq: Unset | str = UNSET,
    filterapi_key_idin: Unset | str = UNSET,
    filterapi_key_idnot_in: Unset | str = UNSET,
    filtersourceeq: Unset | str = UNSET,
    filtersourcenot_eq: Unset | str = UNSET,
    filtersourcein: Unset | str = UNSET,
    filtersourcenot_in: Unset | str = UNSET,
    filteritem_typeeq: Unset | str = UNSET,
    filteritem_typenot_eq: Unset | str = UNSET,
    filteritem_typein: Unset | str = UNSET,
    filteritem_typenot_in: Unset | str = UNSET,
    sort: Unset | str = UNSET,
) -> AuditsList | None:
    """List audits

     List audits

    Args:
        include (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        filteruser_id (Union[Unset, str]):
        filterapi_key_id (Union[Unset, str]):
        filtersource (Union[Unset, str]):
        filteritem_type (Union[Unset, str]):
        filteruser_ideq (Union[Unset, str]):
        filteruser_idnot_eq (Union[Unset, str]):
        filteruser_idin (Union[Unset, str]):
        filteruser_idnot_in (Union[Unset, str]):
        filterapi_key_ideq (Union[Unset, str]):
        filterapi_key_idnot_eq (Union[Unset, str]):
        filterapi_key_idin (Union[Unset, str]):
        filterapi_key_idnot_in (Union[Unset, str]):
        filtersourceeq (Union[Unset, str]):
        filtersourcenot_eq (Union[Unset, str]):
        filtersourcein (Union[Unset, str]):
        filtersourcenot_in (Union[Unset, str]):
        filteritem_typeeq (Union[Unset, str]):
        filteritem_typenot_eq (Union[Unset, str]):
        filteritem_typein (Union[Unset, str]):
        filteritem_typenot_in (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditsList
    """

    return (
        await asyncio_detailed(
            client=client,
            include=include,
            pagenumber=pagenumber,
            pagesize=pagesize,
            filtercreated_atgt=filtercreated_atgt,
            filtercreated_atgte=filtercreated_atgte,
            filtercreated_atlt=filtercreated_atlt,
            filtercreated_atlte=filtercreated_atlte,
            filteruser_id=filteruser_id,
            filterapi_key_id=filterapi_key_id,
            filtersource=filtersource,
            filteritem_type=filteritem_type,
            filteruser_ideq=filteruser_ideq,
            filteruser_idnot_eq=filteruser_idnot_eq,
            filteruser_idin=filteruser_idin,
            filteruser_idnot_in=filteruser_idnot_in,
            filterapi_key_ideq=filterapi_key_ideq,
            filterapi_key_idnot_eq=filterapi_key_idnot_eq,
            filterapi_key_idin=filterapi_key_idin,
            filterapi_key_idnot_in=filterapi_key_idnot_in,
            filtersourceeq=filtersourceeq,
            filtersourcenot_eq=filtersourcenot_eq,
            filtersourcein=filtersourcein,
            filtersourcenot_in=filtersourcenot_in,
            filteritem_typeeq=filteritem_typeeq,
            filteritem_typenot_eq=filteritem_typenot_eq,
            filteritem_typein=filteritem_typein,
            filteritem_typenot_in=filteritem_typenot_in,
            sort=sort,
        )
    ).parsed
