# Generated by Django 4.1.2 on 2022-11-06 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_rename_recommend_gamereview_liked'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamereview',
            name='lastUpdated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
