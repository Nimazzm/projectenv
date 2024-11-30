# Generated by Django 5.1.2 on 2024-10-18 07:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, null=True)),
                ('duration', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=70, null=True)),
                ('last_name', models.CharField(max_length=70, null=True)),
                ('fee_per_hour', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, null=True)),
                ('start_date', models.DateField(null=True)),
                ('task', models.ManyToManyField(to='app_project.task')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manager_set', to='app_project.worker'),
        ),
        migrations.AddField(
            model_name='task',
            name='workers',
            field=models.ManyToManyField(related_name='workers_set', to='app_project.worker'),
        ),
    ]
