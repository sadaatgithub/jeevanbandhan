# Generated by Django 3.1.6 on 2021-03-16 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0037_auto_20210316_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileinfo',
            name='age',
            field=models.CharField(blank=True, default=0, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profileinfo',
            name='height',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
