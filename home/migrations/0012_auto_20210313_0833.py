# Generated by Django 3.1.6 on 2021-03-13 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20210311_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileinfo',
            name='age',
            field=models.IntegerField(blank=True, default=' ', null=True),
        ),
    ]
