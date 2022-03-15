# Generated by Django 4.0.3 on 2022-03-15 08:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='users_like',
            field=models.ManyToManyField(blank=True, null=True, related_name='article_liked', to=settings.AUTH_USER_MODEL),
        ),
    ]
