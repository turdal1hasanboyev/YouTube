# Generated by Django 5.1.1 on 2024-09-08 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='is_active',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
