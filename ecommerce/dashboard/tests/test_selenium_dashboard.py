import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



# @pytest.mark.selenium
# def test_create_new_admin_user(create_admin_user):   # Ese create_admin_user viene de "def create_admin_user(....)" en fixtures.py
#     assert create_admin_user.__str__() == "admintest"


# Por uso de live_server, mirar https://pytest-django.readthedocs.io
@pytest.mark.selenium
def test_dashboard_admin_login(live_server, db_fixture_setup, chrome_browser_instance):  # Poniendo create_admin_user, permite que el usuario y la base de datos sigan exitiendo al momento de hacer el test de login
    browser = chrome_browser_instance
    browser.get(("%s%s" % (live_server.url, "/admin/login/")))

    user_name = browser.find_element(By.NAME, "username")
    user_password = browser.find_element(By.NAME, "password")
    submit = browser.find_element(By.XPATH, '//input[@value="Log in"]') 
    
    user_name.send_keys("admintest")
    user_password.send_keys("passwordtest")
    submit.send_keys(Keys.RETURN)

    assert "Site administration" in browser.page_source


def test_example():
    assert "Hello" == "Hello"

