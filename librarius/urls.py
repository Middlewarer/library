from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'books'

urlpatterns = [
    path('', views.HelloPage.as_view(), name='hello'),
    path('book_list', views.IndexView.as_view(), name='index'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('login/', LoginView.as_view(template_name='librarius/user_login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('book/<int:pk>/assign/', views.assign_tome_book, name='assign'),
    path('author/<int:pk>/', views.AuthorPage.as_view(), name='author_page'),
    path('book/<int:pk>/delete/', views.delete_book_entry, name='delete_book'),
    path('book/<int:pk>/update/', views.BookUpdateView.as_view(), name='update_book'),
    path('author/<int:pk>/support', views.author_support, name='support'),
    path('author/<int:pk>/unsupport', views.author_support_decline, name='decline_support'),
    path('create/category/', views.CreateCategoryOfBookView.as_view(), name='category_create'),
    path('create/author/', views.CreateAuthorView.as_view(), name='category_create'),

]

