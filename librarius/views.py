from django.shortcuts import render, HttpResponseRedirect, redirect
from django.views.generic import ListView, DetailView, UpdateView, CreateView, TemplateView
from extra_views import ModelFormSetView
from django.urls import reverse, reverse_lazy
from .models import Book, Author, Category, BookReview
from django.views.generic.detail import SingleObjectMixin
from .forms import BookForm, CategoryForm, AuthorForm
from django.contrib.auth.mixins import PermissionRequiredMixin

class IndexView(ListView):
    template_name = 'librarius/index_page.html'
    model = Book
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BookForm()

        return context
    
    def post(self, request, *args, **kwargs):
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # сохраняем форму
            return redirect('books:index')  # перенаправляем на главную страницу после успешной отправки формы
        context = self.get_context_data()
        context['form'] = form  # передаем форму с ошибками в контекст, если она невалидна
        return self.render_to_response(context)
    
    
class BookDetailView(DetailView):
    template_name = 'librarius/book_detail.html'
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book_id = self.object.id
        reviews = BookReview.objects.filter(book=book_id)
        context['reviews'] = reviews
        return context
        
def assign_tome_book(request, pk):
    
    book = Book.objects.get(id=pk)
    book.holders.add(request.user)
    book.copy_count -= 1
    book.save()
    

    return redirect('books:index')


class AuthorPage(DetailView):
    model = Author
    template_name = 'librarius/author_page.html'
    context_object_name = 'author'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj'] = self.object
        context['supporters_count'] = self.object.supporters.all().count()
        return context


def delete_book_entry(request, pk):
    object = Book.objects.get(pk=pk)
    object.delete()
    return redirect(request.META.get('HTTP_REFERER', '/'))


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'librarius/book_update.html'
    success_url = reverse_lazy('books:index')


def author_support(request, pk):
    author = Author.objects.get(pk=pk)
    author.supporters.add(request.user)
    return redirect('books:author_page', pk=pk)

def author_support_decline(request, pk):
    author = Author.objects.get(pk=pk)
    author.supporters.delete(request.user)
    author.save()


class CreateCategoryOfBookView(PermissionRequiredMixin, CreateView):
    model = Category
    template_name = 'librarius/create_category.html'
    form_class = CategoryForm
    permission_required = 'is_staff'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect(reverse_lazy('books:index'))
        else:
            return super().dispatch(request, *args, **kwargs)
        

class CreateAuthorView(PermissionRequiredMixin, CreateView):
    model = Author
    template_name = 'librarius/create_author.html'
    form_class = AuthorForm
    permission_required = 'is_staff'
    success_url = reverse_lazy('books:index')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect(reverse_lazy('books:index'))
        else:
            return super().dispatch(request, *args, **kwargs)
        

class HelloPage(TemplateView):
    template_name = 'librarius/hello_page.html'
    

