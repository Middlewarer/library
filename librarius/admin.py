from django.contrib import admin
from .models import *

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date')

admin.site.register(Book, BookAdmin)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(BookReview)