# Generated by Django 2.0.7 on 2018-07-19 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brochure', '0004_affiliate_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='chin_abstract',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='speaker',
            name='chin_degree',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='speaker',
            name='chin_subject',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='speaker',
            name='chin_title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='speaker',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='degree',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
