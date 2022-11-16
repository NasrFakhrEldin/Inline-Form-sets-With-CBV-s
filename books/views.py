from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from books.models import Author, Book

class HomeView(TemplateView):
    template_name = "books/home.html"


class AuthorListView(ListView):
    model = Author
    template_name = "books/author_list.html"
    
class AuthorDetailView(DetailView):
    model = Author
    template_name = "books/author_detail.html"