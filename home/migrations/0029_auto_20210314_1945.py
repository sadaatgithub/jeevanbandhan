# Generated by Django 3.1.6 on 2021-03-14 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_auto_20210314_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileinfo',
            name='pro_pic',
            field=models.FileField(blank=True, null=True, upload_to='profile_pic'),
        ),
    ]