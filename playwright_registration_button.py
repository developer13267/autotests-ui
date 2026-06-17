from playwright.sync_api import sync_playwright, expect
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    #кнопка "Registration" находится в состоянии disabled
    registration_button = page.get_y_test_id('registration-page-registration-button')
    expect(registration_button).to_be_disabled()

    #Заполнить поле Email значением: user.name@gmail.com

    #Заполнить поле Username значением: username


    #Заполнить поле Password значением: password


    #Проверить, что кнопка "Registration" перешла в состояние enabled
   
