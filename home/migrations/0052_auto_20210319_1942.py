# Generated by Django 3.1.6 on 2021-03-19 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0051_auto_20210319_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileinfo',
            name='age',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='profileinfo',
            name='dob',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
