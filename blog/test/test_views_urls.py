from django.test import TestCase
from django.urls import reverse
from blog.models import Post, Author, Tag

class ViewTests(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            first_name="Pau", last_name="Segués", email="pau@example.com"
        )
        self.tag = Tag.objects.create(tag="Django")
        self.post = Post.objects.create(
            title="Títol del Post",
            excerpt="Resum",
            image_name="imatge.jpg",
            date="2024-05-24",
            slug="titol-del-post",
            content="Contingut del post",
            author=self.author
        )
        self.post.tags.add(self.tag)

    def test_starting_page(self):
        response = self.client.get(reverse("Starting-Page"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Títol del Post")

    def test_posts_page(self):
        response = self.client.get(reverse("post_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Títol del Post")

    def test_post_detail(self):
        response = self.client.get(reverse("post-detail", args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Contingut del post")

    def test_post_detail_404(self):
        response = self.client.get(reverse("post-detail", args=["no-existeix"]))
        self.assertEqual(response.status_code, 404)

    def test_authors_page(self):
        response = self.client.get(reverse("author_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Pau Segués")

    def test_author_detail(self):
        response = self.client.get(reverse("author-detail", args=["Pau", "Segués"]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Títol del Post")

    def test_author_detail_404(self):
        response = self.client.get(reverse("author-detail", args=["Nom", "Inexistent"]))
        self.assertEqual(response.status_code, 404)

    def test_tags_page(self):
        response = self.client.get(reverse("tag_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Django")

    def test_tag_detail(self):
        response = self.client.get(reverse("tag-detail", args=["Django"]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Títol del Post")

    def test_tag_detail_404(self):
        response = self.client.get(reverse("tag-detail", args=["Inexistent"]))
        self.assertEqual(response.status_code, 404)
