import pytest
from playwright.sync_api import sync_playwright, Page

from pages.login_page import LoginPage


@pytest.fixture
def chromium_page() -> Page:
    with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False)
            yield browser.new_page()
            browser.close()


@pytest.fixture(scope="session")
def initialize_browser_state():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        # Заполняем поле почты
        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill("user.name@gmail.com")

        # Заполняем поле имя пользователя
        username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill('username')

        # Заполняем поле пароль
        password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill('password')

        # Нажметм на кнопку Registration
        registration_link = page.get_by_test_id('registration-page-registration-button')
        registration_link.click()



        # Сохраняем состояние браузера
        context.storage_state(path='browser-state.json')
        browser.close()

@pytest.fixture
def chromium_page_with_state(initialize_browser_state) -> Page:
    # Запускаем браузер
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browser-state.json')
        page = context.new_page()
        browser = playwright.chromium.launch(headless=False)

        page = context.new_page()

        # Возвращаем страницу для использования в тестах
        yield page

        # Закрываем контекст и браузер после завершения теста
        context.close()
        browser.close()


@pytest.fixture
def login_page(chromium_page:Page) -> LoginPage:
    return LoginPage(page=chromium_page)