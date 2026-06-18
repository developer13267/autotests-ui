from playwright.sync_api import sync_playwright, expect
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    #кнопка "Registration" находится в состоянии disabled
    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_disabled()

     #Заполняем поле почты
    email_input = page.get_by_test_id('registration-form-email-input')
    email_input.fill("user.name@gmail.com")

    #Заполняем поле имя пользователя
    username_input = page.get_by_test_id('registration-form-username-input')
    username_input.fill('username')

    #Заполняем поле пароль
    password_input = page.get_by_test_id('registration-form-password-input')
    password_input.fill('password')


    #Проверить, что кнопка "Registration" перешла в состояние enabled
    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).not_to_be_disabled()
   
