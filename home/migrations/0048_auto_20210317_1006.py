# Generated by Django 3.1.6 on 2021-03-17 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0047_auto_20210317_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileinfo',
            name='pro_created',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
    ]