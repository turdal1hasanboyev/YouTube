# Generated by Django 5.1.1 on 2024-09-08 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_alter_category_is_active_alter_channel_is_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(blank=True, max_length=225, null=True, unique=True),
        ),
    ]
