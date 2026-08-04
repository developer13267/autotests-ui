from playwright.sync_api import sync_playwright, expect, Page
import pytest


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(chromium_page: Page):
        with sync_playwright() as playwright:
                browser = playwright.chromium.launch(headless=False)
                context = browser.new_context()
                page = context.new_page()


                chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

                # Заполняем поле почты
                email_input = chromium_page.get_by_test_id('registration-form-email-input').locator('input')
                email_input.fill("user.name@gmail.com")

                # Заполняем поле имя пользователя
                username_input = chromium_page.get_by_test_id('registration-form-username-input').locator('input')
                username_input.fill('username')

                # Заполняем поле пароль
                password_input = chromium_page.get_by_test_id('registration-form-password-input').locator('input')
                password_input.fill('password')

                # Нажмет на кнопку Registration и редирект на страницу "Dashboard
                registration_link = chromium_page.get_by_test_id('registration-page-registration-button')
                registration_link.click()
                chromium_page.wait_for_url("**/dashboard")

                # Отображение заголовка Dashboard
                wrong_title = chromium_page.get_by_test_id('dashboard-toolbar-title-text')
                expect(wrong_title).to_be_visible()
                expect(wrong_title).to_have_text("Dashboard")

