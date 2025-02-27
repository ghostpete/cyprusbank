# Generated by Django 5.1.4 on 2025-02-27 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_customuser_can_apply_for_cards'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='account_category',
            field=models.CharField(choices=[('Individual', 'Individual'), ('Business', 'Business')], default='Individual', max_length=100),
        ),
    ]
