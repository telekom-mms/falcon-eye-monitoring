FROM mcr.microsoft.com/playwright:v1.53.0

ENV HEADLESS=true

ENV USER=playwright
ENV VIRTUAL_ENV=/home/$USER/venv

RUN adduser $USER --gecos $USER --disabled-password

USER $USER

COPY --chown=$USER pyproject.toml /
COPY --chown=$USER uv.lock /

RUN curl -LsSf https://astral.sh/uv/install.sh | sh

RUN /home/$USER/.local/bin/uv sync --active --locked
RUN /home/$USER/.local/bin/uv run --active playwright  install

COPY --chown=root:root pytest.ini /tests/
COPY --chown=root:root src/__init__.py /tests/src/
COPY --chown=root:root src/pages/ /tests/src/pages/
COPY --chown=root:root src/test/ /tests/src/test/
COPY --chown=root:root src/tests.sh /tests/

WORKDIR /tests/

CMD ["bash", "./tests.sh"]
