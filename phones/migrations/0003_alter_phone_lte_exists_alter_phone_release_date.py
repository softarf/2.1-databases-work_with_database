# Generated by Django 4.2.1 on 2023-06-03 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0002_alter_phone_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='lte_exists',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='release_date',
            field=models.CharField(null=True),
        ),
    ]