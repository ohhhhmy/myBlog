# Generated by Django 2.2.2 on 2019-07-18 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_auto_20190717_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='guestbook',
            name='title',
            field=models.CharField(default=50, max_length=100),
            preserve_default=False,
        ),
    ]
