# Generated by Django 5.1.6 on 2025-02-17 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('source', models.CharField(max_length=255)),
                ('destination', models.CharField(max_length=255)),
                ('total_seats', models.IntegerField()),
                ('available_seats', models.IntegerField()),
            ],
        ),
    ]
