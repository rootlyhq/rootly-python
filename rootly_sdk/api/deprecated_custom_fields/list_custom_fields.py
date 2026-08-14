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
    include: Unset | ListCustomFieldsInclude = UNSET,
    sort: Unset | ListCustomFieldsSort = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filterslug: Unset | str = UNSET,
    filterlabel: Unset | str = UNSET,
    filterkind: Unset | str = UNSET,
    filterenabled: Unset | bool = UNSET,
    filtercreated_atgt: Unset | str = UNSET,
    filtercreated_atgte: Unset | str = UNSET,
    filtercreated_atlt: Unset | str = UNSET,
    filtercreated_atlte: Unset | str = UNSET,
    filterslugeq: Unset | str = UNSET,
    filterslugnot_eq: Unset | str = UNSET,
    filterslugin: Unset | str = UNSET,
    filterslugnot_in: Unset | str = UNSET,
    filterlabeleq: Unset | str = UNSET,
    filterlabelnot_eq: Unset | str = UNSET,
    filterlabelin: Unset | str = UNSET,
    filterlabelnot_in: Unset | str = UNSET,
    filterkindeq: Unset | str = UNSET,
    filterkindnot_eq: Unset | str = UNSET,
    filterkindin: Unset | str = UNSET,
    filterkindnot_in: Unset | str = UNSET,
    filterenabledeq: Unset | str = UNSET,
    filterenablednot_eq: Unset | str = UNSET,
    filterenabledin: Unset | str = UNSET,
    filterenablednot_in: Unset | str = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_include: Unset | str = UNSET
    if not isinstance(include, Unset):
        json_include = include

    params["include"] = json_include

    json_sort: Unset | str = UNSET
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
    include: Unset | ListCustomFieldsInclude = UNSET,
    sort: Unset | ListCustomFieldsSort = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filterslug: Unset | str = UNSET,
    filterlabel: Unset | str = UNSET,
    filterkind: Unset | str = UNSET,
    filterenabled: Unset | bool = UNSET,
    filtercreated_atgt: Unset | str = UNSET,
    filtercreated_atgte: Unset | str = UNSET,
    filtercreated_atlt: Unset | str = UNSET,
    filtercreated_atlte: Unset | str = UNSET,
    filterslugeq: Unset | str = UNSET,
    filterslugnot_eq: Unset | str = UNSET,
    filterslugin: Unset | str = UNSET,
    filterslugnot_in: Unset | str = UNSET,
    filterlabeleq: Unset | str = UNSET,
    filterlabelnot_eq: Unset | str = UNSET,
    filterlabelin: Unset | str = UNSET,
    filterlabelnot_in: Unset | str = UNSET,
    filterkindeq: Unset | str = UNSET,
    filterkindnot_eq: Unset | str = UNSET,
    filterkindin: Unset | str = UNSET,
    filterkindnot_in: Unset | str = UNSET,
    filterenabledeq: Unset | str = UNSET,
    filterenablednot_eq: Unset | str = UNSET,
    filterenabledin: Unset | str = UNSET,
    filterenablednot_in: Unset | str = UNSET,
) -> Response[CustomFieldList]:
    """[DEPRECATED] List Custom Fields

     [DEPRECATED] Use form field endpoints instead. List Custom fields

    Args:
        include (Union[Unset, ListCustomFieldsInclude]):
        sort (Union[Unset, ListCustomFieldsSort]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filterslug (Union[Unset, str]):
        filterlabel (Union[Unset, str]):
        filterkind (Union[Unset, str]):
        filterenabled (Union[Unset, bool]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        filterslugeq (Union[Unset, str]):
        filterslugnot_eq (Union[Unset, str]):
        filterslugin (Union[Unset, str]):
        filterslugnot_in (Union[Unset, str]):
        filterlabeleq (Union[Unset, str]):
        filterlabelnot_eq (Union[Unset, str]):
        filterlabelin (Union[Unset, str]):
        filterlabelnot_in (Union[Unset, str]):
        filterkindeq (Union[Unset, str]):
        filterkindnot_eq (Union[Unset, str]):
        filterkindin (Union[Unset, str]):
        filterkindnot_in (Union[Unset, str]):
        filterenabledeq (Union[Unset, str]):
        filterenablednot_eq (Union[Unset, str]):
        filterenabledin (Union[Unset, str]):
        filterenablednot_in (Union[Unset, str]):

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
    include: Unset | ListCustomFieldsInclude = UNSET,
    sort: Unset | ListCustomFieldsSort = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filterslug: Unset | str = UNSET,
    filterlabel: Unset | str = UNSET,
    filterkind: Unset | str = UNSET,
    filterenabled: Unset | bool = UNSET,
    filtercreated_atgt: Unset | str = UNSET,
    filtercreated_atgte: Unset | str = UNSET,
    filtercreated_atlt: Unset | str = UNSET,
    filtercreated_atlte: Unset | str = UNSET,
    filterslugeq: Unset | str = UNSET,
    filterslugnot_eq: Unset | str = UNSET,
    filterslugin: Unset | str = UNSET,
    filterslugnot_in: Unset | str = UNSET,
    filterlabeleq: Unset | str = UNSET,
    filterlabelnot_eq: Unset | str = UNSET,
    filterlabelin: Unset | str = UNSET,
    filterlabelnot_in: Unset | str = UNSET,
    filterkindeq: Unset | str = UNSET,
    filterkindnot_eq: Unset | str = UNSET,
    filterkindin: Unset | str = UNSET,
    filterkindnot_in: Unset | str = UNSET,
    filterenabledeq: Unset | str = UNSET,
    filterenablednot_eq: Unset | str = UNSET,
    filterenabledin: Unset | str = UNSET,
    filterenablednot_in: Unset | str = UNSET,
) -> CustomFieldList | None:
    """[DEPRECATED] List Custom Fields

     [DEPRECATED] Use form field endpoints instead. List Custom fields

    Args:
        include (Union[Unset, ListCustomFieldsInclude]):
        sort (Union[Unset, ListCustomFieldsSort]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filterslug (Union[Unset, str]):
        filterlabel (Union[Unset, str]):
        filterkind (Union[Unset, str]):
        filterenabled (Union[Unset, bool]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        filterslugeq (Union[Unset, str]):
        filterslugnot_eq (Union[Unset, str]):
        filterslugin (Union[Unset, str]):
        filterslugnot_in (Union[Unset, str]):
        filterlabeleq (Union[Unset, str]):
        filterlabelnot_eq (Union[Unset, str]):
        filterlabelin (Union[Unset, str]):
        filterlabelnot_in (Union[Unset, str]):
        filterkindeq (Union[Unset, str]):
        filterkindnot_eq (Union[Unset, str]):
        filterkindin (Union[Unset, str]):
        filterkindnot_in (Union[Unset, str]):
        filterenabledeq (Union[Unset, str]):
        filterenablednot_eq (Union[Unset, str]):
        filterenabledin (Union[Unset, str]):
        filterenablednot_in (Union[Unset, str]):

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
    include: Unset | ListCustomFieldsInclude = UNSET,
    sort: Unset | ListCustomFieldsSort = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filterslug: Unset | str = UNSET,
    filterlabel: Unset | str = UNSET,
    filterkind: Unset | str = UNSET,
    filterenabled: Unset | bool = UNSET,
    filtercreated_atgt: Unset | str = UNSET,
    filtercreated_atgte: Unset | str = UNSET,
    filtercreated_atlt: Unset | str = UNSET,
    filtercreated_atlte: Unset | str = UNSET,
    filterslugeq: Unset | str = UNSET,
    filterslugnot_eq: Unset | str = UNSET,
    filterslugin: Unset | str = UNSET,
    filterslugnot_in: Unset | str = UNSET,
    filterlabeleq: Unset | str = UNSET,
    filterlabelnot_eq: Unset | str = UNSET,
    filterlabelin: Unset | str = UNSET,
    filterlabelnot_in: Unset | str = UNSET,
    filterkindeq: Unset | str = UNSET,
    filterkindnot_eq: Unset | str = UNSET,
    filterkindin: Unset | str = UNSET,
    filterkindnot_in: Unset | str = UNSET,
    filterenabledeq: Unset | str = UNSET,
    filterenablednot_eq: Unset | str = UNSET,
    filterenabledin: Unset | str = UNSET,
    filterenablednot_in: Unset | str = UNSET,
) -> Response[CustomFieldList]:
    """[DEPRECATED] List Custom Fields

     [DEPRECATED] Use form field endpoints instead. List Custom fields

    Args:
        include (Union[Unset, ListCustomFieldsInclude]):
        sort (Union[Unset, ListCustomFieldsSort]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filterslug (Union[Unset, str]):
        filterlabel (Union[Unset, str]):
        filterkind (Union[Unset, str]):
        filterenabled (Union[Unset, bool]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        filterslugeq (Union[Unset, str]):
        filterslugnot_eq (Union[Unset, str]):
        filterslugin (Union[Unset, str]):
        filterslugnot_in (Union[Unset, str]):
        filterlabeleq (Union[Unset, str]):
        filterlabelnot_eq (Union[Unset, str]):
        filterlabelin (Union[Unset, str]):
        filterlabelnot_in (Union[Unset, str]):
        filterkindeq (Union[Unset, str]):
        filterkindnot_eq (Union[Unset, str]):
        filterkindin (Union[Unset, str]):
        filterkindnot_in (Union[Unset, str]):
        filterenabledeq (Union[Unset, str]):
        filterenablednot_eq (Union[Unset, str]):
        filterenabledin (Union[Unset, str]):
        filterenablednot_in (Union[Unset, str]):

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
    include: Unset | ListCustomFieldsInclude = UNSET,
    sort: Unset | ListCustomFieldsSort = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filterslug: Unset | str = UNSET,
    filterlabel: Unset | str = UNSET,
    filterkind: Unset | str = UNSET,
    filterenabled: Unset | bool = UNSET,
    filtercreated_atgt: Unset | str = UNSET,
    filtercreated_atgte: Unset | str = UNSET,
    filtercreated_atlt: Unset | str = UNSET,
    filtercreated_atlte: Unset | str = UNSET,
    filterslugeq: Unset | str = UNSET,
    filterslugnot_eq: Unset | str = UNSET,
    filterslugin: Unset | str = UNSET,
    filterslugnot_in: Unset | str = UNSET,
    filterlabeleq: Unset | str = UNSET,
    filterlabelnot_eq: Unset | str = UNSET,
    filterlabelin: Unset | str = UNSET,
    filterlabelnot_in: Unset | str = UNSET,
    filterkindeq: Unset | str = UNSET,
    filterkindnot_eq: Unset | str = UNSET,
    filterkindin: Unset | str = UNSET,
    filterkindnot_in: Unset | str = UNSET,
    filterenabledeq: Unset | str = UNSET,
    filterenablednot_eq: Unset | str = UNSET,
    filterenabledin: Unset | str = UNSET,
    filterenablednot_in: Unset | str = UNSET,
) -> CustomFieldList | None:
    """[DEPRECATED] List Custom Fields

     [DEPRECATED] Use form field endpoints instead. List Custom fields

    Args:
        include (Union[Unset, ListCustomFieldsInclude]):
        sort (Union[Unset, ListCustomFieldsSort]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filterslug (Union[Unset, str]):
        filterlabel (Union[Unset, str]):
        filterkind (Union[Unset, str]):
        filterenabled (Union[Unset, bool]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        filterslugeq (Union[Unset, str]):
        filterslugnot_eq (Union[Unset, str]):
        filterslugin (Union[Unset, str]):
        filterslugnot_in (Union[Unset, str]):
        filterlabeleq (Union[Unset, str]):
        filterlabelnot_eq (Union[Unset, str]):
        filterlabelin (Union[Unset, str]):
        filterlabelnot_in (Union[Unset, str]):
        filterkindeq (Union[Unset, str]):
        filterkindnot_eq (Union[Unset, str]):
        filterkindin (Union[Unset, str]):
        filterkindnot_in (Union[Unset, str]):
        filterenabledeq (Union[Unset, str]):
        filterenablednot_eq (Union[Unset, str]):
        filterenabledin (Union[Unset, str]):
        filterenablednot_in (Union[Unset, str]):

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
