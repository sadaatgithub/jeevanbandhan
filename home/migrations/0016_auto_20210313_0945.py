# Generated by Django 3.1.6 on 2021-03-13 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20210313_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileinfo',
            name='pincode',
            field=models.FloatField(blank=True, default='0', null=True),
        ),
    ]
