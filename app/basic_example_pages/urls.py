from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("contact/", ContactPageView.as_view(), name="contact"),
    path("book/<int:pk>/", BookDetailView.as_view(), name="book_detail"),
    path("book/new/", BookCreateView.as_view(), name="book_new"),
    path("book/<int:pk>/update/", BookUpdateView.as_view(), name="book_update"),
    path("book/<int:pk>/delete/", BookDeleteView.as_view(), name="book_delete"),
]
