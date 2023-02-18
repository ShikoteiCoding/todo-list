"""
Test ping route
"""
import json

from flask import Flask


def test_ping_200(app: Flask):
    """UserList.GET"""

    client = app.test_client()
    response = client.get("/api/v1/ping")
    data = json.loads(response.data.decode())

    assert response.status_code == 200
    assert response.content_type == "application/json"
    assert "ping" in data["message"]
