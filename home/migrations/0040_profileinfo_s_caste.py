# Generated by Django 3.1.6 on 2021-03-16 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0039_auto_20210316_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileinfo',
            name='s_caste',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
    ]
