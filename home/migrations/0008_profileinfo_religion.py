# Generated by Django 3.1.6 on 2021-03-11 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20210311_0653'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileinfo',
            name='religion',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
