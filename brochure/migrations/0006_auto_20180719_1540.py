# Generated by Django 2.0.7 on 2018-07-19 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brochure', '0005_auto_20180719_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='chin_profile',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='speaker',
            name='profile',
            field=models.TextField(blank=True),
        ),
    ]
