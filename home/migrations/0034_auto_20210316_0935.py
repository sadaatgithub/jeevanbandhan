# Generated by Django 3.1.6 on 2021-03-16 04:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_profileinfo_pid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profileinfo',
            old_name='pId',
            new_name='pro_Id',
        ),
    ]
