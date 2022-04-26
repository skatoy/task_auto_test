import pytest as pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(7)
    return browser

class TestButton:
    def test_link(self, browser):
            browser.get(link)
            button=browser.find_element_by_css_selector(".btn-add-to-basket")
            assert button
