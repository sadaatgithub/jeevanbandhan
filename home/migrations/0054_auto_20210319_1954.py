# Generated by Django 3.1.6 on 2021-03-19 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0053_auto_20210319_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileinfo',
            name='age',
            field=models.IntegerField(blank=True, default=0, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profileinfo',
            name='dob',
            field=models.DateTimeField(null=True, verbose_name='Date of Birth/Time - Format : YYYY-MM-DD HH:MM'),
        ),
    ]
