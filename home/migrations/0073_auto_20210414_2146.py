# Generated by Django 3.1.6 on 2021-04-14 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0072_auto_20210408_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileinfo',
            name='education',
            field=models.CharField(blank=True, choices=[('Bachelors', 'Bachelors'), ('Masters', 'Masters'), ('Doctorate', 'Doctorate'), ('Diploma', 'Diploma'), ('Secondary', 'Secondary'), ('High School', 'High School')], max_length=50, null=True),
        ),
    ]