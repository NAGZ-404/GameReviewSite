# Generated by Django 4.1.2 on 2022-11-06 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_gamereview_lastupdated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamereview',
            name='lastUpdated',
        ),
    ]
