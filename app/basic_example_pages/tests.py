from django.test import SimpleTestCase, TestCase
from django.urls import reverse
from datetime import datetime
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
        self.assertContains(response, "El Camino")

    def test_book_model(self):
        self.assertEqual(self.book.title, "El Camino")
        self.assertEqual(self.book.genre, "Fiction")
        self.assertEqual(self.book.publish_date, "2006-03-16")
        self.assertEqual(self.book.author.name, "Miguel Delibes")
        self.assertEqual(str(self.book), "El Camino")
        self.assertEqual(self.book.get_absolute_url(), "/book/1/")

    def test_url_exists_at_correct_location_detailview(self):
        response = self.client.get("/book/1/")
        self.assertEqual(response.status_code, 200)

    def test_book_detailview(self):
        response = self.client.get(reverse("book_detail", kwargs={"pk": self.book.pk}))
        no_response = self.client.get("/book/9999/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "El Camino")
        self.assertTemplateUsed(response, "book_detail.html")

    def test_book_createview(self):
        response = self.client.post(
            reverse("book_new"),
            {
                "title": "New title",
                "genre": "Fiction",
                "author": 1,
                "publish_date": "2000-01-31",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Book.objects.last().title, "New title")
        self.assertEqual(Book.objects.last().genre, "Fiction")
        self.assertEqual(Book.objects.last().publish_date, datetime.strptime("2000-01-31", "%Y-%m-%d").date())

    def test_book_updateview(self):  # new
        response = self.client.post(
            reverse("book_update", args="1"),
            {
                "title": "Updated title",
                "genre": "Terror",
                "author": 1,
                "publish_date": "2001-01-31",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Book.objects.last().title, "Updated title")
        self.assertEqual(Book.objects.last().genre, "Terror")
        self.assertEqual(Book.objects.last().publish_date, datetime.strptime("2001-01-31", "%Y-%m-%d").date())

    def test_book_deleteview(self):
        response = self.client.post(reverse("book_delete", args="1"))
        self.assertEqual(response.status_code, 302)


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

