from playwright.sync_api import sync_playwright, expect

def test_empty_courses_list():
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

        # сохраняем состояние
        context.storage_state(path='browser-state.json')
        page.wait_for_timeout(5000)

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browser-state.json')
        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        # Проверка наличия и текста заголовка "Courses"
        courses_clik = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_clik).to_be_visible()
        expect(courses_clik).to_have_text("Courses")

        # наличие и текст блока "There is no results"
        text_title = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(text_title).to_be_visible()
        expect(text_title).to_have_text("There is no results")

        # наличие и видимость иконки пустого блока
        view_icon = page.get_by_test_id('courses-list-empty-view-icon')
        expect(view_icon).to_be_visible()

        # наличие и текст описания блока: "Results from the load test pipeline will be displayed here"
        description_text = page.get_by_test_id('courses-list-empty-view-description-text')
        expect(description_text).to_be_visible()
        expect(description_text).to_have_text("Results from the load test pipeline will be displayed here")
