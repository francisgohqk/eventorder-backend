# Generated by Django 5.0.4 on 2024-04-26 20:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventorder',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='eventorder',
            name='attendance',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='eventorder',
            name='end_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='eventorder',
            name='start_time',
            field=models.TimeField(),
        ),
    ]
