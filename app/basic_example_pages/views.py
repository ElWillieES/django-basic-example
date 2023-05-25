from django.views.generic import TemplateView, ListView
from .models import Book

class HomePageView(ListView):
    model = Book
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"


class ContactPageView(TemplateView):
    template_name = "contact.html"
