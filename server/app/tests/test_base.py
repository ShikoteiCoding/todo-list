"""
Test base routes.
"""

from flask import Flask


def test_empty_url(app: Flask):
    client = app.test_client()
    resp = client.get("/")

    assert resp.status_code == 404
