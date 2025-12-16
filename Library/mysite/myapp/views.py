from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from django.db.models import Q

def book_list(request):
    q = request.GET.get("q")

    if q:
        books = Book.objects.filter(
            Q(title__icontains=q) |
            Q(author__icontains=q) |
            Q(published_yr__icontains=q)
        )
    else:
        books = Book.objects.all()

    return render(request, 'myapp/book_list.html', {'books': books})


def add_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        published_yr = request.POST.get("published_yr")
        quantity = request.POST.get("quantity")

        Book.objects.create(
            title=title,
            author=author,
            published_yr=int(published_yr),
            quantity=int(quantity)
        )

        return redirect('book_list')

    return render(request, 'myapp/add_book.html')


def edit_book(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.published_yr = request.POST.get("published_yr")
        book.quantity = request.POST.get("quantity")

        book.save()
        return redirect('book_list')

    return render(request, 'myapp/edit_book.html', {'book': book})


def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('book_list')
