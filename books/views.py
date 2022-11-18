from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    FormView,
)
from books.models import Author, Book
from django.contrib import messages
from django.views.generic.detail import SingleObjectMixin
from books.forms import AuthorBooksFormset
from django.http import HttpResponseRedirect
from django.urls import reverse


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


class AuthorBooksEditView(SingleObjectMixin, FormView):
    model = Author
    template_name = "books/author_books_edit.html"
    success_url = "/"
    queryset = Author.objects.all()

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=self.queryset)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=self.queryset)
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=AuthorBooksFormset):

        return form_class(**self.get_form_kwargs(), instance=self.object)

    def get_success_url(self):
        return reverse("books:author_detail", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        form.save()
        messages.add_message(
            self.request,
            messages.SUCCESS,
            "Changes were saved",
        )
        return HttpResponseRedirect(self.get_success_url())
