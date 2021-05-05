# Generated by Django 3.1.6 on 2021-03-02 05:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='profileinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conttact_no', models.IntegerField()),
                ('address', models.CharField(blank=True, max_length=250)),
                ('city', models.CharField(blank=True, max_length=250)),
                ('state', models.CharField(blank=True, max_length=250)),
                ('pincode', models.IntegerField()),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('height', models.FloatField()),
                ('pro_pic', models.FileField(upload_to='profile_pic')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
