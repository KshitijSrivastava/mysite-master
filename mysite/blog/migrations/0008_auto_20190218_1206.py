# Generated by Django 2.1.5 on 2019-02-18 12:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190218_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 18, 12, 6, 45, 255907, tzinfo=utc), verbose_name='date_joined'),
        ),
    ]
