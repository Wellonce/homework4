# Generated by Django 4.2.7 on 2024-01-18 11:35

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=28)),
                ('code', models.UUIDField(default=uuid.uuid4)),
                ('is_active', models.BooleanField(default=False)),
                ('start_date', models.DateField()),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
            options={
                'verbose_name': 'Speciliality',
                'verbose_name_plural': 'Specilialities',
                'db_table': 'speciality',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=28)),
                ('last_name', models.CharField(max_length=28)),
                ('degree', models.CharField(choices=[('master', 'Master'), ('bachelor', 'Bachelor'), ('academic', 'Academic'), ('drscience', 'DrScience'), ('phs', 'PhD')], max_length=9)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
            options={
                'verbose_name': 'Teacher',
                'verbose_name_plural': 'Teachers',
                'db_table': 'teacher',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=28)),
                ('speciality', models.ManyToManyField(related_name='subjects', to='courses.speciality')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='courses.teacher')),
            ],
            options={
                'verbose_name': 'Subject',
                'verbose_name_plural': 'Subjects',
                'db_table': 'subject',
            },
        ),
    ]