import os
import time

from flask import Flask, jsonify, request
from prometheus_client import Counter, Histogram, generate_latest
from prometheus_client.exposition import CONTENT_TYPE_LATEST

REQUEST_COUNT = Counter(
    "chromatography_requests_total",
    "Total HTTP requests received",
    ["method", "endpoint", "status"],
)

REQUEST_DURATION = Histogram(
    "chromatography_request_duration_seconds",
    "HTTP request duration",
    ["endpoint"],
)


def create_app() -> Flask:
    app = Flask(__name__)

    @app.before_request
    def start_timer() -> None:
        request.start_time = time.perf_counter()

    @app.after_request
    def record_metrics(response):
        endpoint = request.endpoint or "unknown"
        duration = time.perf_counter() - request.start_time

        REQUEST_DURATION.labels(endpoint=endpoint).observe(duration)

        REQUEST_COUNT.labels(
            method=request.method,
            endpoint=endpoint,
            status=str(response.status_code),
        ).inc()

        return response

    @app.get("/")
    def home():
        return jsonify(
            {
                "application": "Chromatography Insights",
                "description": "Educational liquid chromatography platform",
                "environment": os.getenv("APP_ENV", "development"),
                "version": "0.1.0",
            }
        )

    @app.get("/health")
    def health():
        return jsonify({"status": "healthy"}), 200

    @app.get("/ready")
    def ready():
        return jsonify({"status": "ready"}), 200

    @app.get("/methods")
    def methods():
        return jsonify(
            {
                "methods": [
                    {
                        "name": "Reverse Phase HPLC",
                        "purpose": "Separate compounds by hydrophobic interaction",
                    },
                    {
                        "name": "Ion Exchange Chromatography",
                        "purpose": "Separate molecules by electrical charge",
                    },
                    {
                        "name": "Size Exclusion Chromatography",
                        "purpose": "Separate molecules by molecular size",
                    },
                ]
            }
        )

    @app.get("/metrics")
    def metrics():
        return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

    @app.errorhandler(404)
    def not_found(_error):
        return jsonify({"error": "Resource not found"}), 404

    return app


if __name__ == "__main__":
    application = create_app()

    application.run(
        host="0.0.0.0",
        port=int(os.getenv("APP_PORT", "5000")),
        debug=False,
    )