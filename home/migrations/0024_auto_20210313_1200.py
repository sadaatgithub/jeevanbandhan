# Generated by Django 3.1.6 on 2021-03-13 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_auto_20210313_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileinfo',
            name='pro_pic',
            field=models.FileField(blank=True, default='/media/media/default.png', null=True, upload_to='profile_pic'),
        ),
    ]