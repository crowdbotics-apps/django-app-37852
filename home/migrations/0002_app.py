# Generated by Django 2.2.28 on 2022-12-09 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_load_initial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'app',
            },
        ),
    ]
