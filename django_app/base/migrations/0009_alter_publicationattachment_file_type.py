# Generated by Django 5.0.7 on 2024-07-30 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_home_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicationattachment',
            name='file_type',
            field=models.CharField(editable=False, max_length=10, verbose_name='Type de média'),
        ),
    ]