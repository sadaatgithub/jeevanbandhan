# Generated by Django 3.1.6 on 2021-03-18 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0049_profileinfo_rashi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileinfo',
            name='b_Group',
            field=models.CharField(blank=True, choices=[('A +ve', 'A +ve'), ('A -ve', 'A -ve'), ('B +ve', 'B +ve'), ('B -ve', 'B -ve'), ('O +ve', 'O +ve'), ('O -ve', 'O -ve'), ('AB +ve', 'AB +ve'), ('AB -ve', 'AB-ve')], max_length=50, null=True),
        ),
    ]