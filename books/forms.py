from django.forms.models import inlineformset_factory
from books.models import Book, Author

AuthorBooksFormset = inlineformset_factory(Author, Book, fields=("title",), extra=1, absolute_max=1500)
