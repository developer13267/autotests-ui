from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Заполняем поле почты
    email_input = page.get_by_testid('registration-form-email-input')
    email_input.fill("user.name@gmail.com")

    # Заполняем поле имя пользователя
    username_input = page.get_by_testid('registration-form-username-input')
    username_input.fill('username')

    # Заполняем поле пароль
    password_input = page.get_by_testid('registration-form-password-input')
    password_input.fill('password')

    # Нажмет на кнопку Registration и редирект на страницу "Dashboard
    registration_link = page.get_by_testid('registration-page-registration-button')
    registration_link.click()
    page.wait_for_url("**/dashboard")

    # Отображение заголовка Dashboard
    wrong_title = page.get_by_testid('dashboard-toolbar-title-text')
    expect(wrong_title).to_be_visible()
    expect(wrong_title).to_have_text("Dashboard")


