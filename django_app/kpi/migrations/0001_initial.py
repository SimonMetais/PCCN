# Generated by Django 5.0.6 on 2024-07-23 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('is_authenticated', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('full_url', models.CharField(max_length=200, primary_key=True, serialize=False)),
            ],
        ),
    ]
