from django import forms
from .models import Book

from django import forms
from .models import Book, Category, Author

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'holders',
            'title',
            'author',
            'description',
            'publication_date',
            'cover_image',
            'category',
            'is_available',
            'copy_count',
        ]
        widgets = {
            'holders': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the book title'}),
            'author': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Enter a brief description'}),
            'publication_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'cover_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'category': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'is_available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'copy_count': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={
                'class': 'resize-y h-20 w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500',
                'placeholder': 'Enter the description here...',
                'rows': 1,
            }),
        }
        exclude = ['supporters']


    

    

