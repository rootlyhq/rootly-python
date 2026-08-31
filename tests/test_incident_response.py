import unittest

from rootly_sdk.models.incident_response import IncidentResponse


class TestIncidentResponse(unittest.TestCase):
    def test_deserializes_and_serializes_null_severity(self) -> None:
        payload = {
            "data": {
                "id": "incident-id",
                "type": "incidents",
                "attributes": {
                    "title": "Scheduled maintenance",
                    "created_at": "2026-08-31T12:00:00Z",
                    "updated_at": "2026-08-31T12:00:00Z",
                    "severity": None,
                },
            }
        }

        response = IncidentResponse.from_dict(payload)

        self.assertIsNone(response.data.attributes.severity)
        self.assertIsNone(response.to_dict()["data"]["attributes"]["severity"])


if __name__ == "__main__":
    unittest.main()
