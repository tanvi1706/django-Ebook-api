# Generated by Django 3.2.3 on 2021-05-19 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ebooks', '0002_review_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='review',
            new_name='reviews',
        ),
    ]
