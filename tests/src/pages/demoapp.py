from playwright.sync_api import Page

def owners_index(page: Page):
    """## List owners index page

    ### Args:
        - `page (Page)`: The current page
    """
    page.get_by_role("link").filter(has_text="Find owners").click()


def search_owners(page: Page, name: str):
    """## Search owner by name

    ### Args:
        - `page (Page)`: The current page
        - `name (str)`: The name of the owner to find
    """
    page.locator("#lastName").fill(name)
    page.get_by_role("button", name="Find Owner").click()


def list_owners(page: Page, page_num: int = 1):
    """## List all owners on page

    ### Args:
        - `page (Page)`: The current page
        - `page_num (int, optional)`: The page to show. Defaults to 1.
    """
    page.get_by_role("link").filter(has_text="Find owners").click()
    page.get_by_role("button", name="Find Owner").click()
    for _ in range(0, page_num-1):
        page.get_by_title("Next").click()


def show_owner_details(page: Page, name: str):
    """## Show details of owner

    ### Args:
        - `page (Page)`: The current page
        - `name (str)`: The name of the owner to display
    """
    page.get_by_role("link", name=name).click()


def edit_owner(page: Page, name: str):
    """## Edit owner

    ### Args:
        - `page (Page)`: The current page
        - `name (str)`: The name of the owner to edit
    """
    page.get_by_role("link", name=name).click()
    page.get_by_role("link", name="Edit Owner").click()
    page.get_by_role("button", name="Update Owner").click()


def add_owner(page: Page, firstname: str, lastname: str, street: str, city: str, telephone: str):
    """## Add a new owner

    ### Args:
        - `page (Page)`: The current page
        - `firstname (str)`: The firstname of the owner
        - `lastname (str)`: The lastname of the owner
        - `street (str)`: The street of the owner
        - `city (str)`: The city of the owner
        - `telephone (str)`: The telephone of the owner
    """
    page.get_by_role("link", name="Add Owner").click()
    page.locator("#firstName").fill(firstname)
    page.locator("#lastName").fill(lastname)
    page.locator("#address").fill(street)
    page.locator("#city").fill(city)
    page.locator("#telephone").fill(telephone)
    page.get_by_role("button", name="Add Owner").click()


def add_pet(page: Page, name: str, birth_date: str, type: str):
    """## Add new pet

    ### Args:
        - `page (Page)`: The current page
        - `name (str)`: The name of the pet
        - `birth_date (str)`: The birthdate of the pet
        - `type (str)`: The type of the pet
    """
    page.get_by_role("link", name="Add New Pet").click()
    page.locator("#name").fill(name)
    page.locator("#birthDate").fill(birth_date)
    page.locator("#type").select_option(type)
    page.get_by_role("button", name="Add Pet").click()


def find_veterinarians(page: Page, page_num: int = 1):
    """## Find veterinarians

    ### Args:
        - `page (Page)`: The current page
        - `page_num (int, optional)`: The page to show. Defaults to 1.
    """
    page.get_by_role("link").filter(has_text="Veterinarians").click()
    for i in range(0, page_num-1):
        page.get_by_title("Next").click()


def raise_error(page: Page):
    """## Trigger error

    ### Args:
        - `page (Page)`: The current page
    """
    page.get_by_role("link").filter(has_text="Error").click()
