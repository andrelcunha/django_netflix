# Generated by Django 5.1.3 on 2024-11-18 18:56

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uu_id', models.UUIDField(default=uuid.uuid4)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('release_date', models.DateField()),
                ('genre', models.CharField(choices=[('action', 'Action'), ('comedy', 'Comedy'), ('drama', 'Drama'), ('horror', 'Horror'), ('romance', 'Romance'), ('sci-fi', 'Sci-Fi'), ('thriller', 'Thriller'), ('western', 'Western'), ('animation', 'Animation'), ('documentary', 'Documentary'), ('family', 'Family'), ('fantasy', 'Fantasy')], max_length=100)),
                ('length', models.PositiveIntegerField()),
                ('image_card', models.ImageField(upload_to='movie_images/')),
                ('image_cover', models.ImageField(upload_to='movie_images/')),
                ('video', models.FileField(upload_to='movie_videos/')),
                ('movie_viiews', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
