# Generated by Django 5.0.6 on 2024-06-12 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='resume',
            field=models.TextField(blank=True, null=True),
        ),
    ]