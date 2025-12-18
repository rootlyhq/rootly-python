# rootly
A client library for accessing Rootly API v1

## Installation

```bash
pip install rootly
```

## Quick Start

```python
from rootly_sdk import AuthenticatedClient

client = AuthenticatedClient(
    base_url="https://api.rootly.com",
    token="YOUR_API_TOKEN"
)
```

Get your API token from **Settings > API Keys** in your [Rootly Dashboard](https://rootly.com/account/api_keys).

## Examples

### List Incidents

```python
from rootly_sdk import AuthenticatedClient
from rootly_sdk.api.incidents import list_incidents

client = AuthenticatedClient(base_url="https://api.rootly.com", token="YOUR_API_TOKEN")

with client as client:
    response = list_incidents.sync(client=client)
    for incident in response.data:
        print(f"{incident.attributes.title} - {incident.attributes.status}")
```

### Create an Incident

```python
from rootly_sdk import AuthenticatedClient
from rootly_sdk.api.incidents import create_incident
from rootly_sdk.models import NewIncident, NewIncidentData, NewIncidentDataAttributes

client = AuthenticatedClient(base_url="https://api.rootly.com", token="YOUR_API_TOKEN")

with client as client:
    incident = create_incident.sync(
        client=client,
        body=NewIncident(
            data=NewIncidentData(
                type="incidents",
                attributes=NewIncidentDataAttributes(
                    title="Database connection issues",
                    summary="Users experiencing slow queries and timeouts",
                )
            )
        )
    )
    print(f"Created incident: {incident.data.id}")
```

### List Services

```python
from rootly_sdk import AuthenticatedClient
from rootly_sdk.api.services import list_services

client = AuthenticatedClient(base_url="https://api.rootly.com", token="YOUR_API_TOKEN")

with client as client:
    response = list_services.sync(client=client)
    for service in response.data:
        print(f"{service.attributes.name} - {service.attributes.slug}")
```

### List On-Call Schedules

```python
from rootly_sdk import AuthenticatedClient
from rootly_sdk.api.schedules import list_schedules

client = AuthenticatedClient(base_url="https://api.rootly.com", token="YOUR_API_TOKEN")

with client as client:
    response = list_schedules.sync(client=client)
    for schedule in response.data:
        print(f"{schedule.attributes.name}")
```

### Async Usage

```python
import asyncio
from rootly_sdk import AuthenticatedClient
from rootly_sdk.api.incidents import list_incidents

async def main():
    client = AuthenticatedClient(base_url="https://api.rootly.com", token="YOUR_API_TOKEN")

    async with client as client:
        response = await list_incidents.asyncio(client=client)
        for incident in response.data:
            print(f"{incident.attributes.title}")

asyncio.run(main())
```

### Get Detailed Response

```python
from rootly_sdk import AuthenticatedClient
from rootly_sdk.api.incidents import list_incidents
from rootly_sdk.types import Response

with client as client:
    response: Response = list_incidents.sync_detailed(client=client)
    print(f"Status: {response.status_code}")
    print(f"Headers: {response.headers}")
    if response.parsed:
        print(f"Incidents: {len(response.parsed.data)}")
```

## API Reference

Every endpoint becomes a Python module with four functions:

| Function | Description |
|----------|-------------|
| `sync` | Blocking request that returns parsed data (if successful) or `None` |
| `sync_detailed` | Blocking request that returns a `Response` with status code, headers, and parsed data |
| `asyncio` | Async version of `sync` |
| `asyncio_detailed` | Async version of `sync_detailed` |

All path/query params and request bodies become method arguments.

## Advanced Configuration

### Custom SSL Certificates

```python
client = AuthenticatedClient(
    base_url="https://api.rootly.com",
    token="YOUR_API_TOKEN",
    verify_ssl="/path/to/certificate_bundle.pem",
)
```

### Request/Response Logging

```python
from rootly_sdk import AuthenticatedClient

def log_request(request):
    print(f"Request: {request.method} {request.url}")

def log_response(response):
    print(f"Response: {response.status_code}")

client = AuthenticatedClient(
    base_url="https://api.rootly.com",
    token="YOUR_API_TOKEN",
    httpx_args={"event_hooks": {"request": [log_request], "response": [log_response]}},
)
```

### Custom httpx Client

```python
import httpx
from rootly_sdk import AuthenticatedClient

client = AuthenticatedClient(
    base_url="https://api.rootly.com",
    token="YOUR_API_TOKEN",
)
client.set_httpx_client(httpx.Client(base_url="https://api.rootly.com", proxies="http://localhost:8030"))
```

## Building / publishing this package
This project uses [Poetry](https://python-poetry.org/) to manage dependencies  and packaging.  Here are the basics:
1. Update the metadata in pyproject.toml (e.g. authors, version)
1. If you're using a private repository, configure it with Poetry
    1. `poetry config repositories.<your-repository-name> <url-to-your-repository>`
    1. `poetry config http-basic.<your-repository-name> <username> <password>`
1. Publish the client with `poetry publish --build -r <your-repository-name>` or, if for public PyPI, just `poetry publish --build`

If you want to install this client into another project without publishing it (e.g. for development) then:
1. If that project **is using Poetry**, you can simply do `poetry add <path-to-this-client>` from that project
1. If that project is not using Poetry:
    1. Build a wheel with `poetry build -f wheel`
    1. Install that wheel from the other project `pip install <path-to-wheel>`
