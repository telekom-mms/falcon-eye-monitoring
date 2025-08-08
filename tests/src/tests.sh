#!/usr/bin/bash
poetry run pytest --verbose /tests/src/test/test_demoapp.py

echo "waiting 60 seconds to give some time to metrics shipping and calculation" && sleep 60

poetry run pytest --verbose /tests/src/test/test_grafana_demoapp.py
poetry run pytest --verbose /tests/src/test/test_grafana_shellexporter.py