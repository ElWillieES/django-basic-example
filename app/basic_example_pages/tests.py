from django.test import SimpleTestCase, TestCase
from django.urls import reverse

from .models import BookAuthor, Book

class BookAuthorTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author = BookAuthor.objects.create(name="Miguel Delibes", country="España")

    def test_model_content(self):
        self.assertEqual(self.author.name, "Miguel Delibes")


class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author = BookAuthor.objects.create(name="Miguel Delibes", country="España")
        cls.book = Book.objects.create(title="El Camino", author=cls.author, genre="Fiction", publish_date="2006-03-16")

    def test_model_content(self):
        self.assertEqual(self.book.title, "El Camino")

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")

    def test_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<p>This is the Home page</p>")


class AboutpageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")

    def test_template_content(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<p>This is the About page</p>")


class ContactpageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/contact/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("contact"))
        self.assertTemplateUsed(response, "contact.html")

    def test_template_content(self):
        response = self.client.get(reverse("contact"))
        self.assertContains(response, "<p>This is the Contact page</p>")
