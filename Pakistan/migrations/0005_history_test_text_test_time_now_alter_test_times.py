# Generated by Django 4.2.7 on 2023-12-08 01:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pakistan', '0004_test_delete_history'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('times', models.CharField(max_length=30, verbose_name='历史时期')),
                ('text', models.TextField(blank=True, null=True, verbose_name='历史内容')),
            ],
            options={
                'verbose_name': 'history of Pakistan',
                'verbose_name_plural': 'history of Pakistan',
            },
        ),
        migrations.AddField(
            model_name='test',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='历史内容'),
        ),
        migrations.AddField(
            model_name='test',
            name='time_now',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 8, 9, 54, 31, 916733), verbose_name='历史内容'),
        ),
        migrations.AlterField(
            model_name='test',
            name='times',
            field=models.TextField(max_length=100, unique=True, verbose_name='历史时期'),
        ),
    ]
