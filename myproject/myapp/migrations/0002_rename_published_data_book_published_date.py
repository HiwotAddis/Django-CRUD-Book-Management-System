# Generated by Django 5.1.5 on 2025-02-20 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='published_data',
            new_name='published_date',
        ),
    ]
