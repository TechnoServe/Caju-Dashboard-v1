# Generated by Django 3.2.5 on 2021-11-08 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_beninyield'),
    ]

    operations = [
        migrations.RenameField(
            model_name='beninyield',
            old_name='total_number_tress',
            new_name='total_number_trees',
        ),
    ]
