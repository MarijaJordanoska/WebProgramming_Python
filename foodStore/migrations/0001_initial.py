# Generated by Django 4.0.5 on 2022-06-28 14:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_category', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime', models.CharField(max_length=50)),
                ('prezime', models.CharField(max_length=50)),
                ('adress', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(default=0)),
                ('name_food', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('kategorija', models.CharField(max_length=50)),
                ('food_image', models.ImageField(blank=True, null=True, upload_to='food_image/')),
                ('price', models.IntegerField(default=0)),
                ('amount', models.IntegerField(default=0)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datum', models.DateField()),
                ('ime_prezime', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='foodStore.client')),
                ('sold_food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodStore.food')),
            ],
        ),
    ]
