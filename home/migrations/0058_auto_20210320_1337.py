# Generated by Django 3.1.6 on 2021-03-20 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0057_auto_20210320_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileinfo',
            name='dob',
            field=models.DateField(null=True, verbose_name='Date of Birth/Time - Format : YYYY-MM-DD HH:MM'),
        ),
    ]