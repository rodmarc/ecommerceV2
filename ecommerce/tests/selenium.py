import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# Esto es importante, pero no le tomé mucho asunto
# Ver desde minuto 37:25 de video https://www.youtube.com/watch?v=s3HuIRD5sUY&list=PLOLrQ9Pn6cay_cQkyg-WYYiJ_EKU8KWKh&index=2 
@pytest.fixture(scope="module")
def chrome_browser_instance(request):
    """
    Provide a selenium webdriver instance
    """
    options = Options()
    options.headless = False
    service = Service('/home/policeman/Develop/Curso/ecommerceV2/chromedriver')
    browser = webdriver.Chrome(service=service, options=options)
    yield browser
    browser.close()
