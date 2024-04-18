FROM mcr.microsoft.com/playwright:v1.40.0-jammy

ENV HEADLESS=true

RUN apt-get update && apt-get install --yes python3-pip
RUN pip install pytest playwright pytest-playwright faker
RUN playwright install

COPY --chown=root:root pytest.ini /tests/
COPY --chown=root:root src/__init__.py /tests/src/
COPY --chown=root:root src/pages/ /tests/src/pages/
COPY --chown=root:root src/test/ /tests/src/test/

WORKDIR /tests/

CMD pytest --verbose src/test/test_demoapp.py src/test/test_grafana.py
