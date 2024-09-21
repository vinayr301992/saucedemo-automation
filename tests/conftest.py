import pytest
from playwright.sync_api import Playwright, sync_playwright


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {**browser_context_args, "headless": True}
