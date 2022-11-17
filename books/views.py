from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from books.models import Author, Book
from django.contrib import messages


class HomeView(TemplateView):
    template_name = "books/home.html"


class AuthorListView(ListView):
    model = Author
    template_name = "books/author_list.html"


class AuthorDetailView(DetailView):
    model = Author
    template_name = "books/author_detail.html"


class AuthorCreateView(CreateView):
    model = Author
    template_name = "books/author_create.html"
    fields = ["name"]
    success_url = ""

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            "The author has been added",
        )
        return super().form_valid(form)
