# Generated by Django 4.0.4 on 2022-04-22 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('days_meals', '0008_remove_daymeal_portion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daymeal',
            name='day',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
