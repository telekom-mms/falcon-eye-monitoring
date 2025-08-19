import os
import time

import pytest
from playwright.sync_api import Page, Playwright, expect
from src.pages import grafana
from src.test.base import PreFlightCheck

now = time.time()


class Grafana(PreFlightCheck):

    def __init__(self):
        self.url = PreFlightCheck.get_config("GRAFANA_URL")
        self.user = PreFlightCheck.get_config("GRAFANA_USER")
        self.password = PreFlightCheck.get_config("GRAFANA_PASSWORD")
        self.browser = None

    def setup(self, playwright: Playwright) -> Page:
        """ Login if no context """
        if self.browser is None:
            self.browser = playwright.firefox.launch_persistent_context(
                user_data_dir=f"./test_grafana_{now}",
                headless=os.getenv("HEADLESS") in ("true", "True", "TRUE"))
        page = self.browser.pages[0]

        page.goto(self.url)

        grafana.login(page, self.user, self.password)

        return page


subject = Grafana()


@pytest.mark.base
def test_dashboards_exists(playwright: Playwright) -> None:
    page = subject.setup(playwright)

    grafana.open_dashboards(page)

    expect(page.get_by_role("link", name="shellexporter")).to_be_visible()


@pytest.mark.base
def test_dashboard_contains_panel(playwright: Playwright) -> None:
    page = subject.setup(playwright)

    grafana.open_dashboard(page, "shellexporter")

    panel = page.get_by_test_id(f"data-testid Panel header bash_gauge.sh").get_by_role("heading",
                                                                                       name="bash_gauge.sh")
    expect(panel).to_be_visible()


@pytest.mark.base
def test_panel(playwright: Playwright) -> None:
    page = subject.setup(playwright)

    grafana.open_dashboard(page, "shellexporter")

    for i in range(1, 9):
        locator = page.get_by_text(f"for_{i}", exact=True)
        locator.wait_for(timeout=60000, state="visible")
        expect(locator).to_be_visible()
