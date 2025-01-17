# Generated by Django 5.0 on 2024-12-03 21:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, default='No description', null=True)),
                ('avatar_image', models.ImageField(blank=True, null=True, upload_to='author_avatars/')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('publication_date', models.DateField()),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='covers/')),
                ('is_available', models.BooleanField(default=True)),
                ('copy_count', models.IntegerField(default=1)),
                ('author', models.ManyToManyField(to='librarius.author')),
                ('holders', models.ManyToManyField(blank=True, default=None, to=settings.AUTH_USER_MODEL)),
                ('category', models.ManyToManyField(related_name='books', to='librarius.category')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
                ('books_assignes', models.ManyToManyField(related_name='user_books', to='librarius.book')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
