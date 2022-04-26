import pytest as pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

class TestAnswer1:
    def test_answer1_link(self, browser):
            browser.get(link)
            browser.find_element(By.TAG_NAME,value='Добавить в корзину')