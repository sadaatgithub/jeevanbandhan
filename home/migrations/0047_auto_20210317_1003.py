# Generated by Django 3.1.6 on 2021-03-17 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0046_auto_20210317_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileinfo',
            name='pro_created',
            field=models.CharField(blank=True, choices=[('Son', 'Son'), ('Daughter', 'Daughter'), ('Brother', 'Brother'), ('Sister', 'Sister'), ('Self', 'Self')], max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='profileinfo',
            name='religion',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
