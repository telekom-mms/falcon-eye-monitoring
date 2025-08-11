#!/usr/bin/bash
poetry run pytest --verbose /tests/src/test/test_demoapp.py
echo "'$? :' $?" 

echo "waiting 60 seconds to give some time to metrics shipping and calculation" && sleep 60

poetry run pytest --verbose /tests/src/test/test_grafana_demoapp.py
echo "'$? :' $?" 

poetry run pytest --verbose /tests/src/test/test_grafana_shellexporter.py
echo "'$? :' $?" 
