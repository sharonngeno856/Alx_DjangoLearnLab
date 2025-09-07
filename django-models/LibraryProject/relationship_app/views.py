from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Book, Library

def list_books(request):
    """
    Function-based view that returns a plain text list of books:
    '<title> by <author>'
    """
    books = Book.objects.select_related("author").all()
    if not books.exists():
        return HttpResponse("No books found.", content_type="text/plain")

    lines = []
    for book in books:
        author = getattr(book.author, "name", None) or str(book.author)
        lines.append(f"{book.title} by {author}")

    return HttpResponse("\n".join(lines), content_type="text/plain")


class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"
