FROM mcr.microsoft.com/playwright:v1.46.0-jammy

ENV HEADLESS=true

COPY --chown=root:root pyproject.toml /
COPY --chown=root:root poetry.lock /

RUN apt-get update && apt-get install --yes python3-poetry
RUN poetry config virtualenvs.create false
RUN poetry install
RUN poetry run playwright install

COPY --chown=root:root pytest.ini /tests/
COPY --chown=root:root src/__init__.py /tests/src/
COPY --chown=root:root src/pages/ /tests/src/pages/
COPY --chown=root:root src/test/ /tests/src/test/
COPY --chown=root:root src/tests.sh /tests/

WORKDIR /tests/

CMD ["bash", "./tests.sh"]
