# Generated by Django 3.1.6 on 2021-03-20 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0061_profileinfo_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileinfo',
            name='complexion',
            field=models.CharField(default='Not Specified', max_length=50, null=True),
        ),
    ]
