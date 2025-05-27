from django.test import TestCase
from blog.models import Author, Tag, Post

class ModelTests(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            first_name="Pau", last_name="Segués", email="pau@example.com"
        )
        self.tag1 = Tag.objects.create(tag="Django")
        self.tag2 = Tag.objects.create(tag="WebDev")
        self.post = Post.objects.create(
            title="Títol del Post",
            excerpt="Un petit resum del post.",
            image_name="imatge.jpg",
            date="2024-05-24",
            slug="titol-del-post",
            content="Contingut llarg del post.",
            author=self.author
        )
        self.post.tags.set([self.tag1, self.tag2])

    def test_author_str(self):
        self.assertEqual(str(self.author), "Pau Segués")

    def test_tag_str(self):
        self.assertEqual(str(self.tag1), "Django")

    def test_post_str(self):
        self.assertEqual(str(self.post), "Títol del Post")

    def test_post_author_relation(self):
        self.assertEqual(self.post.author.email, "pau@example.com")

    def test_post_tags_relation(self):
        tags = self.post.tags.all()
        self.assertEqual(tags.count(), 2)
        self.assertIn(self.tag1, tags)
        self.assertIn(self.tag2, tags)