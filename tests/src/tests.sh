#!/usr/bin/bash
uv run pytest --verbose /tests/src/test/test_demoapp.py
rc=$?
if [ "$rc" -gt 0 ]; then exit 1; fi

echo "!!! Notice: waiting for metrics, logs and traces up to 60 seconds being shipped and calculated"

uv run pytest --verbose /tests/src/test/test_grafana_demoapp.py
rc=$?
if [ "$rc" -gt 0 ]; then exit 1; fi

uv run pytest --verbose /tests/src/test/test_grafana_shellexporter.py
rc=$?
if [ "$rc" -gt 0 ]; then exit 1; fi
