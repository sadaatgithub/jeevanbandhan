# Generated by Django 3.1.6 on 2021-03-10 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210310_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileinfo',
            name='about',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
