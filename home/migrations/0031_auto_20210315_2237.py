# Generated by Django 3.1.6 on 2021-03-15 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_profiledata'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileinfo',
            name='B_type',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='profileinfo',
            name='caste',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='profileinfo',
            name='drink',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='profileinfo',
            name='f_occ',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='profileinfo',
            name='m_occ',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='profileinfo',
            name='marital_status',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='profileinfo',
            name='no_bros',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='profileinfo',
            name='no_sis',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='profileinfo',
            name='pob',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='profileinfo',
            name='pro_created',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
    ]