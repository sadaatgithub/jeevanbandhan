# Generated by Django 3.1.6 on 2021-03-17 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0044_auto_20210316_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileinfo',
            name='dob',
            field=models.DateTimeField(null=True, verbose_name='Date of Birth/Time - Format : YYYY-MM-DD HH:MM'),
        ),
    ]