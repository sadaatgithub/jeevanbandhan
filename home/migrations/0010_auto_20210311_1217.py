# Generated by Django 3.1.6 on 2021-03-11 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20210311_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileinfo',
            name='pincode',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
