# Generated by Django 3.2.5 on 2021-11-10 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0015_auto_20211110_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beninyield',
            name='plantation_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='beninyield',
            name='product_id',
            field=models.CharField(max_length=60),
        ),
    ]
