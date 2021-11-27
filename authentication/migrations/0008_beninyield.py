# Generated by Django 3.2.5 on 2021-11-08 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_auto_20210814_0251'),
    ]

    operations = [
        migrations.CreateModel(
            name='BeninYield',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plantation_name', models.CharField(max_length=200, unique=True)),
                ('department', models.CharField(max_length=200)),
                ('commune', models.CharField(max_length=200)),
                ('arrondissement', models.CharField(max_length=200)),
                ('village', models.CharField(max_length=200)),
                ('owner_first_name', models.CharField(max_length=200)),
                ('owner_last_name', models.CharField(max_length=200)),
                ('plantation_code', models.CharField(max_length=200)),
                ('surface_area', models.FloatField(null=True)),
                ('total_yield_kg', models.FloatField()),
                ('total_yield_per_ha_kg', models.FloatField()),
                ('total_yield_per_tree_kg', models.FloatField()),
                ('sex', models.CharField(max_length=200)),
                ('product_id', models.CharField(max_length=60, unique=True)),
                ('total_number_tress', models.FloatField()),
                ('total_sick_trees', models.FloatField()),
                ('total_dead_trees', models.FloatField()),
                ('total_trees_out_of_prod', models.FloatField()),
                ('plantation_age', models.FloatField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField(null=True)),
                ('altitude', models.FloatField(null=True)),
                ('status', models.IntegerField(choices=[(1, 'Active'), (0, 'Inactive')], default=1)),
                ('year', models.IntegerField()),
                ('plantation_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.plantation')),
            ],
        ),
    ]