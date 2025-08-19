FROM mcr.microsoft.com/playwright:v1.53.0

ENV HEADLESS=true

ENV USER=playwright
ENV UV_HOME=/opt/uv

RUN adduser $USER --gecos $USER --disabled-password
RUN mkdir $UV_HOME && chown $USER $UV_HOME

COPY --chown=$USER pyproject.toml /
COPY --chown=$USER uv.lock /

RUN curl -LsSf https://astral.sh/uv/install.sh | env UV_INSTALL_DIR="$UV_HOME" sh

RUN $UV_HOME/uv sync --active --locked
RUN $UV_HOME/uv run --active playwright  install

USER $USER

COPY --chown=$USER pytest.ini /tests/
COPY --chown=$USER src/__init__.py /tests/src/
COPY --chown=$USER src/pages/ /tests/src/pages/
COPY --chown=$USER src/test/ /tests/src/test/
COPY --chown=$USER src/tests.sh /tests/

WORKDIR /tests/

CMD ["/bin/bash", "./tests.sh"]
