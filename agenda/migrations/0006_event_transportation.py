# Generated by Django 4.2.4 on 2023-10-24 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0005_event_program'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='transportation',
            field=models.CharField(max_length=750, null=True),
        ),
    ]
