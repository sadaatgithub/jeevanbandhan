# Generated by Django 3.1.6 on 2021-03-21 08:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0065_contact_us'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileinfo',
            name='favourites',
            field=models.ManyToManyField(blank=True, related_name='favourite', to=settings.AUTH_USER_MODEL),
        ),
    ]
