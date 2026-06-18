from playwright.sync_api import sync_playwright

with sync_playwright() as plawright:
    browser = playwright.chromium.launch(headless=False)
