# Generated by Django 4.2.7 on 2023-12-09 02:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pakistan', '0018_alter_history_time_now'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='time_now',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 9, 10, 3, 52, 343684), verbose_name='更新时间'),
        ),
    ]
