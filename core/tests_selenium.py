from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class MySeleniumTests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        service = Service(executable_path=r"C:\webdrivers\chromedriver.exe")
        cls.selenium = webdriver.Chrome(service=service)
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_homepage(self):
        self.selenium.get(f'{self.live_server_url}')
        assert 'Catstagram' in self.selenium.title
