from playwright.sync_api import sync_playwright
import os

with sync_playwright() as pw:
    browser = pw.chromium.launch(channel="msedge", headless=False)
    page = browser.new_page()

    url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
    page.goto(url, wait_until="networkidle")

    selector = "div.mw-parser-output.ws-page-container.dynlayout-haspagenums"
    page.wait_for_selector(selector)

    os.makedirs("screenshots", exist_ok=True)
    output_path = "screenshots/chapter1_full_clean.png"
    page.locator(selector).screenshot(path=output_path)

    print(f"✅ Saved clean full element screenshot at {output_path}")

    browser.close()

