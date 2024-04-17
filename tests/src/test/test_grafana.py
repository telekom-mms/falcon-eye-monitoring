import unittest

import pytest
from playwright.sync_api import Page, Playwright, expect
import os
import time

from src.test.base import PreFlightCheck
from src.pages import grafana

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
                headless=os.getenv("HEADLESS") in ("true", "True", "yes"))
        page = self.browser.pages[0]

        page.goto(self.url)

        grafana.login(page, self.user, self.password)

        return page


subject = Grafana()


@pytest.mark.base
def test_dashboard_exists(playwright: Playwright) -> None:
    page = subject.setup(playwright)

    grafana.open_dashboards(page)

    expect(page.get_by_role("link", name="demoapp")).to_be_visible()


@pytest.mark.base
def test_dashboard_contains_panels(playwright: Playwright) -> None:
    page = subject.setup(playwright)

    grafana.open_dashboard(page, "demoapp")

    for panel_heading in ["trace duration",
                          "trace duration descending",
                          "runtime exceptions",
                          "logfile - exceptions"]:
        panel = page.get_by_test_id(f"data-testid Panel header {panel_heading}").get_by_role("heading",
                                                                                             name=panel_heading)

        expect(panel).to_be_visible()

    # scroll down
    page.mouse.wheel(0, 250)

    for panel_heading in ["http status code",
                          "logfile - app start duration"]:
        panel = page.get_by_test_id(f"data-testid Panel header {panel_heading}").get_by_role("heading",
                                                                                             name=panel_heading)

        expect(panel).to_be_visible()

@pytest.mark.base
def test_panel_data(playwright: Playwright) -> None:
    page = subject.setup(playwright)

    grafana.open_dashboard(page, "demoapp")

    expect(page.get_by_test_id("data-testid VizLegend series Duration")
           .get_by_role("button", name="Duration")).to_be_visible()

    expect(page.get_by_text("demoapp: GET /owners").first).to_be_visible()
    expect(page.get_by_text("demoapp: GET /vets.html").first).to_be_visible()
    expect(page.get_by_text("demoapp: GET /oups").first).to_be_visible()

    expect(page.get_by_test_id("data-testid Panel header runtime exceptions")
           .get_by_role("button", name="RuntimeException").first).to_be_visible()

    expect(page.get_by_test_id("data-testid Panel header logfile - exceptions")
           .locator("div").filter(has_text="exception").first).to_be_visible()

    # scroll down
    page.mouse.wheel(0, 250)

    expect(page.get_by_test_id("data-testid Panel header logfile - app start duration")
           .get_by_role("button", name="container").first).to_be_visible()

    expect(page.get_by_test_id("data-testid Panel header http status code")
           .locator("div").filter(has_text="Name200 302 400 500").first).to_be_visible()
