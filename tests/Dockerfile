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

COPY --chown=$USER pytest.ini /tests/
COPY --chown=$USER src/__init__.py /tests/src/
COPY --chown=$USER src/pages/ /tests/src/pages/
COPY --chown=$USER src/test/ /tests/src/test/

WORKDIR /tests/

CMD /home/$USER/.local/bin/uv run --active pytest --verbose src/test/test_demoapp.py src/test/test_grafana.py
