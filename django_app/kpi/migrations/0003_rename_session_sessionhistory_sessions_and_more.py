# Generated by Django 5.0.6 on 2024-07-23 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kpi', '0002_sessionhistory_session_urls'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sessionhistory',
            old_name='session',
            new_name='sessions',
        ),
        migrations.RenameField(
            model_name='sessionhistory',
            old_name='url',
            new_name='urls',
        ),
    ]
