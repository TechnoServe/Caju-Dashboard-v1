# Generated by Django 4.0.1 on 2022-01-22 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_alter_remuser_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='remuser',
            name='email',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]