# Generated by Django 3.1.6 on 2021-03-19 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0050_auto_20210318_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileinfo',
            name='age',
            field=models.IntegerField(blank=True, default=0, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profileinfo',
            name='b_Group',
            field=models.CharField(blank=True, choices=[('A +ve', 'A +ve'), ('A -ve', 'A -ve'), ('B +ve', 'B +ve'), ('B -ve', 'B -ve'), ('O +ve', 'O +ve'), ('O -ve', 'O -ve'), ('AB +ve', 'AB +ve'), ('AB -ve', 'AB -ve')], max_length=50, null=True),
        ),
    ]