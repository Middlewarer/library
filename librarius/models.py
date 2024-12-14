from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Book(models.Model):
    holders = models.ManyToManyField(User, default=None, blank=True)
    title = models.CharField(max_length=255)
    author = models.ManyToManyField('Author')
    description = models.TextField()
    publication_date = models.DateField()
    cover_image = models.ImageField(upload_to='covers/', null=True, blank=True)
    category = models.ManyToManyField('Category', related_name='books')
    is_available = models.BooleanField(default=True)
    copy_count = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.title}'
    

class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    

class Author(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True, default='')
    avatar_image = models.ImageField(upload_to='author_avatars/', null=True, blank=True)
    supporters = models.ManyToManyField(User, related_name='author_supporters')

    def __str__(self):
        return self.name
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    books_assignes = models.ManyToManyField(Book, related_name='user_books')

    def __str__(self):
        return self.user.username
    

class BookReview(models.Model):
    RATES = ((1, 'Bad!'),
             (2, 'Not good'),
             (3, 'Ok'),
             (4, 'Well done!'),
             (5, 'Incredible!'))
    
    book = models.ForeignKey(Book, on_delete=models.CASCADE) 
    rate = models.PositiveIntegerField(choices=RATES, verbose_name="Rating", help_text="Rate the book from 1 to 5.")
    comment = models.TextField(blank=True, null=True)

    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Создаем профиль для нового пользователя
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    # Сохраняем профиль при изменении пользователя
    instance.userprofile.save()
    

