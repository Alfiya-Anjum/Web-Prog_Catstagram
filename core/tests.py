from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post
from django.utils import timezone

User = get_user_model()

class PostModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create user and post for the test case
        test_user = User.objects.create_user(username='testuser', password='12345')
        cls.post = Post.objects.create(
            user=test_user,
            caption='Just a test caption',
            image='post.image.url',  # Use a path that makes sense for your setup
            created_at=timezone.now(),
            no_of_likes=0
        )

    def test_caption_content(self):
        post = Post.objects.get(caption='Just a test caption')
        self.assertEqual(post.caption, 'Just a test caption')
