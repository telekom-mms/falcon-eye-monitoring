from playwright.sync_api import Page

def login(page: Page, username: str, password: str):
    """## Login to grafana

    ### Args:
        - `page (Page)`: The current page
        - `username (str)`: The username
        - `password (str)`: The password
    """
    if page.get_by_test_id("data-testid Username input field").is_visible():
        page.get_by_test_id("data-testid Username input field").fill(username)
        page.get_by_test_id("data-testid Password input field").fill(password)
        page.get_by_test_id("data-testid Login button").click()
        page.get_by_test_id("data-testid Skip change password button").click()


def open_dashboards(page: Page):
    """## _summary_

    ### Args:
        - `page (Page)`: The current page
    """
    page.get_by_test_id("data-testid Toggle menu").click()
    page.get_by_test_id("data-testid navigation mega-menu").get_by_role("link", name="Dashboards").click()
    page.get_by_label("Expand folder Services").click()


def open_dashboard(page: Page, name: str):
    """## Open dashboard with given name

    ### Args:
        - `page (Page)`: The current page
        - `name (str)`: The name of the dashboard to open
    """
    open_dashboards(page)
    page.get_by_role("link", name=name).click()
