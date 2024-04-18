def owners_index(page):
    page.get_by_role("link").filter(has_text="Find owners").click()


def search_owners_by_name(page, name: str):
    page.locator("#lastName").fill(name)
    page.get_by_role("button", name="Find Owner").click()


def list_owners(page, page_num=1):
    page.get_by_role("link").filter(has_text="Find owners").click()
    page.get_by_role("button", name="Find Owner").click()
    for i in range(0, page_num-1):
        page.get_by_title("Next").click()


def show_owner_details(page, name):
    page.get_by_role("link", name=name).click()


def edit_owner(page, name):
    page.get_by_role("link", name=name).click()
    page.get_by_role("link", name="Edit Owner").click()
    page.get_by_role("button", name="Update Owner").click()


def add_owner(page, firstname: str, lastname: str, street: str, city: str, telephone: str):
    page.get_by_role("link", name="Add Owner").click()
    page.locator("#firstName").fill(firstname)
    page.locator("#lastName").fill(lastname)
    page.locator("#address").fill(street)
    page.locator("#city").fill(city)
    page.locator("#telephone").fill(telephone)
    page.get_by_role("button", name="Add Owner").click()


def add_pet(page, name: str, birth_date: str, type: str):
    page.get_by_role("link", name="Add New Pet").click()
    page.locator("#name").fill(name)
    page.locator("#birthDate").fill(birth_date)
    page.locator("#type").select_option(type)
    page.get_by_role("button", name="Add Pet").click()


def find_veterinarians(page, page_num=1):
    page.get_by_role("link").filter(has_text="Veterinarians").click()
    for i in range(0, page_num-1):
        page.get_by_title("Next").click()


def raise_error(page):
    page.get_by_role("link").filter(has_text="Error").click()
