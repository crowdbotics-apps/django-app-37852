# Generated by Django 2.2.28 on 2022-12-09 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_subscription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='app',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.App'),
        ),
    ]
