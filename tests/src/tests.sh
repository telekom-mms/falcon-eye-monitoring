#!/usr/bin/bash
poetry run pytest --verbose /tests/src/test/test_demoapp.py
if [ "$rc" -gt 0 ]; then exit 1; fi

echo "waiting 60 seconds to give some time to metrics shipping and calculation" && sleep 60

poetry run pytest --verbose /tests/src/test/test_grafana_demoapp.py
if [ "$rc" -gt 0 ]; then exit 1; fi

poetry run pytest --verbose /tests/src/test/test_grafana_shellexporter.py
if [ "$rc" -gt 0 ]; then exit 1; fi
