import os
import random
import string
from datetime import datetime

import pytest
from faker import Faker
from playwright.sync_api import Page, Playwright, expect
from src.pages import demoapp
from src.test.base import PreFlightCheck


class Demoapp(PreFlightCheck):

    def __init__(self):
        self.url = PreFlightCheck.get_config("DEMOAPP_URL")
        self.browser = None

    def setup(self, playwright: Playwright) -> Page:
        """ Login if no context """
        if self.browser is None:
            self.browser = playwright.firefox.launch_persistent_context(
                user_data_dir=f"./test_demoapp_{datetime.timestamp(datetime.now())}",
                headless=os.getenv("HEADLESS") in ("true", "True", "TRUE"))
        page = self.browser.pages[0]

        page.goto(self.url)

        return page


class DemoAppData:

    class Owner:
        def __init__(self, first_name: str, last_name: str, address: str, city: str, phone: str):
            self.first_name = first_name
            self.last_name = last_name
            self.address = address
            self.city = city
            self.telephone = phone

    class Pet:
        def __init__(self, name: str, type: str, birth_date=datetime.date(datetime.now()).isoformat()):
            self.name = name
            self.birth_date = birth_date
            self.type = type


    def __init__(self):
        faker = Faker()
        self.owner = self.Owner(faker.name(), faker.name(), faker.address(), faker.city(),
                                ''.join(random.choice(string.digits) for _ in range(10)))
        self.pet = self.Pet(faker.name(), random.sample(["cat", "dog", "bird", "hamster", "lizard", "snake"], 6)[0])


subject = Demoapp()
data = DemoAppData()


@pytest.mark.base
def test_owners_page(playwright: Playwright) -> None:
    page = subject.setup(playwright)

    demoapp.list_owners(page)

    expect(page.get_by_role("link", name="George Franklin")).to_be_visible()
    expect(page.get_by_role("link", name="Betty Davis")).to_be_visible()
    expect(page.get_by_role("link", name="Eduardo Rodriquez")).to_be_visible()
    expect(page.get_by_role("link", name="Harold Davis")).to_be_visible()
    expect(page.get_by_role("link", name="Peter McTavish")).to_be_visible()

    demoapp.list_owners(page, 2)

    expect(page.get_by_role("link", name="Jean Coleman")).to_be_visible()
    expect(page.get_by_role("link", name="Jeff Black")).to_be_visible()
    expect(page.get_by_role("link", name="Maria Escobito")).to_be_visible()
    expect(page.get_by_role("link", name="David Schroeder")).to_be_visible()
    expect(page.get_by_role("link", name="Carlos Estaban")).to_be_visible()


@pytest.mark.extended
def test_owners_actions(playwright: Playwright) -> None:
    page = subject.setup(playwright)

    demoapp.list_owners(page)
    demoapp.show_owner_details(page, "George Franklin")

    expect(page.get_by_role("link", name="Edit Owner")).to_be_visible()
    expect(page.get_by_role("link", name="Add New Pet")).to_be_visible()

    expect(page.get_by_role("link", name="Edit Pet")).to_be_visible()
    expect(page.get_by_role("link", name="Add Visit")).to_be_visible()


@pytest.mark.extended
def test_owner_edit(playwright: Playwright) -> None:
    page = subject.setup(playwright)

    demoapp.list_owners(page)
    demoapp.edit_owner(page, "George Franklin")

    expect(page.get_by_text("Owner Values Updated")).to_be_visible()


@pytest.mark.extended
def test_owner_add(playwright: Playwright) -> None:
    page = subject.setup(playwright)

    demoapp.owners_index(page)
    demoapp.add_owner(page, data.owner.first_name, data.owner.last_name, data.owner.address, data.owner.city, data.owner.telephone)

    expect(page.get_by_text("New Owner Created")).to_be_visible()


@pytest.mark.extended
def test_pet_add(playwright: Playwright) -> None:
    page = subject.setup(playwright)

    demoapp.owners_index(page)
    demoapp.search_owners(page, data.owner.last_name)
    demoapp.add_pet(page, data.pet.name, data.pet.birth_date, data.pet.type)

    expect(page.get_by_text("New Pet has been Added")).to_be_visible()


@pytest.mark.base
def test_veterinarians_page(playwright: Playwright) -> None:
    page = subject.setup(playwright)

    demoapp.find_veterinarians(page)

    expect(page.get_by_role("cell", name="James Carter")).to_be_visible()
    expect(page.get_by_role("cell", name="Helen Leary")).to_be_visible()
    expect(page.get_by_role("cell", name="Linda Douglas")).to_be_visible()
    expect(page.get_by_role("cell", name="Rafael Ortega")).to_be_visible()
    expect(page.get_by_role("cell", name="Henry Stevens")).to_be_visible()

    demoapp.find_veterinarians(page, 2)

    expect(page.get_by_role("cell", name="Sharon Jenkins")).to_be_visible()


@pytest.mark.base
def test_raise_error(playwright: Playwright) -> None:
    page = subject.setup(playwright)

    demoapp.raise_error(page)

    expect(page.get_by_role("heading", name="Something happened...")).to_be_visible()
