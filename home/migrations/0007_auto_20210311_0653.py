# Generated by Django 3.1.6 on 2021-03-11 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_profileinfo_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileinfo',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
