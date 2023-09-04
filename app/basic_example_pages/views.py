from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Book
from django.urls import reverse_lazy


class HomePageView(ListView):
    model = Book
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"


class ContactPageView(TemplateView):
    template_name = "contact.html"


class BookDetailView(DetailView):
    model = Book
    template_name = "book_detail.html"


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    template_name = "book_new.html"
    fields = ["title", "genre", "author", "publish_date"]

class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    template_name = "book_update.html"
    fields = '__all__'


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = "book_delete.html"
    success_url = reverse_lazy("home")
