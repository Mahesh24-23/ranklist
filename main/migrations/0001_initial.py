# Generated by Django 4.0.2 on 2022-02-14 08:00

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appid', models.IntegerField(max_length=8, unique=True)),
                ('name', models.CharField(max_length=20)),
                ('father_name', models.CharField(max_length=20)),
                ('phone_no', models.CharField(max_length=10)),
                ('email_id', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m1', models.IntegerField(max_length=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('m2', models.IntegerField(max_length=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('m3', models.IntegerField(max_length=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('m4', models.IntegerField(max_length=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('appid', models.ForeignKey(max_length=8, on_delete=django.db.models.deletion.CASCADE, to='main.personal')),
            ],
        ),
    ]
