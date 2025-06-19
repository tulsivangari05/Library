from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Count
from django.http import HttpResponse
from .models import Book, Author, Category
from .forms import BookForm, AuthorForm, CategoryForm, ContactForm

# --- Admin check decorator ---
def admin_required(view_func):
    return user_passes_test(lambda u: u.is_superuser)(view_func)

# --- Views ---

def home(request):
    books = Book.objects.all().select_related('category').prefetch_related('authors')
    return render(request, 'library/home.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book.objects.prefetch_related('authors'), pk=book_id)
    return render(request, 'library/book_detail.html', {'book': book})

@login_required
@admin_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()
    return render(request, 'library/book_form.html', {'form': form, 'action': 'Add'})

@login_required
@admin_required
def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm(instance=book)
    return render(request, 'library/book_form.html', {'form': form, 'action': 'Edit'})

@login_required
@admin_required
def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return redirect('home')

@login_required
@admin_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AuthorForm()
    return render(request, 'library/author_form.html', {'form': form, 'action': 'Add'})

@login_required
@admin_required
def edit_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AuthorForm(instance=author)
    return render(request, 'library/author_form.html', {'form': form, 'action': 'Edit'})

@login_required
@admin_required
def delete_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    author.delete()
    return redirect('home')

@login_required
@admin_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoryForm()
    return render(request, 'library/category_form.html', {'form': form, 'action': 'Add'})

@login_required
@admin_required
def edit_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'library/category_form.html', {'form': form, 'action': 'Edit'})

@login_required
@admin_required
def delete_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    category.delete()
    return redirect('home')

@login_required
@admin_required
def stats_view(request):
    stats = {
        'books_count': Book.objects.count(),
        'authors_count': Author.objects.count(),
        'categories_count': Category.objects.count(),
    }
    return render(request, 'library/stats.html', {'stats': stats})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponse('Thanks for your message!')
    else:
        form = ContactForm()
    return render(request, 'library/contact.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'library/register.html', {'form': form})

def custom_404(request, exception):
    return render(request, 'library/404.html', status=404)
