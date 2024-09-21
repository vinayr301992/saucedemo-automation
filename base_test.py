import os

import allure
from playwright.sync_api import Playwright, sync_playwright


class BaseTest:
    def setup(self, headless=True,video_dir="videos"):
        os.makedirs(video_dir, exist_ok=True)
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=headless, slow_mo=1000)
        self.context = self.browser.new_context(viewport={"width": 1500, "height": 1080},
                                                record_video_dir= os.path.abspath(video_dir))
        self.page = self.context.new_page()


    def teardown(self):
        self.browser.close()
        self.playwright.stop()

    def take_screenshot(self, step_name: str):
        # Capture screenshot and attach it to the Allure report
        screenshot = self.page.screenshot()
        allure.attach(
            screenshot,
            name=step_name,
            attachment_type=allure.attachment_type.PNG
        )
