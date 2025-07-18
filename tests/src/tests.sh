#!/usr/bin/bash
poetry run pytest --verbose /tests/src/test/test_demoapp.py & sleep 60   # give some time to metrics shipping and calculation
poetry run pytest --verbose /tests/src/test/test_grafana_demoapp.py
poetry run pytest --verbose /tests/src/test/test_grafana_shellexporter.py