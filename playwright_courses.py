from playwright.sync_api import sync_playwright

with sync_playwright() as plawright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    #Заполняем поле почты
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill("user.name@gmail.com")

    #Заполняем поле имя пользователя
    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    #Заполняем поле пароль
    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    #Нажметм на кнопку Registration
    registration_link = page.get_by_test_id('registration-page-registration-button')
    registration_link.click()
    
with sync_playwright() as plawright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    #Проверка наличия и текста заголовка "Courses" 




    #наличие и текст блока "There is no results"

    #наличие и видимость иконки пустого блока
    #наличие и текст описания блока: "Results from the load test pipeline will be displayed here"
