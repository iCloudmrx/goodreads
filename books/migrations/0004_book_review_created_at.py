# Generated by Django 4.0.5 on 2023-05-22 17:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_review',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
