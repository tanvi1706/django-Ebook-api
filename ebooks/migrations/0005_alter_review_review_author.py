# Generated by Django 3.2.3 on 2021-06-07 11:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ebooks', '0004_rename_reviews_review_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review_author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
