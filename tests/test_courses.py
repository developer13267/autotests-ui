from playwright.sync_api import sync_playwright, expect, Page
import pytest

@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(chromium_page_with_state: Page):

        page = chromium_page_with_state
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
