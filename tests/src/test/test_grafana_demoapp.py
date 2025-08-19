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
def test_dashboard_exists(playwright: Playwright) -> None:
    page = subject.setup(playwright)

    grafana.open_dashboards(page)

    locator = page.get_by_role("link", name="demoapp")
    locator.wait_for(timeout=60000, state="visible")

    expect(locator).to_be_visible()


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
def test_panel_data_trace_duration_graph(playwright: Playwright) -> None:
    page = subject.setup(playwright)

    grafana.open_dashboard(page, "demoapp")

    locator = page.get_by_test_id("data-testid VizLegend series Duration").get_by_role("button", name="Duration")
    locator.wait_for(timeout=60000, state="visible")

    expect(locator).to_be_visible()


@pytest.mark.base
def test_panel_data_trace_duration_list(playwright: Playwright) -> None:
    page = subject.setup(playwright)

    grafana.open_dashboard(page, "demoapp")

    page.get_by_test_id("data-testid Panel header trace duration descending").get_by_test_id("header-container").click()
    page.get_by_test_id("data-testid Panel menu trace duration descending").click()
    page.get_by_test_id("data-testid Panel menu item View").click()

    path_list = [
        "demoapp: GET /owners",
        "demoapp: GET /vets.html",
        "demoapp: GET /oups"
        ]

    for p in path_list:
        locator = page.get_by_text(p).first
        locator.wait_for(timeout=60000, state="visible")
        expect(locator).to_be_visible()


@pytest.mark.base
def test_panel_data_runtime_exception(playwright: Playwright) -> None:
    page = subject.setup(playwright)

    time.sleep(30)

    grafana.open_dashboard(page, "demoapp")

    expect(page.get_by_test_id("data-testid Panel header runtime exceptions")
           .get_by_role("button", name="RuntimeException").first).to_be_visible()

    locator = page.get_by_test_id("data-testid Panel header logfile - exceptions").locator("div").filter(has_text="exception").first
    locator.wait_for(timeout=60000, state="visible")

    expect(locator).to_be_visible()


@pytest.mark.base
def test_panel_data_http_status(playwright: Playwright) -> None:
    page = subject.setup(playwright)

    grafana.open_dashboard(page, "demoapp")

    page.get_by_test_id("data-testid Panel header trace duration").press("PageDown")

    locator = page.get_by_test_id("data-testid Panel header http status code").locator("div").filter(has_text="Name").first
    locator.wait_for(timeout=60000, state="visible")

    expect(locator).to_be_visible()


@pytest.mark.base
def test_panel_data_app_starts(playwright: Playwright) -> None:
    page = subject.setup(playwright)

    grafana.open_dashboard(page, "demoapp")

    page.get_by_test_id("data-testid Panel header trace duration").press("PageDown")

    locator = page.get_by_test_id("data-testid Panel header logfile - app start duration").get_by_role("button", name="container").first
    locator.wait_for(timeout=60000, state="visible")

    expect(locator).to_be_visible()
