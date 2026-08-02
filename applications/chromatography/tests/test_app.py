import sys
from pathlib import Path

APPLICATION_DIRECTORY = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APPLICATION_DIRECTORY))

from app import create_app


def test_home_endpoint():
    app = create_app()
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.get_json()["application"] == "Chromatography Insights"


def test_health_endpoint():
    app = create_app()
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}


def test_ready_endpoint():
    app = create_app()
    client = app.test_client()

    response = client.get("/ready")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ready"}


def test_methods_endpoint():
    app = create_app()
    client = app.test_client()

    response = client.get("/methods")

    assert response.status_code == 200
    assert len(response.get_json()["methods"]) == 3


def test_metrics_endpoint():
    app = create_app()
    client = app.test_client()

    client.get("/health")
    response = client.get("/metrics")

    assert response.status_code == 200
    assert b"chromatography_requests_total" in response.data


def test_unknown_route_returns_json_404():
    app = create_app()
    client = app.test_client()

    response = client.get("/does-not-exist")

    assert response.status_code == 404
    assert response.get_json() == {"error": "Resource not found"}