# Generated by Django 3.2.9 on 2021-12-08 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_building', models.CharField(max_length=30)),
                ('building_level', models.PositiveSmallIntegerField()),
                ('building_health', models.PositiveIntegerField()),
                ('stone', models.PositiveSmallIntegerField()),
                ('wood', models.PositiveSmallIntegerField()),
                ('iron', models.PositiveSmallIntegerField()),
                ('size_warehouse', models.PositiveIntegerField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='buildings',
            name='id_unit',
        ),
    ]
