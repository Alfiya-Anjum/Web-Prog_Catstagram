from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post
from django.utils import timezone
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

User = get_user_model()

class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create user and post for the test case
        test_user = User.objects.create_user(username='testuser', password='12345')
        cls.post = Post.objects.create(
            user=test_user,
            caption='Just a test caption',
            image='post_images/sample.jpg',  # Adjust path as needed
            created_at=timezone.now(),
            no_of_likes=0
        )

    def test_caption_content(self):
        post = Post.objects.get(id=self.post.id)
        self.assertEqual(post.caption, 'Just a test caption')

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
