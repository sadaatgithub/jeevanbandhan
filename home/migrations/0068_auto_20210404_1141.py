# Generated by Django 3.1.6 on 2021-04-04 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0067_auto_20210401_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileinfo',
            name='middlename',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
    ]