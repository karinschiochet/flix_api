# Generated by Django 5.0.6 on 2024-06-12 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='nationality',
            field=models.CharField(blank=True, choices=[('USA', 'Estados Unidos'), ('BRA', 'Brasil'), ('ESP', 'Espanha'), ('FRA', 'França'), ('URY', 'Uruguai'), ('TUR', 'Turquia')], max_length=100, null=True),
        ),
    ]