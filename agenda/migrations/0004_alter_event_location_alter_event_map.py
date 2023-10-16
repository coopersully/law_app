# Generated by Django 4.2.4 on 2023-10-10 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0003_alter_event_map'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(default='Cambridge', max_length=200),
        ),
        migrations.AlterField(
            model_name='event',
            name='map',
            field=models.URLField(default='https://maps.app.goo.gl/J5oJ5SHma4qW7UHs5', max_length=500),
        ),
    ]