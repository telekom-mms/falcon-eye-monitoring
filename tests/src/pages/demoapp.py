def find_owners(page, page_num=1):
    page.get_by_role("link").filter(has_text="Find owners").click()
    page.get_by_role("button", name="Find Owner").click()
    for i in range(0, page_num-1):
        page.get_by_title("Next").click()


def show_owner(page, name):
    page.get_by_role("link", name=name).click()


def edit_owner(page, name):
    page.get_by_role("link", name=name).click()
    page.get_by_role("link", name="Edit Owner").click()
    page.get_by_role("button", name="Update Owner").click()


def find_veterinarians(page, page_num=1):
    page.get_by_role("link").filter(has_text="Veterinarians").click()
    for i in range(0, page_num-1):
        page.get_by_title("Next").click()


def raise_error(page):
    page.get_by_role("link").filter(has_text="Error").click()
