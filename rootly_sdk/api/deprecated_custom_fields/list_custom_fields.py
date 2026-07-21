from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.custom_field_list import CustomFieldList
from ...models.list_custom_fields_include import ListCustomFieldsInclude
from ...models.list_custom_fields_sort import ListCustomFieldsSort
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include: ListCustomFieldsInclude | Unset = UNSET,
    sort: ListCustomFieldsSort | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filterslug: str | Unset = UNSET,
    filterlabel: str | Unset = UNSET,
    filterkind: str | Unset = UNSET,
    filterenabled: bool | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filterslugeq: str | Unset = UNSET,
    filterslugnot_eq: str | Unset = UNSET,
    filterslugin: str | Unset = UNSET,
    filterslugnot_in: str | Unset = UNSET,
    filterlabeleq: str | Unset = UNSET,
    filterlabelnot_eq: str | Unset = UNSET,
    filterlabelin: str | Unset = UNSET,
    filterlabelnot_in: str | Unset = UNSET,
    filterkindeq: str | Unset = UNSET,
    filterkindnot_eq: str | Unset = UNSET,
    filterkindin: str | Unset = UNSET,
    filterkindnot_in: str | Unset = UNSET,
    filterenabledeq: str | Unset = UNSET,
    filterenablednot_eq: str | Unset = UNSET,
    filterenabledin: str | Unset = UNSET,
    filterenablednot_in: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_include: str | Unset = UNSET
    if not isinstance(include, Unset):
        json_include = include

    params["include"] = json_include

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort

    params["sort"] = json_sort

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize

    params["filter[slug]"] = filterslug

    params["filter[label]"] = filterlabel

    params["filter[kind]"] = filterkind

    params["filter[enabled]"] = filterenabled

    params["filter[created_at][gt]"] = filtercreated_atgt

    params["filter[created_at][gte]"] = filtercreated_atgte

    params["filter[created_at][lt]"] = filtercreated_atlt

    params["filter[created_at][lte]"] = filtercreated_atlte

    params["filter[slug][eq]"] = filterslugeq

    params["filter[slug][not_eq]"] = filterslugnot_eq

    params["filter[slug][in]"] = filterslugin

    params["filter[slug][not_in]"] = filterslugnot_in

    params["filter[label][eq]"] = filterlabeleq

    params["filter[label][not_eq]"] = filterlabelnot_eq

    params["filter[label][in]"] = filterlabelin

    params["filter[label][not_in]"] = filterlabelnot_in

    params["filter[kind][eq]"] = filterkindeq

    params["filter[kind][not_eq]"] = filterkindnot_eq

    params["filter[kind][in]"] = filterkindin

    params["filter[kind][not_in]"] = filterkindnot_in

    params["filter[enabled][eq]"] = filterenabledeq

    params["filter[enabled][not_eq]"] = filterenablednot_eq

    params["filter[enabled][in]"] = filterenabledin

    params["filter[enabled][not_in]"] = filterenablednot_in

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/custom_fields",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CustomFieldList | None:
    if response.status_code == 200:
        response_200 = CustomFieldList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CustomFieldList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    include: ListCustomFieldsInclude | Unset = UNSET,
    sort: ListCustomFieldsSort | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filterslug: str | Unset = UNSET,
    filterlabel: str | Unset = UNSET,
    filterkind: str | Unset = UNSET,
    filterenabled: bool | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filterslugeq: str | Unset = UNSET,
    filterslugnot_eq: str | Unset = UNSET,
    filterslugin: str | Unset = UNSET,
    filterslugnot_in: str | Unset = UNSET,
    filterlabeleq: str | Unset = UNSET,
    filterlabelnot_eq: str | Unset = UNSET,
    filterlabelin: str | Unset = UNSET,
    filterlabelnot_in: str | Unset = UNSET,
    filterkindeq: str | Unset = UNSET,
    filterkindnot_eq: str | Unset = UNSET,
    filterkindin: str | Unset = UNSET,
    filterkindnot_in: str | Unset = UNSET,
    filterenabledeq: str | Unset = UNSET,
    filterenablednot_eq: str | Unset = UNSET,
    filterenabledin: str | Unset = UNSET,
    filterenablednot_in: str | Unset = UNSET,
) -> Response[CustomFieldList]:
    """[DEPRECATED] List Custom Fields

     [DEPRECATED] Use form field endpoints instead. List Custom fields

    Args:
        include (ListCustomFieldsInclude | Unset):
        sort (ListCustomFieldsSort | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filterslug (str | Unset):
        filterlabel (str | Unset):
        filterkind (str | Unset):
        filterenabled (bool | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        filterslugeq (str | Unset):
        filterslugnot_eq (str | Unset):
        filterslugin (str | Unset):
        filterslugnot_in (str | Unset):
        filterlabeleq (str | Unset):
        filterlabelnot_eq (str | Unset):
        filterlabelin (str | Unset):
        filterlabelnot_in (str | Unset):
        filterkindeq (str | Unset):
        filterkindnot_eq (str | Unset):
        filterkindin (str | Unset):
        filterkindnot_in (str | Unset):
        filterenabledeq (str | Unset):
        filterenablednot_eq (str | Unset):
        filterenabledin (str | Unset):
        filterenablednot_in (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomFieldList]
    """

    kwargs = _get_kwargs(
        include=include,
        sort=sort,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filterslug=filterslug,
        filterlabel=filterlabel,
        filterkind=filterkind,
        filterenabled=filterenabled,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        filterslugeq=filterslugeq,
        filterslugnot_eq=filterslugnot_eq,
        filterslugin=filterslugin,
        filterslugnot_in=filterslugnot_in,
        filterlabeleq=filterlabeleq,
        filterlabelnot_eq=filterlabelnot_eq,
        filterlabelin=filterlabelin,
        filterlabelnot_in=filterlabelnot_in,
        filterkindeq=filterkindeq,
        filterkindnot_eq=filterkindnot_eq,
        filterkindin=filterkindin,
        filterkindnot_in=filterkindnot_in,
        filterenabledeq=filterenabledeq,
        filterenablednot_eq=filterenablednot_eq,
        filterenabledin=filterenabledin,
        filterenablednot_in=filterenablednot_in,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    include: ListCustomFieldsInclude | Unset = UNSET,
    sort: ListCustomFieldsSort | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filterslug: str | Unset = UNSET,
    filterlabel: str | Unset = UNSET,
    filterkind: str | Unset = UNSET,
    filterenabled: bool | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filterslugeq: str | Unset = UNSET,
    filterslugnot_eq: str | Unset = UNSET,
    filterslugin: str | Unset = UNSET,
    filterslugnot_in: str | Unset = UNSET,
    filterlabeleq: str | Unset = UNSET,
    filterlabelnot_eq: str | Unset = UNSET,
    filterlabelin: str | Unset = UNSET,
    filterlabelnot_in: str | Unset = UNSET,
    filterkindeq: str | Unset = UNSET,
    filterkindnot_eq: str | Unset = UNSET,
    filterkindin: str | Unset = UNSET,
    filterkindnot_in: str | Unset = UNSET,
    filterenabledeq: str | Unset = UNSET,
    filterenablednot_eq: str | Unset = UNSET,
    filterenabledin: str | Unset = UNSET,
    filterenablednot_in: str | Unset = UNSET,
) -> CustomFieldList | None:
    """[DEPRECATED] List Custom Fields

     [DEPRECATED] Use form field endpoints instead. List Custom fields

    Args:
        include (ListCustomFieldsInclude | Unset):
        sort (ListCustomFieldsSort | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filterslug (str | Unset):
        filterlabel (str | Unset):
        filterkind (str | Unset):
        filterenabled (bool | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        filterslugeq (str | Unset):
        filterslugnot_eq (str | Unset):
        filterslugin (str | Unset):
        filterslugnot_in (str | Unset):
        filterlabeleq (str | Unset):
        filterlabelnot_eq (str | Unset):
        filterlabelin (str | Unset):
        filterlabelnot_in (str | Unset):
        filterkindeq (str | Unset):
        filterkindnot_eq (str | Unset):
        filterkindin (str | Unset):
        filterkindnot_in (str | Unset):
        filterenabledeq (str | Unset):
        filterenablednot_eq (str | Unset):
        filterenabledin (str | Unset):
        filterenablednot_in (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomFieldList
    """

    return sync_detailed(
        client=client,
        include=include,
        sort=sort,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filterslug=filterslug,
        filterlabel=filterlabel,
        filterkind=filterkind,
        filterenabled=filterenabled,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        filterslugeq=filterslugeq,
        filterslugnot_eq=filterslugnot_eq,
        filterslugin=filterslugin,
        filterslugnot_in=filterslugnot_in,
        filterlabeleq=filterlabeleq,
        filterlabelnot_eq=filterlabelnot_eq,
        filterlabelin=filterlabelin,
        filterlabelnot_in=filterlabelnot_in,
        filterkindeq=filterkindeq,
        filterkindnot_eq=filterkindnot_eq,
        filterkindin=filterkindin,
        filterkindnot_in=filterkindnot_in,
        filterenabledeq=filterenabledeq,
        filterenablednot_eq=filterenablednot_eq,
        filterenabledin=filterenabledin,
        filterenablednot_in=filterenablednot_in,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    include: ListCustomFieldsInclude | Unset = UNSET,
    sort: ListCustomFieldsSort | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filterslug: str | Unset = UNSET,
    filterlabel: str | Unset = UNSET,
    filterkind: str | Unset = UNSET,
    filterenabled: bool | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filterslugeq: str | Unset = UNSET,
    filterslugnot_eq: str | Unset = UNSET,
    filterslugin: str | Unset = UNSET,
    filterslugnot_in: str | Unset = UNSET,
    filterlabeleq: str | Unset = UNSET,
    filterlabelnot_eq: str | Unset = UNSET,
    filterlabelin: str | Unset = UNSET,
    filterlabelnot_in: str | Unset = UNSET,
    filterkindeq: str | Unset = UNSET,
    filterkindnot_eq: str | Unset = UNSET,
    filterkindin: str | Unset = UNSET,
    filterkindnot_in: str | Unset = UNSET,
    filterenabledeq: str | Unset = UNSET,
    filterenablednot_eq: str | Unset = UNSET,
    filterenabledin: str | Unset = UNSET,
    filterenablednot_in: str | Unset = UNSET,
) -> Response[CustomFieldList]:
    """[DEPRECATED] List Custom Fields

     [DEPRECATED] Use form field endpoints instead. List Custom fields

    Args:
        include (ListCustomFieldsInclude | Unset):
        sort (ListCustomFieldsSort | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filterslug (str | Unset):
        filterlabel (str | Unset):
        filterkind (str | Unset):
        filterenabled (bool | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        filterslugeq (str | Unset):
        filterslugnot_eq (str | Unset):
        filterslugin (str | Unset):
        filterslugnot_in (str | Unset):
        filterlabeleq (str | Unset):
        filterlabelnot_eq (str | Unset):
        filterlabelin (str | Unset):
        filterlabelnot_in (str | Unset):
        filterkindeq (str | Unset):
        filterkindnot_eq (str | Unset):
        filterkindin (str | Unset):
        filterkindnot_in (str | Unset):
        filterenabledeq (str | Unset):
        filterenablednot_eq (str | Unset):
        filterenabledin (str | Unset):
        filterenablednot_in (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomFieldList]
    """

    kwargs = _get_kwargs(
        include=include,
        sort=sort,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filterslug=filterslug,
        filterlabel=filterlabel,
        filterkind=filterkind,
        filterenabled=filterenabled,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        filterslugeq=filterslugeq,
        filterslugnot_eq=filterslugnot_eq,
        filterslugin=filterslugin,
        filterslugnot_in=filterslugnot_in,
        filterlabeleq=filterlabeleq,
        filterlabelnot_eq=filterlabelnot_eq,
        filterlabelin=filterlabelin,
        filterlabelnot_in=filterlabelnot_in,
        filterkindeq=filterkindeq,
        filterkindnot_eq=filterkindnot_eq,
        filterkindin=filterkindin,
        filterkindnot_in=filterkindnot_in,
        filterenabledeq=filterenabledeq,
        filterenablednot_eq=filterenablednot_eq,
        filterenabledin=filterenabledin,
        filterenablednot_in=filterenablednot_in,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    include: ListCustomFieldsInclude | Unset = UNSET,
    sort: ListCustomFieldsSort | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filterslug: str | Unset = UNSET,
    filterlabel: str | Unset = UNSET,
    filterkind: str | Unset = UNSET,
    filterenabled: bool | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filterslugeq: str | Unset = UNSET,
    filterslugnot_eq: str | Unset = UNSET,
    filterslugin: str | Unset = UNSET,
    filterslugnot_in: str | Unset = UNSET,
    filterlabeleq: str | Unset = UNSET,
    filterlabelnot_eq: str | Unset = UNSET,
    filterlabelin: str | Unset = UNSET,
    filterlabelnot_in: str | Unset = UNSET,
    filterkindeq: str | Unset = UNSET,
    filterkindnot_eq: str | Unset = UNSET,
    filterkindin: str | Unset = UNSET,
    filterkindnot_in: str | Unset = UNSET,
    filterenabledeq: str | Unset = UNSET,
    filterenablednot_eq: str | Unset = UNSET,
    filterenabledin: str | Unset = UNSET,
    filterenablednot_in: str | Unset = UNSET,
) -> CustomFieldList | None:
    """[DEPRECATED] List Custom Fields

     [DEPRECATED] Use form field endpoints instead. List Custom fields

    Args:
        include (ListCustomFieldsInclude | Unset):
        sort (ListCustomFieldsSort | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filterslug (str | Unset):
        filterlabel (str | Unset):
        filterkind (str | Unset):
        filterenabled (bool | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        filterslugeq (str | Unset):
        filterslugnot_eq (str | Unset):
        filterslugin (str | Unset):
        filterslugnot_in (str | Unset):
        filterlabeleq (str | Unset):
        filterlabelnot_eq (str | Unset):
        filterlabelin (str | Unset):
        filterlabelnot_in (str | Unset):
        filterkindeq (str | Unset):
        filterkindnot_eq (str | Unset):
        filterkindin (str | Unset):
        filterkindnot_in (str | Unset):
        filterenabledeq (str | Unset):
        filterenablednot_eq (str | Unset):
        filterenabledin (str | Unset):
        filterenablednot_in (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomFieldList
    """

    return (
        await asyncio_detailed(
            client=client,
            include=include,
            sort=sort,
            pagenumber=pagenumber,
            pagesize=pagesize,
            filterslug=filterslug,
            filterlabel=filterlabel,
            filterkind=filterkind,
            filterenabled=filterenabled,
            filtercreated_atgt=filtercreated_atgt,
            filtercreated_atgte=filtercreated_atgte,
            filtercreated_atlt=filtercreated_atlt,
            filtercreated_atlte=filtercreated_atlte,
            filterslugeq=filterslugeq,
            filterslugnot_eq=filterslugnot_eq,
            filterslugin=filterslugin,
            filterslugnot_in=filterslugnot_in,
            filterlabeleq=filterlabeleq,
            filterlabelnot_eq=filterlabelnot_eq,
            filterlabelin=filterlabelin,
            filterlabelnot_in=filterlabelnot_in,
            filterkindeq=filterkindeq,
            filterkindnot_eq=filterkindnot_eq,
            filterkindin=filterkindin,
            filterkindnot_in=filterkindnot_in,
            filterenabledeq=filterenabledeq,
            filterenablednot_eq=filterenablednot_eq,
            filterenabledin=filterenabledin,
            filterenablednot_in=filterenablednot_in,
        )
    ).parsed
