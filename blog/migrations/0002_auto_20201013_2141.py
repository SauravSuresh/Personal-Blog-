# Generated by Django 3.1.2 on 2020-10-13 16:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 10, 13, 16, 11, 33, 305520, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 10, 13, 16, 11, 33, 275568, tzinfo=utc)),
        ),
    ]