# Generated by Django 4.0.1 on 2022-05-14 09:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_post_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 5, 14, 9, 51, 56, 242608, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
