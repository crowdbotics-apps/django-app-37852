# Generated by Django 2.2.28 on 2022-12-09 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20221209_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='domain_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='plans',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
